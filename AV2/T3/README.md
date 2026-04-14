## Trabalho Pratico 3 - Problema do Carteiro Chines

Implementacao em Python para encontrar um circuito euleriano em um digrafo ponderado ja eulerizado.

## Estrutura

- dados/entrada_original.txt: grafo original de exemplo
- dados/entrada_eulerizada.txt: grafo eulerizado usado na execucao
- src/main.py: ponto de entrada do projeto
- src/digraph.py: representacao do digrafo ponderado
- src/hierholzer.py: implementacao do metodo de Hierholzer

## Como executar

1. Abra o terminal na pasta AV2/T3
2. Rode:

	python -m src.main

## O que o programa mostra

- Lista de adjacencia do grafo
- Graus de entrada e saida de cada vertice
- Verificacao de balanceamento dos vertices
- Circuito euleriano encontrado
- Custo total do circuito

## Observacao

O arquivo entrada_eulerizada.txt deve estar balanceado para que o circuito euleriano exista.

## Video Explicativo

link vídeo -> https://youtu.be/zYqNQ8R_Nsc