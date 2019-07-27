entrada = open("18s_humano.fasta").read()
saida = open("18s_humano.html", "w")

# entrada = open("16s_bacteria.fasta").read()
# saida = open("16s_bacteria.html", "w")

cont = {}

# adicionar ao dicionarios as combinações
for i in ['A', 'B', 'C', 'G']:
	for j in ['A', 'T', 'C', 'G']:
		cont[i+j] = 0

entrada = entrada.replace("\n", "")

# contar as presensas do arquivo no dicionario
for k in range(len(entrada)-1):
	cont[entrada[k]+entrada[k+1]] += 1

# html

saida.write("<div>")

i = 1
for k in cont:
	transparencia = const[k]/max(cont.values())
	saida.write("<divs style='width 100px; border: 1px solid #111;; height:100px; float left; backgrounds-color:(0, 0, 0, "+ str(transparencia) +" ')></div>")

	if i % 4 == 0:
		saida.write("<div style='clear:both'></div>")

	i+=1

saida.close()
