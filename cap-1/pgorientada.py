#Criando classes sem atributos, apenas métodos
import random
class Jogo:
    def __init__(self):
        pass
    def iniciar(self):
        print("O jogo começou!")

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida  

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} tomou {dano} de dano! Vida atual: {self.vida}")

    def atacar(self, alvo):
        dano = random.randint(5, 20)
        print(f"{self.nome} atacou ferozmente!")
        alvo.tomar_dano(dano)



class Inimigo:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida  
        self.forca = forca  

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} tomou {dano} de dano! Vida restante: {self.vida}")

    def atacar(self, alvo):
        dano = random.randint(5, 20) + self.forca  
        print(f"{self.nome} atacou ferozmente!")
        alvo.tomar_dano(dano)




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


class Menu:
    def __init__(self, titulo):
        self.titulo = titulo  

    def iniciar_jogo(self):
        print(f"=== {self.titulo} ===")
        print("Escolha a dificuldade")

    def mostrar_opcoes(self):
        print("Aqui estão todas as configurações")

    def sair(self):
        print("Deseja mesmo sair desse jogo tão bom?")




class Jogador:
    def __init__(self, nome, energia, pontos):
        self.nome = nome
        self.energia = energia 
        self.pontos = pontos   

    def recuperar_energia(self, quantidade):
        self.energia += quantidade
        print(f"Energia recuperada. Você está com {self.energia} de energia.")

    def usar_energia(self, quantidade):
        if self.energia - quantidade < 0:
            print("Sem energia")
        else:
            self.energia -= quantidade
            print(f"Foi um ótimo golpe. No entanto, resta {self.energia} de energia.")





