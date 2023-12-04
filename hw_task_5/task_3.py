import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 10, size=(10, 10)))

letters = 'abcdefghij'
df.index = [*letters]
df.columns = [*letters]

print(df.shape)
print(df.columns)
print(df.mean().mean())

df.to_csv('df_10x10.csv')