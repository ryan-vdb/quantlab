import numpy as np
import pandas as pd

def meanReversion(data):
    results = {}
    for col in data.columns:
        s = pd.Series(data[col])
        n = len(s)
        t = np.arange(n)
        y = np.log(s.values)
        t_mean = t.mean()
        y_mean = y.mean()
        slope = np.sum((t - t_mean) * (y - y_mean)) / np.sum((t - t_mean)**2)
        intercept = y_mean - slope * t_mean
        exp_ys = intercept + slope * t
        exp_ps = np.exp(exp_ys)
        residuals = s.values - exp_ps
        error_threshold = residuals.std()
        current_price = s.iloc[-1]
        exp_current_price = exp_ps[-1]
        error = current_price - exp_current_price

        if error > 2 * error_threshold:
            results[col] = -100 / current_price
        elif error < -2 * error_threshold:
            results[col] = 100 / current_price
        else:
            continue
    return pd.Series(results, name = "shares")