import numpy as np
import matplotlib.pyplot as plt
import math

# Exercício 1: Translação Simples
# Dado o ponto ( P(2, 3) ), aplique a translação com vetor ( (4, -2) ).
# Perguntas: Qual é o novo ponto ( P' )? Quais coordenadas foram alteradas?
P1 = np.array([2, 3])
vetor_translacao1 = np.array([4, -2])
P1_transformado = P1 + vetor_translacao1
print("--- Exercício 1 ---")
print(f"O novo ponto P' é: {P1_transformado}")
# Resposta: O novo ponto P' é (6, 1). Ambas as coordenadas (x e y) foram alteradas.
plt.figure(figsize=(8, 8))
plt.title("Exercício 1: Translação Simples")
plt.scatter(P1[0], P1[1], color='blue', label='Original P(2, 3)', s=100)
plt.scatter(P1_transformado[0], P1_transformado[1], color='red', label=f"Transformado P'({P1_transformado[0]}, {P1_transformado[1]})", s=100)
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.axis('equal')
plt.legend()
plt.show()

# Exercício 2: Escala Uniforme
# Considere um triângulo com vértices ( A(1, 1), B(3, 1) ) e ( C(2, 4) ). Aplique uma escala uniforme de fator 2.
# Perguntas: Quais são as novas coordenadas dos vértices após a transformação? O que acontece com o tamanho do triângulo?
triangulo2 = np.array([[1, 1], [3, 1], [2, 4]])
fator_escala2 = 2
triangulo2_transformado = triangulo2 * fator_escala2
print("\n--- Exercício 2 ---")
print(f"As novas coordenadas dos vértices são:\n{triangulo2_transformado}")
# Resposta: As novas coordenadas são A'(2, 2), B'(6, 2) e C'(4, 8). O tamanho do triângulo duplica em todas as direções.
plt.figure(figsize=(8, 8))
plt.title("Exercício 2: Escala Uniforme")
plt.plot(*np.vstack([triangulo2, triangulo2[0]]).T, 'b-o', label='Original')
plt.plot(*np.vstack([triangulo2_transformado, triangulo2_transformado[0]]).T, 'r--o', label='Transformado')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.axis('equal')
plt.legend()
plt.show()

# Exercício 3: Escala Não Uniforme
# Aplique uma escala não uniforme no triângulo do Exercício 2, com fator de 2 no eixo (x) e fator de 0,5 no eixo (y).
# Pergunta: Quais são as novas coordenadas dos vértices?
triangulo3 = np.array([[1, 1], [3, 1], [2, 4]])
fator_escala3 = np.array([2, 0.5])
triangulo3_transformado = triangulo3 * fator_escala3
print("\n--- Exercício 3 ---")
print(f"As novas coordenadas dos vértices são:\n{triangulo3_transformado}")
# Resposta: As novas coordenadas são A'(2.0, 0.5), B'(6.0, 0.5), C'(4.0, 2.0).
plt.figure(figsize=(8, 8))
plt.title("Exercício 3: Escala Não Uniforme")
plt.plot(*np.vstack([triangulo3, triangulo3[0]]).T, 'b-o', label='Original')
plt.plot(*np.vstack([triangulo3_transformado, triangulo3_transformado[0]]).T, 'r--o', label='Transformado')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.axis('equal')
plt.legend()
plt.show()

# Exercício 4: Rotação em Torno da Origem
# Rotacione o ponto ( P(1, 0) ) em 90° no sentido anti-horário em torno da origem.
# Pergunta: Qual é a nova posição do ponto ( P' ) após a rotação?
P4 = np.array([1, 0])
angulo4_rad = math.radians(90)
matriz_rotacao4 = np.array([[math.cos(angulo4_rad), -math.sin(angulo4_rad)],
                          [math.sin(angulo4_rad), math.cos(angulo4_rad)]])
P4_transformado = np.round(matriz_rotacao4 @ P4).astype(int)
print("\n--- Exercício 4 ---")
print(f"A nova posição do ponto P' é: {P4_transformado}")
# Resposta: A nova posição do ponto P' é (0, 1).
plt.figure(figsize=(8, 8))
plt.title("Exercício 4: Rotação de 90° Anti-horário")
plt.scatter(P4[0], P4[1], color='blue', label='Original P(1, 0)', s=100)
plt.scatter(P4_transformado[0], P4_transformado[1], color='red', label=f"Transformado P'({P4_transformado[0]}, {P4_transformado[1]})", s=100)
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.axis('equal')
plt.legend()
plt.show()

# Exercício 5: Rotação de um Polígono
# Um quadrado tem vértices ( A(1, 1), B(1, 4), C(4, 4), D(4, 1) ). Aplique uma rotação de 45° no sentido horário.
# Pergunta: Quais são as novas coordenadas dos vértices?
quadrado5 = np.array([[1, 1], [1, 4], [4, 4], [4, 1]])
angulo5_rad = math.radians(-45)
matriz_rotacao5 = np.array([[math.cos(angulo5_rad), -math.sin(angulo5_rad)],
                          [math.sin(angulo5_rad), math.cos(angulo5_rad)]])
quadrado5_transformado = (matriz_rotacao5 @ quadrado5.T).T
print("\n--- Exercício 5 ---")
print(f"As novas coordenadas dos vértices são:\n{quadrado5_transformado}")
plt.figure(figsize=(8, 8))
plt.title("Exercício 5: Rotação de 45° Horário")
plt.plot(*np.vstack([quadrado5, quadrado5[0]]).T, 'b-o', label='Original')
plt.plot(*np.vstack([quadrado5_transformado, quadrado5_transformado[0]]).T, 'r--o', label='Transformado')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.axis('equal')
plt.legend()
plt.show()

# Exercício 6: Reflexão Simples
# Dado o ponto ( P(2, 5) ), aplique uma reflexão em relação ao eixo (y).
# Pergunta: Qual é a nova posição do ponto ( P' )?
P6 = np.array([2, 5])
P6_transformado = np.array([-P6[0], P6[1]])
print("\n--- Exercício 6 ---")
print(f"A nova posição do ponto P' é: {P6_transformado}")
# Resposta: A nova posição do ponto P' é (-2, 5).
plt.figure(figsize=(8, 8))
plt.title("Exercício 6: Reflexão em Relação ao Eixo Y")
plt.scatter(P6[0], P6[1], color='blue', label='Original P(2, 5)', s=100)
plt.scatter(P6_transformado[0], P6_transformado[1], color='red', label=f"Transformado P'({P6_transformado[0]}, {P6_transformado[1]})", s=100)
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.axis('equal')
plt.legend()
plt.show()

# Exercício 7: Reflexão de um Triângulo
# Considere um triângulo com vértices ( A(2, 3), B(4, 3) ) e ( C(3, 5) ). Aplique uma reflexão em relação ao eixo (x).
# Pergunta: Quais são as novas coordenadas dos vértices após a transformação?
triangulo7 = np.array([[2, 3], [4, 3], [3, 5]])
matriz_reflexao_x7 = np.array([[1, 0], [0, -1]])
triangulo7_transformado = triangulo7 @ matriz_reflexao_x7
print("\n--- Exercício 7 ---")
print(f"As novas coordenadas dos vértices são:\n{triangulo7_transformado}")
# Resposta: As novas coordenadas são A'(2, -3), B'(4, -3), C'(3, -5).
plt.figure(figsize=(8, 8))
plt.title("Exercício 7: Reflexão em Relação ao Eixo X")
plt.plot(*np.vstack([triangulo7, triangulo7[0]]).T, 'b-o', label='Original')
plt.plot(*np.vstack([triangulo7_transformado, triangulo7_transformado[0]]).T, 'r--o', label='Transformado')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.axis('equal')
plt.legend()
plt.show()

# Exercício 8: Cisalhamento Horizontal
# Dado o ponto ( P(2, 3) ), aplique um cisalhamento horizontal com ( k = 2 ).
# Pergunta: Qual é a nova posição do ponto ( P' )?
P8 = np.array([2, 3])
k8 = 2
P8_transformado = np.array([P8[0] + k8 * P8[1], P8[1]])
print("\n--- Exercício 8 ---")
print(f"A nova posição do ponto P' é: {P8_transformado}")
# Resposta: A nova posição do ponto P' é (8, 3).
plt.figure(figsize=(10, 8))
plt.title("Exercício 8: Cisalhamento Horizontal com k=2")
plt.scatter(P8[0], P8[1], color='blue', label='Original P(2, 3)', s=100)
plt.scatter(P8_transformado[0], P8_transformado[1], color='red', label=f"Transformado P'({P8_transformado[0]}, {P8_transformado[1]})", s=100)
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.axis('equal')
plt.legend()
plt.show()

# Exercício 9: Composição de Transformações
# Dado o ponto ( P(3, 2) ), aplique as seguintes transformações consecutivas:
# 1. Uma translação com vetor ( (1, -1) ).
# 2. Uma rotação de 90° no sentido anti-horário.
# 3. Uma escala uniforme com fator 2.
# Pergunta: Qual é a nova posição do ponto ( P' ) após todas as transformações?
P9 = np.array([3, 2])
P9_1 = P9 + np.array([1, -1])
angulo9_rad = math.radians(90)
matriz_rotacao9 = np.array([[math.cos(angulo9_rad), -math.sin(angulo9_rad)],
                           [math.sin(angulo9_rad), math.cos(angulo9_rad)]])
P9_2 = matriz_rotacao9 @ P9_1
P9_final = P9_2 * 2
P9_final = np.round(P9_final).astype(int)
print("\n--- Exercício 9 ---")
print(f"A posição final do ponto P' é: {P9_final}")
# Resposta: A nova posição do ponto P' é (-2, 8).
plt.figure(figsize=(8, 8))
plt.title("Exercício 9: Composição de Transformações")
plt.scatter(P9[0], P9[1], color='blue', label='P Original', s=100)
plt.scatter(P9_1[0], P9_1[1], color='green', label='Pós-translação', s=100)
plt.scatter(P9_2[0], P9_2[1], color='orange', label='Pós-rotação', s=100)
plt.scatter(P9_final[0], P9_final[1], color='red', label='Pós-escala (Final)', s=100)
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.axis('equal')
plt.legend()
plt.show()

# Exercício 10: Combinação de Transformações em uma Figura
# Dado um retângulo com vértices ( A(1, 1), B(5, 1), C(5, 3), D(1, 3) ), aplique as seguintes transformações em sequência:
# 1. Translação com vetor ( (-2, 3) ).
# 2. Escala não uniforme com fatores ( 1.5 ) no eixo (x) e (0.5) no eixo (y).
# 3. Reflexão em relação ao eixo (y).
# Pergunta: Quais são as novas coordenadas dos vértices após as três transformações?
retangulo10 = np.array([[1, 1], [5, 1], [5, 3], [1, 3]])
retangulo10_1 = retangulo10 + np.array([-2, 3])
retangulo10_2 = retangulo10_1 * np.array([1.5, 0.5])
matriz_reflexao_y10 = np.array([[-1, 0], [0, 1]])
retangulo10_final = retangulo10_2 @ matriz_reflexao_y10
print("\n--- Exercício 10 ---")
print(f"As novas coordenadas dos vértices são:\n{retangulo10_final}")
plt.figure(figsize=(10, 8))
plt.title("Exercício 10: Combinação de Transformações")
plt.plot(*np.vstack([retangulo10, retangulo10[0]]).T, 'b-o', label='Original')
plt.plot(*np.vstack([retangulo10_1, retangulo10_1[0]]).T, 'g-o', label='Pós-translação', alpha=0.5)
plt.plot(*np.vstack([retangulo10_2, retangulo10_2[0]]).T, 'y-o', label='Pós-escala', alpha=0.5)
plt.plot(*np.vstack([retangulo10_final, retangulo10_final[0]]).T, 'r--o', label='Final')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.axis('equal')
plt.legend()
plt.show()