#Criando classes sem atributos, apenas métodos
class Jogo:
    def __init__(self):
        pass
    def iniciar(self):
        print("O jogo começou!")

class Personagem:
    def __init__(self):
        self.nome = input("Digite o nome do personagem: ")
        self.vida = 100
    def tomar_dano(self,dano):
        self.vida -= dano
        if self.vida <= 0:
            print("Game over")
        else:
            print(self.vida) 

    def pular(self):
        print("O personagem pulou!")
    def dizer_nome(self):
        print(self.nome)

"""
Crie uma classe Personagem com um atributo vida, inicializado
em 100. Adicione um método tomar_dano(dano), que reduz a
vida do personagem pelo valor passado como parâmetro. Se a
vida chegar a 0, imprima "Game Over!".
"""
    

class Inimigo:
    def __init__(self):
        self.nome = "Sem nome"

    def atacar(self, alvo):
        print("O inimigo atacou!")

"""
Crie uma classe Inimigo com atributos nome e vida (inicializada
com 100). Adicione um método atacar(alvo), onde alvo é um
objeto da classe Personagem. Esse método deve reduzir a vida
do alvo em 10 pontos.'
"""



class Pontuacao:
    def __init__(self):
        self.pontos = 0
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
        if self.energia < 100:
            self.energia += quantidade
            print(f"Você recuperou {quantidade} de energia!")
        else:
            print("Sua energia esta cheia.")

    def usar_energia(self, quantidade):
        if self.energia > 0:
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




"""
teste = pontuacao()
teste.pontos = +5
teste.adicionar_pontos(43)
teste.mostrar_pontos()
"""






