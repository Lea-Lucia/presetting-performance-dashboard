import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Presetting Performance Dashboard")

data = {
    "Datum": ["2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10"],
    "Anwahlen": [156, 130, 105, 95],
    "Erreicht": [19, 17, 21, 15],
    "Zielgruppe": [11, 11, 15, 11],
    "Termine": [3, 4, 7, 5]
}

df = pd.DataFrame(data)
df["Terminquote"] = df["Termine"] / df["Zielgruppe"]

gesamt_termine = df["Termine"].sum()
terminquote = df["Terminquote"].mean()

col1, col2 = st.columns(2)
col1.metric("Gesamttermine", gesamt_termine)
col2.metric("Ø Terminquote", f"{terminquote:.1%}")

st.line_chart(df.set_index("Datum")["Terminquote"])
st.bar_chart(df.set_index("Datum")["Termine"])
