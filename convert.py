# import numpy as np
import pandas as pd

df = pd.read_csv('motorola.txt', header=None, delimiter='?')
df.columns = ['Description', 'Cost']

df.to_excel('converted.xlsx', index=None)
