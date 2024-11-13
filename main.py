# Importar las bibliotecas necesarias
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

# Datos predefinidos de las jugadas comunes en la apertura Ruy López
def obtener_datos_ruy_lopez():
    # Lista de secuencias de jugadas comunes en la Ruy López
    partidas = [
        ['e4', 'e5', 'Nf3', 'Nc6', 'Bb5', 'a6', 'Ba4', 'Nf6', 'O-O', 'Be7'],
        ['e4', 'e5', 'Nf3', 'Nc6', 'Bb5', 'Nf6', 'O-O', 'Nxe4'],
        ['e4', 'e5', 'Nf3', 'Nc6', 'Bb5', 'a6', 'Bxc6', 'dxc6', 'O-O', 'f6'],
        ['e4', 'e5', 'Nf3', 'Nc6', 'Bb5', 'f5'],
        ['e4', 'e5', 'Nf3', 'Nc6', 'Bb5', 'd6'],
        # Agrega más secuencias si lo deseas
    ]
    return partidas

# Función para construir la matriz de transición
def construir_matriz_transicion(partidas):
    transiciones = {}
    for partida in partidas:
        movimientos = partida
        for i in range(len(movimientos)-1):
            estado_actual = movimientos[i]
            estado_siguiente = movimientos[i+1]
            if estado_actual not in transiciones:
                transiciones[estado_actual] = {}
            if estado_siguiente not in transiciones[estado_actual]:
                transiciones[estado_actual][estado_siguiente] = 0
            transiciones[estado_actual][estado_siguiente] += 1
    return transiciones

# Función para calcular las probabilidades en la matriz de transición
def calcular_probabilidades(transiciones):
    matriz_probabilidades = {}
    for estado, transiciones_estado in transiciones.items():
        total = sum(transiciones_estado.values())
        matriz_probabilidades[estado] = {}
        for estado_siguiente, frecuencia in transiciones_estado.items():
            matriz_probabilidades[estado][estado_siguiente] = frecuencia / total
    return matriz_probabilidades

# Función para visualizar el grafo de transiciones
def visualizar_grafo(matriz_probabilidades):
    G = nx.DiGraph()
    for estado, transiciones_estado in matriz_probabilidades.items():
        for estado_siguiente, probabilidad in transiciones_estado.items():
            G.add_edge(estado, estado_siguiente, weight=probabilidad)
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, arrowstyle='->', arrowsize=20)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    edge_labels = {k: f"{v:.2f}" for k, v in edge_labels.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.title("Grafo de Transiciones de la Apertura Ruy López")
    plt.show()

# Función para visualizar el heatmap de la matriz de transición
def visualizar_heatmap(matriz_probabilidades):
    estados = list(matriz_probabilidades.keys())
    # Obtener todos los estados posibles
    estados_unicos = set(estados)
    for transiciones_estado in matriz_probabilidades.values():
        estados_unicos.update(transiciones_estado.keys())
    estados_unicos = sorted(estados_unicos)
    matriz = []
    for estado in estados_unicos:
        fila = []
        for estado_siguiente in estados_unicos:
            probabilidad = matriz_probabilidades.get(estado, {}).get(estado_siguiente, 0)
            fila.append(probabilidad)
        matriz.append(fila)
    df = pd.DataFrame(matriz, index=estados_unicos, columns=estados_unicos)
    plt.figure(figsize=(12, 10))
    sns.heatmap(df, annot=True, cmap='YlGnBu', fmt=".2f")
    plt.title("Heatmap de la Matriz de Transición")
    plt.xlabel("Estado Siguiente")
    plt.ylabel("Estado Actual")
    plt.show()

# Función principal para ejecutar el análisis
def main():
    # Obtener datos predefinidos de la apertura Ruy López
    partidas = obtener_datos_ruy_lopez()
    print(f"Total de partidas analizadas: {len(partidas)}")

    # Construir la matriz de transición
    transiciones = construir_matriz_transicion(partidas)
    print("Matriz de transición construida.")

    # Calcular las probabilidades
    matriz_probabilidades = calcular_probabilidades(transiciones)
    print("Matriz de probabilidades calculada.")

    # Visualizar el grafo de transiciones
    visualizar_grafo(matriz_probabilidades)

    # Visualizar el heatmap de la matriz de transición
    visualizar_heatmap(matriz_probabilidades)

if __name__ == "__main__":
    main()