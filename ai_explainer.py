def explain_signal(signal, price, ma50, ma200):

    if "BUY" in signal:
        return f"""
The stock is currently trading above its 200-day moving average, which indicates a strong long-term upward trend.

This suggests bullish momentum in the market.

However, investors should be cautious of short-term fluctuations and confirm with additional indicators.
"""

    elif "SELL" in signal:
        return f"""
The stock is trading below its 200-day moving average, indicating a downward trend.

This suggests bearish sentiment and potential weakness.

Investors should be careful and avoid entering without further confirmation.
"""

    else:
        return f"""
The stock is not showing a clear trend based on moving averages.

It is better to wait for a clearer signal before making a decision.
"""