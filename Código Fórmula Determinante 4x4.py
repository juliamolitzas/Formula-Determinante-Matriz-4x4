#Declarando as Matrizes
matriz1 = [
        [1, 2, 3, 4], [2, 4, 6, 8],
        [3, 6, 9, 12], [4, 8, 12, 16]
      ]

matriz2 = [
        [1, 0, 0, 0], [0, 1, 0, 0],
        [0, 0, 1, 0], [0, 0, 0, 1]
     ]

#Lei Leibniz
def determinante_leibniz(matriz):

    calc = 0
    determinante = 0

    for i in range(0, 4):
        for j in range(0, 6):
            if i == 0:
                if j == 0:
                    calc = matriz[0][0] * matriz[1][1] * matriz[2][2] * matriz[3][3]

                elif j == 1:
                    calc = (matriz[0][0] * matriz[1][1] * matriz[2][3] * matriz[3][2]) * -1

                elif j == 2:
                    calc = (matriz[0][0] * matriz[1][2] * matriz[2][1] * matriz[3][3]) * -1

                elif j == 3:
                    calc = matriz[0][0] * matriz[1][2] * matriz[2][3] * matriz[3][1]

                elif j == 4:
                    calc = matriz[0][0] * matriz[1][3] * matriz[2][1] * matriz[3][2]

                elif j == 5:
                    calc = (matriz[0][0] * matriz[1][3] * matriz[2][2] * matriz[3][1]) * -1

            if i == 1:
                if j == 0:
                    calc = (matriz[0][1] * matriz[1][0] * matriz[2][2] * matriz[3][3]) * -1

                elif j == 1:
                    calc = matriz[0][1] * matriz[1][0] * matriz[2][3] * matriz[3][2]

                elif j == 2:
                    calc = matriz[0][1] * matriz[1][2] * matriz[2][0] * matriz[3][3]

                elif j == 3:
                    calc = (matriz[0][1] * matriz[1][2] * matriz[2][3] * matriz[3][0]) * -1

                elif j == 4:
                    calc = (matriz[0][1] * matriz[1][3] * matriz[2][0] * matriz[3][2]) * -1

                elif j == 5:
                    calc = matriz[0][1] * matriz[1][3] * matriz[2][2] * matriz[3][0]

            if i == 2:
                if j == 0:
                    calc = matriz[0][2] * matriz[1][0] * matriz[2][1] * matriz[3][3]

                elif j == 1:
                    calc = (matriz[0][2] * matriz[1][0] * matriz[2][3] * matriz[3][1]) * -1

                elif j == 2:
                    calc = (matriz[0][2] * matriz[1][1] * matriz[2][0] * matriz[3][3]) * -1

                elif j == 3:
                    calc = matriz[0][2] * matriz[1][1] * matriz[2][3] * matriz[3][0]

                elif j == 4:
                    calc = matriz[0][2] * matriz[1][3] * matriz[2][0] * matriz[3][1]

                elif j == 5:
                    calc = (matriz[0][2] * matriz[1][3] * matriz[2][1] * matriz[3][0]) * -1

            if i == 3:
                if j == 0:
                    calc = (matriz[0][3] * matriz[1][0] * matriz[2][1] * matriz[3][2]) * -1

                elif j == 1:
                    calc = matriz[0][3] * matriz[1][0] * matriz[2][2] * matriz[3][1]

                elif j == 2:
                    calc = matriz[0][3] * matriz[1][1] * matriz[2][0] * matriz[3][2]

                elif j == 3:
                    calc = (matriz[0][3] * matriz[1][1] * matriz[2][2] * matriz[3][0]) * -1

                elif j == 4:
                    calc = (matriz[0][3] * matriz[1][2] * matriz[2][0] * matriz[3][1]) * -1

                elif j == 5:
                    calc = matriz[0][3] * matriz[1][2] * matriz[2][1] * matriz[3][0]

            determinante += calc
            calc = 0

    return determinante

#Chamando Função
determinante1 = determinante_leibniz(matriz1)
determinante2 = determinante_leibniz(matriz2)

#Resultados no Console
print("\nO resultado do determinate da primeira matriz é:", determinante1)
print("O resultado do determinante da segunda matriz é:", determinante2)
