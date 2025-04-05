class Personagem:
    def __init__(self):
        self.vida = 100

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print("Game Over!")
        else:
            print(f"Vida restante: {self.vida}")


class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def atacar(self, alvo):
        print(f"{self.nome} atacou ferozmente!")
        alvo.tomar_dano(10)

heroi = Personagem()
vilao = Inimigo("Goblin")

vilao.atacar(heroi)  # Goblin atacou! Vida restante: 90
vilao.atacar(heroi)  # Goblin atacou! Vida restante: 80
