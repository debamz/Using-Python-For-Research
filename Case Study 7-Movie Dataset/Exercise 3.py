df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna(how="any")

df.shape
