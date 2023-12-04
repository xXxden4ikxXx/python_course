import pandas as pd
import matplotlib.pyplot as plt

emojis = pd.read_csv('emojis.csv')

emojis_created = emojis['Year'].value_counts().sort_index()

print(emojis_created)

emojis_created.plot()
plt.show()

