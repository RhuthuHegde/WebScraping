import numpy as np
import pandas as pd

df = pd.read_excel('converted.xlsx')
df['Cost'] = df['Cost'].str.replace(r'\D', '').astype(int)
df = df.sort_values('Cost', ascending=True)
df = df.set_index('Description')
print(df.head())
filename = 'converted.xlsx'
df.to_excel(filename)
