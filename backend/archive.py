from database import get_connection

def initialize_database():
  conn = get_connection()

  conn.execute("""
    CREATE TABLE IF NOT EXISTS hero_snapshots (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      hero_name TEXT,
      intelligence INTEGER,
      power INTEGER,
      speed INTEGER,
      collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
  """)

  conn.commit()
  conn.close()
