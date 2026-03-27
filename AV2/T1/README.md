## Trabalho Pratico 1 - Grafos (DFS e BFS)

Este projeto implementa um grafo com os estados do Nordeste e executa DFS e BFS para responder os requisitos do T1.

## Pre-requisitos

- Python 3.10 ou superior instalado
- Terminal aberto na pasta AV2/T1

## Estrutura usada na execucao

- O mapeamento dos estados esta em dados/dicionario.py
- As arestas (fronteiras terrestres) estao em dados/mapa nordeste.txt
- O ponto de entrada e src/main.py

## Como rodar

1. Entre na pasta do trabalho:

	cd AV2/T1

2. Execute o programa:

	python -m src.main

3. Informe no terminal:

- Estado de origem (exemplo: AL)
- Estado de destino (exemplo: CE)

## O que o programa mostra

- Se a origem alcanca o destino por fronteiras terrestres
- Caminho encontrado por DFS
- Caminho encontrado por BFS
- Estados alcancaveis a partir da origem
- Ordem de visita da DFS
- Ordem de visita da BFS

## Exemplo rapido

Com origem AL e destino CE, o programa imprime todos os itens acima, incluindo os caminhos e as ordens de visita.
