import pandas as pd

df = pd.read_excel("Dados Excel.xlsx")

# returna todos os valores
df.sort_values("FistName")
df.sort_values(by = ["FistName", "LastNames"]).head()

# filter
df.filter(itens = ["FistName", "LastNames"]).head()

# 5 primeiros
df.head()