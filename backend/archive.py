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

def save_snapshot(hero):
  conn = get_connection()

  conn.execute(
    """
    INSERT INTO hero_snapshots
    (
        hero_name,
        intelligence,
        power,
        speed
    )
    VALUES (?, ?, ?, ?)
    """,
    (
        hero["name"],
        hero["powerstats"]["intelligence"],
        hero["powerstats"]["power"],
        hero["powerstats"]["speed"]
    )
  )

  conn.commit()
  conn.close()

def get_history():
  conn = get_connection()

  rows = conn.execute("""
      SELECT *
      FROM hero_snapshots
      ORDER BY collected_at DESC
  """).fetchall()

  conn.close()

  return rows
