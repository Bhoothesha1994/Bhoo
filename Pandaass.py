
import pandas as pd
data=pd.read_excel('C:/Users/Windows10/Desktop/Book1.xlsx')
df=pd.DataFrame(data)
print(df)
a=list(df['Vehicle No'])
print(a)
b=input('enter vehicle no')
c=a.index(b)
print(df.loc[c])

