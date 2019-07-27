import matplotlib.pyplot as plt

x = [1, 2, 5, 4, 7]
y = [2, 3, 7, 1, 0]

title = "Grafico Barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(title)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x,y)
plt.show()
