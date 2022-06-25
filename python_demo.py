import numpy as np
import pandas as pd

df = {'A':[1,2,3],'B':[4,5,6]}
df = pd.DataFrame(df)
df1 = df.rename(columns={'A':'Somrudee'})
print(df)
print(df1)