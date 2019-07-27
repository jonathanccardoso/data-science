# Diagrama de caixa

import matplotlib.pyplot as plt
import random

vetor = []

for i in range(10):
	number_random = ramdom.randint(0,5)
	vetor.append(number_random)

plt.bloxplot(vetor)
plt.show()


