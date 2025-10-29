import numpy as np
import pandas as pd

def momentum(data):
    results = {}
    for col in data.columns:
        s = pd.Series(data[col])
        current_price = s.iloc[-1]
        past_price = s.iloc[-8]
        change = np.log(current_price / past_price)
        daily_returns = np.log(s/s.shift(1))
        vol = daily_returns.iloc[-8:].std(ddof = 1)
        threshold = 0.75 * vol * np.sqrt(8)

        if change > threshold:
            results[col] = 100 / current_price
        elif change < threshold:
            results[col] = -100 / current_price
        else:
            continue
    return pd.Series(results, name = "shares")


    