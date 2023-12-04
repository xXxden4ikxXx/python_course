import pandas as pd

emojis = pd.read_csv('emojis.csv')

print("Самая популярная подкатегория: ", emojis['Subcategory'][0])
