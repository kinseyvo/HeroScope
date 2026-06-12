import requests

API_TOKEN = "YOUR_TOKEN_HERE"
BASE_URL = f"https://superheroapi.com/api/{API_TOKEN}"

def search_hero(name):
  url = f"{BASE_URL}/search/{name}"
  response = requests.get(url)
  data = response.json()

  if data["response"] == "success":
    return data["results"][0]
  return None


def get_hero_insight(hero_name):
  hero = search_hero(hero_name)

  if not hero:
    return {"hero": hero_name, "insight": "Hero not found."}
  
  powerstats = hero["powerstats"]

  return {
    "hero": hero["name"],
    "insight": f"Power: {powerstats['power']}, Intelligence: {powerstats['intelligence']}"
  }


def get_live_insights():
  heroes = ["Batman", "Spider-Man", "Iron Man"]
  
  return [get_hero_insight(hero) for hero in heroes]
