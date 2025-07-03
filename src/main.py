# src/main.py
import numpy as np
import pandas as pd

data = {
    "temperature": [25.1, 26.3, 24.7],
    "humidity": [55, 60, 65]
}

df = pd.DataFrame(data)
print("✅ Running from subdirectory:")
print(df)
