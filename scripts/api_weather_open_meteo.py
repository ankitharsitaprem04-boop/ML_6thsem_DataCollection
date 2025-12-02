# scripts/api_weather_open_meteo.py
import requests
import pandas as pd
from datetime import datetime

# Example coordinates: Delhi approx (lat=28.6, lon=77.2)
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 28.6,
    "longitude": 77.2,
    "hourly": "temperature_2m",
    "start_date": datetime.utcnow().strftime("%Y-%m-%d"),
    "end_date": datetime.utcnow().strftime("%Y-%m-%d"),
    "timezone": "UTC"
}

r = requests.get(url, params=params, timeout=10)
r.raise_for_status()
data = r.json()

times = data["hourly"]["time"]
temps = data["hourly"]["temperature_2m"]
df = pd.DataFrame({"time_utc": times, "temp_c": temps})
out = "datasets/weather_open_meteo.csv"
df.to_csv(out, index=False)
print("Saved:", out, "Rows:", len(df))
