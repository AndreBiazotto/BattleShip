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
        
    def posicionar(self, barco: str, letra: str, numero: int, direcao: str):
        # Receber uma posição por vez.
        # Esperace uma coordenada, um tamanho e uma direção cardeal (N, S, L, O)

        if barco not in self.navios.keys():
            return "BARCO NÃO ENCONTRADO"
        
        if not self.navios[barco][0] == 0:
            return "POSIÇÃO OCUPADA"
        
        tam = len(self.navios[barco])
        if direcao == "N":
            for t in range(tam):
                if (numero - t) < 0:
                    return "FORA DOS LIMITES"
                
                if self.mar_navios[numero - t][self.letras.index(letra)] != "0":
                    return f"POSIÇÃO {numero - t}|{letra} OCUPADA"    
            
            self.navios[barco] = [f"{letra}{numero - t}" for t in range(tam)]

            for coordenada in self.navios[barco]:
                letra = coordenada[0]
                numero = int(coordenada[1])
                self.mar_navios[numero][self.letras.index(letra)] = "\033[93mN\033[00m"

            return "ALOCADO"
        
        if direcao == "S":
            for t in range(tam):
                if (numero + t) > 7:
                    return "FORA DOS LIMITES"
                
                if self.mar_navios[numero + t][self.letras.index(letra)] != "0":
                    return f"POSIÇÃO {numero + t}|{letra} OCUPADA"    
            
            self.navios[barco] = [f"{letra}{numero + t}" for t in range(tam)]

            for coordenada in self.navios[barco]:
                letra = coordenada[0]
                numero = int(coordenada[1])
                self.mar_navios[numero][self.letras.index(letra)] = "\033[93mN\033[00m"

            return "ALOCADO"
        
        if direcao == "O":
            for t in range(tam):
                if (self.letras.index(letra) - t) < 0:
                    return "FORA DOS LIMITES"
                
                if self.mar_navios[numero][self.letras.index(letra) - t] != "0":
                    return f"POSIÇÃO {numero - t}|{letra} OCUPADA"    
            
            self.navios[barco] = [f"{self.letras[self.letras.index(letra) - t]}{numero}" for t in range(tam)]

            for coordenada in self.navios[barco]:
                letra = coordenada[0]
                numero = int(coordenada[1])
                self.mar_navios[numero][self.letras.index(letra)] = "\033[93mN\033[00m"

            return "ALOCADO"
        
        if direcao == "O":
            for t in range(tam):
                if (self.letras.index(letra) + t) > 7:
                    return "FORA DOS LIMITES"
                
                if self.mar_navios[numero][self.letras.index(letra) + t] != "0":
                    return f"POSIÇÃO {numero + t}|{letra} OCUPADA"    
            
            self.navios[barco] = [f"{self.letras[self.letras.index(letra) + t]}{numero}" for t in range(tam)]

            for coordenada in self.navios[barco]:
                letra = coordenada[0]
                numero = int(coordenada[1])
                self.mar_navios[numero][self.letras.index(letra)] = "\033[93mN\033[00m"

            return "ALOCADO"
                

    def desenhar_mapa(self, mapa: list):
        desenho = ""
        for linhas in mapa:
            for colunas in linhas:
                desenho = desenho + str(colunas) + " "
            desenho = desenho + "\n"
        return desenho

jogo = set_jogo()
resultado = jogo.posicionar("Cruzador", "C", 3, "O")
print(resultado)
resultado = jogo.posicionar("Cruzador", "A", 3, "N")
print(resultado)
print(jogo.desenhar_mapa(jogo.mar_navios))
