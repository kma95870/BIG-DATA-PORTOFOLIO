import os, json, pandas as pd 
from glob import glob

def latest_raw_path():
    parts = sorted(glob("data/raw/*")) #Trie par ordre chrono liste des sous dossier de data/raw
    if not parts: raise FileNotFoundError("Aucun Fichier Brut")
    latest_dir = parts[-1] #prend le dernier dossier = + récent
    files = sorted(glob(os.path.join(latest_dir,"openmeteo_*.json")))
    if not files: raise FileNotFoundError("Aucun JSON dans le fichier")
    return files[-1]

def transform(path_json):
    with open(path_json,"r", encoding= "utf-8") as f:
        payload = json.load(f) #Convertit le JSON en dictionnaire Python dans payload
    
    h = payload["hourly"]
    df_hourly = pd.DataFrame({
        "time": pd.to_datetime(h["time"]),
        "temp_c": h["temperature_2m"],
        "humidity": h["relative_humidity_2m"],
        "precip_mm": h["precipitation"],
        "wind_speed_10m": h["wind_speed_10m"],
    }).assign(city="Paris", lat=payload["latitude"], lon=payload["longitude"])

    d = payload["daily"]
    df_daily = pd.DataFrame({
        "date": pd.to_datetime(d["time"]).date,
        "tmax_c": d["temperature_2m_max"],
        "tmin_c": d["temperature_2m_min"],
        "precip_sum_mm": d["precipitation_sum"],
        "wind_10m_max": d["wind_speed_10m_max"],
    }).assign(city="Paris")  

    os.makedirs("data/processed", exist_ok=True)
    df_hourly.to_parquet("data/processed/hourly.parquet", index=False)
    df_daily.to_parquet("data/processed/daily.parquet", index=False)
    print("data/processed/hourly.parquet")
    print("data/processed/daily.parquet")

def main():
    path = latest_raw_path()
    transform(path)

if __name__ == "__main__":
    main()     