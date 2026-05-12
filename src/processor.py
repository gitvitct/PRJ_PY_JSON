import json
import csv
import unittest
from datetime import datetime, timedelta

# =========================
# CONFIGURAÇÕES
# =========================

INPUT_FILE = "events.json"
DEADLETTER_FILE = "deadletter.json"
STATS_FILE = "stats.csv"

####################################################################################################################################################
# =========================
# FUNÇÕES UTILITÁRIAS
# =========================

##---------------------------------------------------------------------------------------------------------------------
def is_valid_timestamp(timestamp_str):
    """
    Valida se o timestamp está no formato ISO.
    """
    try:
        datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")
        return True
    except (ValueError, TypeError):
        return False


##---------------------------------------------------------------------------------------------------------------------
def is_recent_event(timestamp_str, days=30):
    """
    Verifica se o evento pertence aos últimos X dias.
    """
    event_date = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")
    limit_date = datetime.now() - timedelta(days=days)

    return event_date >= limit_date



##---------------------------------------------------------------------------------------------------------------------
def validate_event(event):
    """
    Valida estrutura obrigatória do evento.
    """
    required_fields = ["user_id", "event_type", "timestamp"]

    for field in required_fields:
        if field not in event:
            return False, f"Campo ausente: {field}"

    if not is_valid_timestamp(event["timestamp"]):
        return False, "Timestamp inválido"

    return True, None



##---------------------------------------------------------------------------------------------------------------------
def count_unique_users(events):
    """
    Conta quantidade de user_id únicos.
    """
    unique_users = set()

    for event in events:
        unique_users.add(event["user_id"])

    return len(unique_users)



##---------------------------------------------------------------------------------------------------------------------
def sum_purchase_amount(events):
    """
    Soma o valor total de compras,
    conta quantas compras válidas existem
    e calcula a média de compras.
    """

    total_purchase_amount = 0.0
    purchase_count = 0

    for event in events:
        event_type = event.get("event_type")
        amount = event.get("amount")

        # Estatísticas de compra
        if event_type == "purchase" and amount is not None:
            total_purchase_amount += float(amount)
            purchase_count += 1

    # Média de compra
    average_purchase_amount = (
        total_purchase_amount / purchase_count
        if purchase_count > 0
        else 0
    )

    return total_purchase_amount, average_purchase_amount



##---------------------------------------------------------------------------------------------------------------------
def count_events_by_type(events):
    """
    Conta quantos eventos existem por tipo de evento.
    Retorna uma lista pronta para CSV.
    
    Retorna um dicionário no formato:
    {
        "event_login": 10,
        "event_purchase": 5,
        "event_logout": 8
    }
    """

    event_counts = {}
    stats = []

    for event in events:
        event_type = event.get("event_type")

        # Contagem por tipo de evento
        if event_type:
            key = f"event_{event_type}"
            event_counts[key] = event_counts.get(key, 0) + 1

     # Adicionar eventos dinamicamente
    for event_name, count in sorted(event_counts.items()):
        stats.append([event_name, count])

    return stats




####################################################################################################################################################
# =========================
# PROCESSAMENTO PRINCIPAL
# =========================


##---------------------------------------------------------------------------------------------------------------------
def process_events():
    
    valid_events = []
    deadletter_events = []

    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("O JSON deve conter uma lista de eventos.")

        for event in data:

            # Validar estrutura
            is_valid, error_message = validate_event(event)

            if not is_valid:
                deadletter_events.append({
                    "event": event,
                    "error": error_message
                })
                continue

            # Filtrar últimos 30 dias
            if not is_recent_event(event["timestamp"]):
                continue

            valid_events.append(event)

        # Processa DEF/Metricas ######################################################################################
        total_unique_users = count_unique_users(valid_events)
        total_purchase_amount, average_purchase_amount = sum_purchase_amount(valid_events)        
        stats = count_events_by_type(valid_events)
        #total_event_counts, stats = count_events_by_type(valid_events)



        # Gerar CSV de estatísticas -----------------------------------------------------------------------
        with open(STATS_FILE, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow(["metric", "value"])
            writer.writerow(["unique_users", total_unique_users])
            
            ## Pivot Eventos Validos
            for row in stats:
                writer.writerow(row)

            writer.writerow(["total_purchase_amount", round(total_purchase_amount, 2)])          
            writer.writerow(["average_purchase_amount", round(average_purchase_amount, 2)])            
            


        # Gerar deadletter -----------------------------------------------------------------------
        with open(DEADLETTER_FILE, "w", encoding="utf-8") as deadfile:
            json.dump(deadletter_events, deadfile, indent=4)


        # Print Validacoes -----------------------------------------------------------------------
        print("Processamento concluído com sucesso.")
        print(f"Eventos válidos: {len(valid_events)}")
        print(f"Eventos inválidos: {len(deadletter_events)}")
        #print(f"Usuários únicos: {total_unique_users}")
        #print(f"Soma Total: {total_purchase_amount}")
        #print(f"Media: {average_purchase_amount}")
        #print(f"Media: {stats}")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{INPUT_FILE}' não encontrado.")

    except json.JSONDecodeError:
        print("Erro: JSON inválido.")

    except Exception as error:
        print(f"Erro inesperado: {error}")




####################################################################################################################################################
# =========================
# TESTES UNITÁRIOS
# =========================


##---------------------------------------------------------------------------------------------------------------------
class TestEventProcessing(unittest.TestCase):

    def test_valid_timestamp(self):
        self.assertTrue(
            is_valid_timestamp("2026-05-01T10:00:00Z")
        )

    def test_invalid_timestamp(self):
        self.assertFalse(
            is_valid_timestamp("01-05-2026")
        )

    def test_validate_event_success(self):
        event = {
            "user_id": "user1",
            "event_type": "login",
            "timestamp": "2026-05-01T10:00:00Z"
        }

        valid, _ = validate_event(event)

        self.assertTrue(valid)

    def test_validate_event_missing_field(self):
        event = {
            "user_id": "user1",
            "timestamp": "2026-05-01T10:00:00Z"
        }

        valid, error = validate_event(event)

        self.assertFalse(valid)
        self.assertEqual(error, "Campo ausente: event_type")

    def test_count_unique_users(self):
        events = [
            {"user_id": "user1"},
            {"user_id": "user2"},
            {"user_id": "user1"}
        ]

        result = count_unique_users(events)

        self.assertEqual(result, 2)



####################################################################################################################################################
# =========================
# EXECUÇÃO
# =========================

if __name__ == "__main__":
    process_events()

    print("\nExecutando testes unitários...\n")

    unittest.main(argv=["first-arg-is-ignored"], exit=False)