import pandas as pd

df = pd.read_excel("Dados Excel.xlsx")

# seleciona o indice
df.loc[0]
# seleciona o intervalo
df.loc[0:3]
# seleciona o intervalo e coluna
df.loc[4:6, ["FistName", "LastName"]]

# iloc, usa-se somente intervalos
df.iloc[2:6, 3:5]

df.head()