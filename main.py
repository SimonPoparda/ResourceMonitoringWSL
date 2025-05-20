import psycopg2
import psutil
from datetime import datetime

# Połączenie z PostgreSQL
conn = psycopg2.connect(
    dbname="monitoring_project",
    user="monitoring_user",
    password="root",
    host="localhost"
)
cur = conn.cursor()

# Stwórz tabelę (jeśli nie istnieje)
cur.execute("""
CREATE TABLE IF NOT EXISTS procesy (
    id SERIAL PRIMARY KEY,
    pid INTEGER,
    name TEXT,
    cpu REAL,
    memory REAL,
    timestamp TIMESTAMP
)
""")
conn.commit()

# Zbieranie danych
for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
    try:
        cur.execute(
            "INSERT INTO procesy (pid, name, cpu, memory, timestamp) VALUES (%s, %s, %s, %s, %s)",
            (
                proc.info['pid'],
                proc.info['name'],
                proc.info['cpu_percent'],
                proc.info['memory_percent'],
                datetime.now()
            )
        )
    except Exception as e:
        print(f"Problem z procesem: {e}")

conn.commit()
cur.close()
conn.close()
print("Zapisano dane:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

