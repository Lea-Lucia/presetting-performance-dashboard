import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Presetting Performance Dashboard")

csv_url = "https://docs.google.com/spreadsheets/d/1gJjgZT313SNeXrHHK06t81jJG4LmkAOEMcXhmiL-EoQ/export?format=csv&gid=1484787871"
df = pd.read_csv(csv_url)

df["Terminquote"] = df["Termine"] / df["Zielgruppe"]

gesamt_termine = df["Termine"].sum()
terminquote = df["Terminquote"].mean()

col1, col2 = st.columns(2)
col1.metric("Gesamttermine", gesamt_termine)
col2.metric("Ø Terminquote", f"{terminquote:.1%}")

st.line_chart(df.set_index("Datum")["Terminquote"])
st.bar_chart(df.set_index("Datum")["Termine"])
