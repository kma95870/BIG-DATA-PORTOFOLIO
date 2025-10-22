import os, json, requests
from datetime import datetime, timezone

#COORDONNEES DE PARIS
LAT, LON = 48.8566, 2.3522

def fetch_openmeteo():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LAT}&longitude={LON}"
        "&hourly=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m"
        "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max"
        "&timezone=Europe%2FParis"
    )
    r = requests.get(url, timeout=30) #évite que le script blpque plus de 30s si API rep pas
    r.raise_for_status()
    return r.json()

def save_raw(playload):
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    outdir = os.path.join("data","raw",ts[:8]) #création chemin dossier (partion journalière)
    os.makedirs(outdir,exist_ok=True) #création dossier si inexistant
    path = os.path.join(outdir, f"openmeteo_{ts}.json") #construction du chemin complet du fichier
    with open(path, "w", encoding= "utf-8") as f: #ouvre fichier en écriture
        json.dump(playload,f,ensure_ascii=False) #dump écrit fichier 
    print(path)
    return path

def main():
    data = fetch_openmeteo()
    save_raw(data)

if __name__ == "__main__":
    main()

