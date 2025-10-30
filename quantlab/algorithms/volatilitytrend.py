import numpy as np
import pandas as pd

def volatilityTrend(data):
    results = {}
    for col in data.columns:
        s = pd.Series(data[col])
        y = np.log(s)
        vol_short = y[-10:].std()
        vol_long = y[-60:].std()
        vol_ratio = vol_short / vol_long
        current_price = s.iloc[-1]
        past_price = s.iloc[-10]
        price_movement = np.sign(current_price - past_price)
        
        if vol_ratio > 1.25:
            results[col] = price_movement * (100 / current_price)
        else:
            continue
    return pd.Series(results, name = "shares")