#Criando classes sem atributos, apenas métodos
import random
class Jogo:
    def __init__(self):
        pass
    def iniciar(self):
        print("O jogo começou!")

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.__vida = 100

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} tomou {dano} de dano! Vida atual: {self.vida}")

    def atacar(self, alvo):
        dano = random.randint(5,20)
        print(f"{self.nome} atacou ferozmente!")
        alvo.tomar_dano(dano)  


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

"""
heroi = Personagem("MIguel")
vilao = Inimigo("Goblin")
"""

while heroi.vida > 0 and vilao.vida > 0:
    heroi.atacar(vilao)
    if vilao.vida <= 0:
        print(f"{vilao.nome} foi pra vala! {heroi.nome} venceu!")
        break

    vilao.atacar(heroi)
    if vilao.vida <= 0:
        print(f"{heroi.nome} foi pra vala! {vilao.nome} venceu!")
        break

class Pontuacao:
    def __init__(self):
        self.__pontos = 0
    def zerar_pontos(self):
        print("Pontuação zerada!")
    def adicionar_pontos(self, quantidade):
        self.pontos += quantidade
    def mostrar_pontos(self):
        print(self.pontos)


"""
Crie uma classe Pontuacao com um atributo pontos, inicializado
em 0, e dois métodos: adicionar_pontos(quantidade), que soma
quantidade ao total de pontos, e mostrar_pontos(), que imprime
a pontuação atual.
"""

class Menu:
    def __init__(self):
        pass
    def iniciar_jogo(self):
        print("Escolha a dificuldade")
    def mostrar_opcoes(self):
        print("Aqui esta todas as configurações")
    def sair(self):
        print("Deseja mesmo sair desse jogo tão boom?")



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





"""
teste = pontuacao()
teste.pontos = +5
teste.adicionar_pontos(43)
teste.mostrar_pontos()
"""


heroi = Personagem()
vilao = Inimigo("Goblin")

vilao.atacar(heroi)  # Goblin atacou! Vida restante: 90
vilao.atacar(heroi)  # Goblin atacou! Vida restante: 80

