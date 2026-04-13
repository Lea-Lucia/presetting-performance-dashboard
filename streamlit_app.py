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
