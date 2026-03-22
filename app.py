import streamlit as st
import yfinance as yf
from indicators import add_indicators
from signal_agent import detect_signal
from ai_explainer import explain_signal

# Page config
st.set_page_config(page_title="MarketMind AI", layout="centered")

# Title
st.title("📊 MarketMind AI")
st.subheader("AI-Powered Stock Insight Assistant")

# Input
ticker = st.text_input("Enter Stock Symbol (e.g., RELIANCE.NS)", "RELIANCE.NS")

if st.button("Analyze"):

    with st.spinner("Analyzing market trends..."):

        data = yf.download(ticker, period="1y", interval="1d")
        data = add_indicators(data)

        signal = detect_signal(data)

        latest = data.iloc[-1]

        explanation = explain_signal(
            signal,
            latest['Close'],
            latest['MA50'],
            latest['MA200']
        )

    # 📊 Show Data
    st.markdown("### 📊 Latest Stock Data")
    st.dataframe(data[['Close','MA50','MA200']].tail())

    # 📢 Show Signal (COLOR BASED)
    st.markdown("### 📢 Signal")

    if signal == "BUY":
        st.success(f"📈 {signal}")
    elif signal == "SELL":
        st.error(f"📉 {signal}")
    else:
        st.warning(f"⚖️ {signal}")

    # 🤖 AI Explanation
    st.markdown("### 🤖 AI Explanation")
    st.info(explanation)