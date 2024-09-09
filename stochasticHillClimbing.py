import random

# Função para calcular o número de conflitos (ataques entre rainhas)
def calcular_conflitos(tabuleiro):
		conflitos = 0
		n = len(tabuleiro)

		# Verifica conflitos em cada par de rainhas
		for i in range(n):
				for j in range(i + 1, n):
						# Mesma linha
						if tabuleiro[i] == tabuleiro[j]:
								conflitos += 1
						# Mesma diagonal
						if abs(tabuleiro[i] - tabuleiro[j]) == abs(i - j):
								conflitos += 1
		return conflitos

# Função que gera vizinhos aleatórios (mudança de uma rainha de posição)
def gerar_vizinho(tabuleiro):
		n = len(tabuleiro)
		novo_tabuleiro = tabuleiro[:]

		# Escolhe uma coluna aleatória
		coluna = random.randint(0, n - 1)

		# Escolhe uma linha diferente para a rainha nessa coluna
		nova_linha = random.randint(0, n - 1)

		# Garante que a rainha mude de linha
		while novo_tabuleiro[coluna] == nova_linha:
				nova_linha = random.randint(0, n - 1)

		novo_tabuleiro[coluna] = nova_linha
		return novo_tabuleiro

# Algoritmo Stochastic Hill Climbing
def stochastic_hill_climbing():
		# Inicializa com uma solução aleatória (array de 8 posições)
		tabuleiro = [random.randint(0, 7) for _ in range(8)]
		conflitos = calcular_conflitos(tabuleiro)

		# Limite de iterações para evitar laços infinitos
		iteracoes = 10000

		for i in range(iteracoes):
				# Se não há conflitos, encontramos a solução
				if conflitos == 0:
						break

				# Gera um vizinho aleatório
				vizinho = gerar_vizinho(tabuleiro)
				novos_conflitos = calcular_conflitos(vizinho)

				# Aceita o vizinho se ele melhorar ou mantiver a qualidade
				if novos_conflitos <= conflitos:
						tabuleiro = vizinho
						conflitos = novos_conflitos

		return tabuleiro, conflitos

# Executa o algoritmo
solucao, conflitos_finais = stochastic_hill_climbing()

# Exibe a solução encontrada
if conflitos_finais == 0:
		print("Solução encontrada:", solucao)
else:
		print("Solução parcial encontrada com", conflitos_finais, "conflitos:", solucao)

# Função para imprimir o tabuleiro visualmente
def imprimir_tabuleiro(solucao):
		for i in range(8):
				linha = ""
				for j in range(8):
						if solucao[j] == i:
								linha += "♛ "
						else:
								linha += ". "
				print(linha)

imprimir_tabuleiro(solucao)


