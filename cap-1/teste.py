import random

class Jogador:
    def __init__(self):
        self.energia = 100
        self.pontos = 0

    def recuperar_energia(self, quantidade):
            self.energia += quantidade
            if self.energia > 100:
                self.energia = 100
            print(f"Energia recuperada. Você esta com {self.energia} de energia.")

    def usar_energia(self, quantidade):
        if self.energia - quantidade < 0:
            print("Sem energia, você precisa descansar, AGORA!")
        else:
            self.energia -= quantidade
            print(f"Foi um otimo golpe. No entanto, resta {self.energia} de energia.")

    def atacar(self, inimigo):
        if self.energia <= 10:
            print("Você chegou ao seu limite, use descansar () para se recuperar.")
            return
        
        self.energia -= 10
        print(f"Você atacou! Energia restante: {self.energia}")
        dano = random.randint(15,30)
        inimigo.tomar_dano(dano)

        if inimigo.vida == 0:
            self.pontos += 10
            print(f"Inimigo derrotado com sucesso! Pontuaçâo atual: {self.pontos}")


    def descansar(self):
        recuperacao = 20
        self.energia += recuperacao
        if self.energia > 100:
            self.energia = 100
        print(f"Você repousou em uma fogueira e repoz sua energia. Energia atual: {self.energia}")
         

class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} tomou {dano} de dano. Vida restante: {self.vida}")

class Pontuacao:
    def __init__(self):
        self.pontos = 0
    def zerar_pontos(self):
        self.pontos = 0
        print("Pontuação zerada!")
    def adicionar_pontos(self, quantidade):
        self.pontos += quantidade
    def mostrar_pontos(self):
        print(self.pontos)

pontos = Pontuacao()
jogador = Jogador()
inimigo = Inimigo("Goblin")

while inimigo.vida > 0:
    jogador.atacar(inimigo)
    if inimigo.vida == 0:
        pontos.adicionar_pontos(10)

    if jogador.energia <= 10 and inimigo.vida > 0:
        jogador.descansar()

pontos.mostrar_pontos()
