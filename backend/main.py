from fastapi import FastAPI
from insights import get_live_insights

app = FastAPI()

@app.get("/")
def root():
  return {"message": "HeroScope API is online"}

@app.get("/insights")
def insights():
  return get_live_insights()
