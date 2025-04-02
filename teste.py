class Jogador:
    def __init__(self):
        self.energia = 100

    def recuperar_energia(self, quantidade):
        if self.energia < 100:
            self.energia += quantidade
            print(f"Você recuperou {quantidade} de energia!")
        else:
            print("Sua energia esta cheia.")

    def usar_energia(self, quantidade):
        if self.energia >= 0:
            self.energia -= quantidade
            print(f"Você gastou {quantidade} de energia")
        elif self.energia <= 0:
            print("Sem energia suficiente!")




"""
Crie uma classe Jogador com um atributo energia, inicializado
em 50. Adicione métodos recuperar_energia(quantidade) e
usar_energia(quantidade). Se a energia for menor que 0,
imprima "Sem energia suficiente!".
"""

teste = Jogador()
teste.recuperar_energia(20)
