import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 10, size=(10, 10)))

letters = 'abcdefghij'
df.index = [*letters]

for letter in letters:
    if all(df.loc[letter] > 5):
        print(df.loc[letter])
