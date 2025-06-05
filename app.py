import streamlit as st
from screener import get_breakout_stocks
from filters import apply_filters

st.set_page_config(page_title="Breakout Screener", layout="wide")
st.title("📈 Indian Market Breakout Screener")
st.markdown("Filter breakout stocks using technical + fundamental rules.")

with st.spinner("Fetching breakout stocks..."):
    stocks = get_breakout_stocks()
    filtered = apply_filters(stocks)

st.success(f"✅ {len(filtered)} stocks found!")
st.dataframe(filtered)