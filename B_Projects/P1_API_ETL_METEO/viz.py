import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

ENGINE_URL = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5433/etl_db"

@st.cache_data(ttl=600)
def load_data():
    engine = create_engine(ENGINE_URL)
    daily = pd.read_sql("SELECT * FROM weather_daily ORDER BY date DESC", engine)
    hourly = pd.read_sql("SELECT * FROM weather_hourly ORDER BY time DESC LIMIT 500", engine)
    return daily, hourly

st.title("🌦️ Météo Paris — ETL Dashboard")
daily, hourly = load_data()

col1, col2, col3 = st.columns(3)
col1.metric("Jours chargés", daily["date"].nunique())
col2.metric("Tx max (dernier jour)", f"{daily.iloc[0]['tmax_c']:.1f} °C")
col3.metric("Précip. (dernier jour)", f"{daily.iloc[0]['precip_sum_mm']:.1f} mm")

st.subheader("T° min / max par jour")
st.line_chart(daily.set_index("date")[["tmin_c","tmax_c"]])

st.subheader("Vent horaire (derniers points)")
st.area_chart(hourly.set_index("time")[["wind_speed_10m"]])
