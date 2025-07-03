# main.py
import numpy as np
import pandas as pd

data = {
    "temperature": [22.5, 23.0, 21.8],
    "humidity": [60, 65, 70]
}

df = pd.DataFrame(data)
print("📊 Sample DataFrame:")
print(df)

average_temp = np.mean(df["temperature"])
print(f"\n🌡️ Average Temperature: {average_temp:.2f}°C")
