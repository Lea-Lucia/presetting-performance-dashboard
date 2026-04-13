import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Presetting Performance Dashboard")

csv_url = "https://docs.google.com/spreadsheets/d/1gJjgZT313SNeXrHHK06t81jJG4LmkAOEMcXhmiL-EoQ/export?format=csv&gid=1484787871"
df = pd.read_csv(csv_url)

st.subheader("Spalten im Sheet")
st.write(df.columns.tolist())

st.subheader("Vorschau")
st.dataframe(df.head())
st.subheader("Sales Funnel")

funnel_data = pd.DataFrame({
    "Stage": ["Anwahlen", "Erreicht", "Zielgruppe", "Termine"],
    "Value": [
        df["Anwahlen"].sum(),
        df["Erreicht"].sum(),
        df["Zielgruppe"].sum(),
        df["Termine"].sum()
    ]
})

st.bar_chart(funnel_data.set_index("Stage"))

st.subheader("Forecast Szenario")

fuehrung_boost = st.slider("Führung verbessern", 0.0, 1.0, 0.3)

forecast_termine = int(gesamt_termine * (1 + fuehrung_boost * 0.2))
st.metric("Forecast Termine", forecast_termine)

st.subheader("Peak-Day DNA")

peak_compare = pd.DataFrame({
    "Kennzahl": ["Peak Terminquote", "Durchschnitt"],
    "Wert": [
        peak["Terminquote"].iloc[0],
        df["Terminquote"].mean()
    ]
})

st.dataframe(peak_compare)
