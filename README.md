# 🚀 Python JSON Event Processing Pipeline

A Python-based Data Engineering project that processes JSON events, generates statistical metrics in CSV format, handles invalid records through a dead-letter mechanism, and includes automated unit testing.

---

# 📖 Overview

This project simulates a lightweight Data Engineering pipeline responsible for:

* Reading events from a JSON file
* Validating event structure and timestamps
* Filtering events from the last 30 days
* Generating business and operational metrics
* Storing invalid events in a dead-letter file
* Executing automated unit tests

The solution was intentionally developed using only Python's standard library to demonstrate core programming, data processing, validation, and error-handling concepts without external dependencies.

---

# 🛠️ Technologies Used

* Python 3.8+
* Built-in Libraries:

  * `json`
  * `csv`
  * `datetime`
  * `unittest`

> No third-party packages are required.

---

# 📂 Project Structure

```text
PRJ_PY_JSON
│
├── GeraDados/
│   ├── cria_json_2026.py
│   └── events.json
│
├── src/
│   ├── processor.py
│   ├── events.json
│   ├── stats.csv
│   ├── deadletter.json
│   └── .gitignore
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/gitvitct/PRJ_PY_JSON.git
cd PRJ_PY_JSON
```

## Create a Virtual Environment

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

> The project uses only native Python libraries. The requirements file is provided for future extensibility.

---

# ▶️ Running the Application

Navigate to the source directory and execute the processor:

```bash
cd src
python3 processor.py
```

The script will:

1. Read the JSON event file.
2. Validate event records.
3. Filter events from the last 30 days.
4. Generate statistical metrics.
5. Create a CSV report.
6. Save invalid records to the dead-letter file.

---

# 📥 Expected JSON Format

The `events.json` file must contain a list of event objects following the structure below:

```json
[
  {
    "user_id": "user1",
    "event_type": "login",
    "timestamp": "2026-05-01T10:00:00Z"
  },
  {
    "user_id": "user2",
    "event_type": "purchase",
    "timestamp": "2026-05-02T12:30:00Z",
    "amount": 150.75
  }
]
```

---

# 📊 Example Output (`stats.csv`)

```csv
metric,value
unique_users,491
event_login,686
event_logout,636
event_purchase,664
total_purchase_amount,164286.16
average_purchase_amount,247.42
```

Generated metrics include:

* Total unique users
* Event counts by type
* Total purchase amount
* Average purchase amount

---

# 🚨 Error Handling

The pipeline includes validation and error-handling mechanisms for the following scenarios:

* Missing JSON file
* Invalid JSON syntax
* Invalid timestamp format
* Missing required fields
* Unexpected event structure
* Malformed purchase events
* Unexpected runtime exceptions

Invalid records are automatically redirected to the `deadletter.json` file for further analysis.

---

# 🧪 Unit Testing

The project includes automated unit tests using Python's built-in `unittest` framework.

Run the tests with:

```bash
python -m unittest discover
```

The tests validate:

* JSON loading
* Event filtering
* Data validation
* Metrics calculation
* Dead-letter processing
* Error handling scenarios

---

# 📈 Data Pipeline Flow

```text
events.json
      │
      ▼
Read JSON File
      │
      ▼
Validate Records
      │
      ├── Valid Records ──► Generate Metrics ──► stats.csv
      │
      └── Invalid Records ──► deadletter.json
```

---

# 🎯 Learning Objectives

This project demonstrates key Data Engineering concepts, including:

* Data ingestion
* Data validation
* Data quality checks
* Event processing
* Dead-letter handling
* Metrics generation
* Automated testing
* Python data pipelines

It is designed as a portfolio project to showcase foundational Data Engineering and Python development skills.
