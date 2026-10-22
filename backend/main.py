from fastapi import FastAPI
from insights import get_live_insights
from archive import initialize_database
from archive import get_history

app = FastAPI()

initialize_database()

@app.get("/")
def root():
  return {"message": "HeroScope API is online"}

@app.get("/insights")
def insights():
  return get_live_insights()

@app.get("/history")
def history():
  return get_history()
