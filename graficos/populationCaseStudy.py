# Crescimento da população Brasileira
# DataSus

import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

# percorre os valores do arquivo
for i in range(len(data)):
	if i != 0:
		line = data[i].split(";")
		x.append(int(line[0]))
		y.append(int(line[1]))

plt.bar(x, y, color="#e4e4e4")
plt.plot(x, y, color='k', linestyle="--")

plt.title("Crescimento da População Brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("Populacao")

plt.show()
# plt.savefig("populacao_brasileira.png", dpi=300)
