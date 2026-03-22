import streamlit as st

def detect_signal(data):
    latest = data.iloc[-1]

    st.write("TYPE:", type(latest))
    st.write("DATA:", latest)

    ma50 = float(latest['MA50'])
    ma200 = float(latest['MA200'])

    if ma50 > ma200:
        return "BUY"
    elif ma50 < ma200:
        return "SELL"
    else:
        return "HOLD"