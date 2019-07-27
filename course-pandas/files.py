import pandas as pd

# separador e header (especificar o cabelalho) 
df = pd.read_csv("Dados aula 1.csv", encoding="UTF-8", sep=";", header=0)

# abrir um excel
#df = pd.read_excel("Dados Excel.xlsx")

# selecionando algumas colunas
df = pd.read_csv("Dados aula 1.csv", encoding="UTF-8", sep=";", usecols=["AddressID", "AddressLine1"])

df[["AddressID", "AddressLine1"]].head()

# mostra o consultado
df.head()

# saber quantas linhas e colunas o csv obtem
#df.shape()
