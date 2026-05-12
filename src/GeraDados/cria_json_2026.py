import json
import random
from datetime import datetime, timedelta

# Config
NUM_REGISTROS = 10000
OUTPUT_FILE = "events.json"

event_types = ["login", "purchase", "logout"]
users = [f"user{i}" for i in range(1, 501)]  # 500 usuários únicos

# Data inicial fixa
start_date = datetime(2026, 1, 1)

# Data final = agora
end_date = datetime.now()

# Diferença total em segundos entre as datas
total_seconds = int((end_date - start_date).total_seconds())

data = []

for _ in range(NUM_REGISTROS):
    event_type = random.choice(event_types)

    # Gera um instante aleatório entre 01/01/2026 e agora
    random_seconds = random.randint(0, total_seconds)
    timestamp = start_date + timedelta(seconds=random_seconds)

    # Amount só para purchase
    amount = round(random.uniform(10, 500), 2) if event_type == "purchase" else None

    record = {
        "user_id": random.choice(users),
        "event_type": event_type,
        "timestamp": timestamp.isoformat() + "Z",
        "amount": amount
    }

    data.append(record)

# Salvar JSON
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print(f"{NUM_REGISTROS} registros gerados em {OUTPUT_FILE}")
print(f"Período: {start_date} até {end_date}")