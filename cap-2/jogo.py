import random

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.__vida = 100
        self.__defesa = 50  

    @property
    def vida(self):
        return self.__vida

    @property
    def defesa(self):
        return self.__defesa

    @defesa.setter
    def defesa(self, valor):
        if 0 <= valor <= 100:
            self.__defesa = valor
        else:
            print("Erro: Defesa deve estar entre 0 e 100.")


class Pontuacao:
    def __init__(self):
        self.__pontos = 0 

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, valor):
        if valor >= 0:
            self.__pontos = valor
        else:
            print("Erro: pontos não podem ser negativos!")



class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.__forca = random.randint(5, 20)

    def mostrar_forca(self):
        return self.__forca

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
        print(f"{self.nome} tomou {dano} de dano! Vida restante: {self.vida}")

    def atacar(self, alvo):
        print(f"{self.nome} atacou com força {self.__forca}!")
        alvo.tomar_dano(self.__forca)

class Jogador:
    def __init__(self):
        self.__energia = 100  

    def recuperar_energia(self, quantidade):
        if quantidade > 0:
            self.__energia += quantidade
            if self.__energia > 100:
                self.__energia = 100
            print(f"Energia recuperada. Você está com {self.__energia} de energia.")
        else:
            print("Quantidade inválida para recuperação.")

    def usar_energia(self, quantidade):
        if quantidade > 0:
            if self.__energia - quantidade < 0:
                self.__energia = 0
                print("Sem energia suficiente para o golpe.")
            else:
                self.__energia -= quantidade
                print(f"Foi um ótimo golpe. No entanto, resta {self.__energia} de energia.")
        else:
            print("Quantidade inválida para uso.")

    def mostrar_energia(self):
        return self.__energia  

class Jogo:
    def __init__(self):
        self.__dificuldade = 1 

    @property
    def dificuldade(self):
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, valor):
        if valor in [1, 2, 3]:
            self.__dificuldade = valor
        else:
            print("Erro: Dificuldade deve ser 1, 2 ou 3.")
