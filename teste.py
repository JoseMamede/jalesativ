import random

class Jogador:
    def __init__(self):
        self.energia = 100

    def recuperar_energia(self, quantidade):
            self.energia += quantidade
            print(f"Energia recuperada. Você esta com {self.energia} de energia.")

    def usar_energia(self, quantidade):
        if self.energia - quantidade < 0:
            print("Sem energia")
        else:
            self.energia -= quantidade
            print(f"Foi um otimo golpe. No entanto, resta {self.energia} de energia.")

class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} tomou {dano} de dano! Vida restante: {self.vida}")

    def atacar(self, alvo):
        dano = random.randint(5,20)
        print(f"{self.nome} atacou ferozmente!")
        alvo.tomar_dano(dano)

class Pontuacao:
    def __init__(self):
        self.pontos = 0
    def zerar_pontos(self):
        print("Pontuação zerada!")
    def adicionar_pontos(self, quantidade):
        self.pontos += quantidade
    def mostrar_pontos(self):
        print(self.pontos)