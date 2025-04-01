#Criando classes sem atributos, apenas métodos
class jogo:
    def __init__(self):
        pass
    def iniciar(self):
        print("O jogo começou!")

class personagem:
    def __init__(self):
        self.nome = input("Digite o nome do personagem: ")
    def pular(self):
        print("O personagem pulou!")
    def dizer_nome(self):
        print(self.nome)
    

class Inimigo:
    def __init__(self):
        pass
    def atacar(self):
        print("O inimigo atacou!")



class pontuacao:
    def __init__(self):
        self.pontos = 0
    def zerar_pontos(self):
        print("Pontuação zerada!")
    def adicionar_pontos(self, quantidade):
        self.quantidade = 5
    def mostrar_pontos(self):
        self.pontos + self.quantidade


"""
Crie uma classe Pontuacao com um atributo pontos, inicializado
em 0, e dois métodos: adicionar_pontos(quantidade), que soma
quantidade ao total de pontos, e mostrar_pontos(), que imprime
a pontuação atual.
"""

class menu:
    def __init__(self):
        pass
    def iniciar_jogo(self):
        print("Escolha a dificuldade")
    def mostrar_opcoes(self):
        print("Aqui esta todas as configurações")
    def sair(self):
        print("Deseja mesmo sair desse jogo tão boom?")




teste = pontuacao()
teste.mostrar_pontos()



