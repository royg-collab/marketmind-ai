# 🧠 System Architecture – MarketMind AI

## Overview
MarketMind AI is a modular GenAI-powered system designed to simplify stock analysis for retail investors.

---

## 🔧 Components

### 1. Data Agent
- Fetches stock data using yfinance
- Retrieves historical price data

### 2. Indicator Engine
- Calculates:
  - Moving Average 50 (MA50)
  - Moving Average 200 (MA200)

### 3. Signal Agent
- Applies rule-based logic:
  - MA50 > MA200 → BUY
  - MA50 < MA200 → SELL

### 4. GenAI Explainer
- Uses OpenAI API
- Converts signals into human-readable explanations

### 5. UI Layer
- Built using Streamlit
- Allows user interaction and displays results

---

## 🔄 Workflow

User Input → Data Fetch → Indicators → Signal → AI Explanation → Output

---

## ⚠️ Error Handling

- Invalid stock → user prompt
- API failure → fallback explanation
- Missing data → safe defaults

---

## 🧠 Key Innovation

Instead of only generating signals, the system explains *why* a decision is made using Generative AI, improving interpretability.