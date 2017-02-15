# coding=utf-

# Trabalho de Inteligência Artificial
# Grupo: Rafael Batista Andrade, Thiago Hocsis

# Algoritmo Genético

# Encontrar de x para o qual a função f(x) = x² - 3x + 4 assume o valor máximo .# 
# f(x) = 2X+ X*X - 5X + 4 
# -Assumir que x [-10, +10]# 
# -Codificar X como vetor binário# 
# -Criar uma população inicial com 10 indivíduos# 
# -Aplicar Mutação com taxa de 1%# 
# -Aplicar Crossover com taxa de 70%# 
# -Usar seleção por torneio.# 
# -Usar 200 gerações.# 





import random
import sys



# Para ficar mais facil a manipulacao de bits usamos esse array chamado dominio
# o index representa a posicao dentro do vetor
# Index - 10 representa o valor da posicao.

# index = 0
# valor representa e (0 - 10) == -10, logo posicao 0 representa o valor

#Dominio[0] = -10
#Dominio[20] = 10

dominio = [
"11010" 
,"10111" 
,"11000"
,"11001"
,"11010"
,"11011"
,"11100"
,"11101"
,"11110"
,"11111"
,"00000"
,"00001"
,"00010"
,"00011"
,"00100"
,"00101"
,"00110"
,"00111"
,"01000"
,"01001"
,"01010"
]


# Representa a funcao f(x)
def f(x) :
	return (x**2 - 3*x + 4)

# Seleciona qual dos 2 valores tem maior valor de f(x)
def torneio(ind1,ind2):
	if (f(ind1-10) > f(ind2-10)):
		return ind1
	else:
		return ind2

# Procura elemento no array, se for encontrado retorn o index, caso contrario retorna -1
def procura(el, array):
	if (el in array):
		return array.index(el)
	else:
		return -1

# Insere o elemento no array se e somente se ele fizer parte do dominio
# Por exemplo, caso o cromossomo gerado pela mutação não faça parte do dominio ele não sera inserido
# Retorna 1 se for inserido, 0 caso contrário
def insere(el, populacao, dominio):
	if (procura(el, dominio) >= 0):
		populacao.append(procura(el,dominio))
		return 1
	else:
		return 0

	
# Determina se irá ter crossover ou não
# 70% de chances de haver crossover
def crossover():
	cross = random.randint(1,100)
	if (cross > 30):
		return True
	else:
		return False

# Seleciona os 10 melhores da população concatenado com nova populacao
def seleciona(populacao,nova_populacao):
	populacao2 = populacao + nova_populacao
	print populacao2
	selected_populacao = []
	maior = 0
	for i in range(10):
		maior = 0
		for j in range(19):
			if (f(populacao2[j-i] - 10) > f(populacao2[j-i+1] - 10)):
				maiorAux = j-i
				if (f(populacao2[maiorAux]-10) > f(populacao2[maior]-10)):
					maior = maiorAux
			else:
				maiorAux = j-i+1
				if(f(populacao2[maiorAux]-10) > f(populacao2[maior]-10)):
					maior = maiorAux
	
		selected_populacao.append(populacao2[maior])
		populacao2.pop(maior)

	return selected_populacao




# Aplica o crossover
def apply_crossover(populacao, dominio):
	nova_populacao = []
	for i in range(len(populacao)-1):
		if (i%2 == 0):
			if (crossover()):
				# Gera um valor que será feita o corte
				calda = random.randint(1,3)
				#Child1  mantém a primeira parte e concatena com a calda do segundo, se houver crossover
				child1 = dominio[populacao[i]][:calda] + dominio[populacao[i+1]][calda:]
				#Child2  mantém a primeira parte e concatena com a calda do primeiro, se houver crossover
				child2 = dominio[populacao[i+1]][:calda] + dominio[populacao[i]][calda:]

				#Caso o resultado gerado não esteja no dominio, o cromossomo inserido na nova populacao será o pai
				if (insere(child1,nova_populacao,dominio) == 0):
					nova_populacao.append(populacao[i])
				if(insere(child2,nova_populacao,dominio) == 0):
					nova_populacao.append(populacao[i+1])
			else : 
				nova_populacao.append(populacao[i])
				nova_populacao.append(populacao[i+1])
	
	return nova_populacao


# Define como será feita a mutação
def mutacao(populacao,dominio):
	nova_populacao = []
	child = ""
	# Para cada individuo da populacao ele verifica se haverá mutação
	# Se sim ele trocará o bit que houve a mutação
	for i in range(10):
		for j in range(5):
			mut = random.randint(1,100)
			if (mut == 1):

				#Se mutação correr e o bit for 1 troca por 0, se for 0 troca por 1
				if (dominio[i][j] == '1'):
					child = dominio[i][:j] + '0' +dominio[i][j+1:]
				else:
					child = dominio[i][:j] + '1' +dominio[i][j+1:]

		# Caso a mutação não exista no dominio ele irá inserir o pai na nova população
		if(insere(child,nova_populacao,dominio) == 0):
			nova_populacao.append(populacao[i])

	return nova_populacao


def executa(populacao, dominio):
	nova_populacao = []
	for i in range(10):
			#Seleciono 2 individuos aleatorio da populacao
			ind1 = random.randint(0,9)
			ind2 = random.randint(0,9)
			
			#Escolhe um dos 2 por torneio
			ind_selecionado = torneio(populacao[ind1],populacao[ind2])
			
			#Adiciono na nova_população
			nova_populacao.append(ind_selecionado)

	# Aplica o crossover na população gerada
	nova_populacao = apply_crossover(nova_populacao,dominio)
	# Aplica a mutação na população gerada e retorna a nova população
	nova_populacao = mutacao(nova_populacao,dominio)
	return nova_populacao


# Funcao que imprime na tela os resultados
def imprime (populacao, dominio):
	print "IND \t CROMOSSOMOS\t X\t F(X)"
	#print populacao
	for i in range(10):
		print str(i) + " \t "+ dominio[populacao[i]] + " \t \t " + str(populacao[i] - 10) + "\t " + str(f(populacao[i]-10))
	
	print ""
	print ""






# É criada uma população
populacao = []
nova_populacao = []
# São gerados 10 individuos aleatorios do dominio
for i in range(10):
	# Random de 0 a 20 pois esses são os indexes do dominio
	# São 21 termos
	x = random.randint(0,20)

	#Insiro na população
	populacao.append(x)

#Imprime primeira populaçãp

imprime(populacao,dominio)
for i in range(200):
	print "Geração: " , i+1
	nova_populacao = executa(populacao,dominio)
	populacao = seleciona(populacao,nova_populacao)
	imprime (populacao,dominio)









