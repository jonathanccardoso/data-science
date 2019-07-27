import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]

title = "Scatterplot: grafico de dispersao"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(title)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x, y, color="k", linestyle="--") # ligacao de linhas
plt.scatter(x, y, label="Meus pontos", color="k", marker=".", s=200)
plt.legend()

plt.show()

# save grafic
# best resolution
# plt.savefig("figura1.png", dpi=300)
plt.savefig("figura1.pdf")
