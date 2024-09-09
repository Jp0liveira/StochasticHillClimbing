import random
import time
import numpy as np
import  stochasticHillClimbing as shc

# Algoritmo Stochastic Hill Climbing Test
def stochastic_hill_climbing(max_iter=500):
		# Inicializa com uma solução aleatória (array de 8 posições)
		tabuleiro = [random.randint(0, 7) for _ in range(8)]
		conflitos = shc.calcular_conflitos(tabuleiro)

		# Limite de iterações sem melhoria
		iteracoes = 10000
		sem_melhoria = 0

		for i in range(iteracoes):
				# Se não há conflitos, encontramos a solução
				if conflitos == 0 or sem_melhoria >= max_iter:
						return i, conflitos

				# Gera um vizinho aleatório
				vizinho = shc.gerar_vizinho(tabuleiro)
				novos_conflitos = shc.calcular_conflitos(vizinho)

				# Aceita o vizinho se ele melhorar ou mantiver a qualidade
				if novos_conflitos <= conflitos:
						tabuleiro = vizinho
						conflitos = novos_conflitos
						sem_melhoria = 0  # Reinicia contador de iterações sem melhorias
				else:
						sem_melhoria += 1
		return iteracoes, conflitos  # No caso de não encontrar solução

# Executar 50 vezes
iteracoes_totais = []
tempos_execucao = []

for _ in range(50):
		# Medir o tempo de execução
		inicio = time.time()

		# Executa o algoritmo
		iteracoes, conflitos_finais = stochastic_hill_climbing()

		fim = time.time()
		tempo_execucao = fim - inicio

		# Armazenar o número de iterações e o tempo
		iteracoes_totais.append(iteracoes)
		tempos_execucao.append(tempo_execucao)

# Calcular média e desvio padrão
media_iteracoes = np.mean(iteracoes_totais)
desvio_padrao_iteracoes = np.std(iteracoes_totais)

media_tempo = np.mean(tempos_execucao)
desvio_padrao_tempo = np.std(tempos_execucao)

# Exibir resultados
print(f"Média de iterações: {media_iteracoes}")
print(f"Desvio padrão de iterações: {desvio_padrao_iteracoes}")
print(f"Média de tempo de execução: {media_tempo:.6f} segundos")
print(f"Desvio padrão do tempo de execução: {desvio_padrao_tempo:.6f} segundos")

