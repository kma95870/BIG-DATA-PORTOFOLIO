import pandas as pd
from sqlalchemy import create_engine, text

ENGINE_URL = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5433/etl_db"
# (127.0.0.1 évite certains soucis IPv6 de 'localhost' sous Windows)

def get_engine():
    return create_engine(
        ENGINE_URL,
        pool_pre_ping=True,
        connect_args={"connect_timeout": 5},
    )

def main():
    engine = get_engine()
    # test rapide de connexion
    with engine.connect() as conn:
        print("✅ DB:", conn.execute(text("SELECT current_database()")).scalar())

    # chargement des Parquet
    df_hourly = pd.read_parquet("data/processed/hourly.parquet")
    df_daily  = pd.read_parquet("data/processed/daily.parquet")

    df_hourly.to_sql("weather_hourly", engine, if_exists="replace", index=False)
    df_daily.to_sql("weather_daily", engine, if_exists="replace", index=False)
    print("✅ Chargé dans Postgres (Docker).")

if __name__ == "__main__":
    main()
