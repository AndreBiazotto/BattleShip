"""
Batalha Naval (Battleship)

O jogo consiste em dois jogadores, com os mesmo conjuntos de navios, espaços e ataques.

O set padrão consite em duas matrizes, uma onde tem os navios de cada jogador, e outra onde
marca os ataques aos adversários. Se um ataque cai na água ele é marcado de branco e se atinge
um navio é marcado de vermelho.

Navios
Porta-aviões (5 quadrados)
Couraçado (4 quadrados)
Cruzador (3 quadrados)
Submarino (3 quadrados)
Destroyer (2 quadrados)
"""

class set_jogo():
    def __init__(self):
        self.letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        self.mar_ataque = [["0" for _colunas in range(10)] for _linhas in range(8)]
        self.mar_navios = [["0" for _colunas in range(10)] for _linhas in range(8)]

        # <A><Letra><Número>
        # A só quando o návio foi atacado
        self.navios = {
            "Porta-aviões": [0, 0, 0, 0, 0], 
            "Couraçado": [0, 0, 0, 0], 
            "Cruzador": [0, 0, 0], 
            "Submarino": [0, 0, 0], 
            "Destroyer": [0, 0]
        }

        self.cont_abates = {"Porta-aviões": 0, "Couraçado": 0, "Cruzador": 0, "Submarino": 0, "Destroyer": 0}
        
    def posicionar(self):
        # Fazer esse metodo receber uma lista com as posiçoes e direçoes ou receber uma por vez
        pass
                

    def desenhar_mapa(self, mapa: list):
        desenho = ""
        for linhas in mapa:
            for colunas in linhas:
                desenho = desenho + str(colunas) + " "
            desenho = desenho + "\n"
        return desenho

jogo = set_jogo()
jogo.posicionar()