#Criando classes sem atributos, apenas métodos
import random
class Jogo:
    def iniciar(self):
        print("O jogo começou!")

class JogoMultiplayer(Jogo):
    def __init__(self):
        super().__init__() 
        self.jogadores = []  

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
        print(f"Jogador {jogador.nome} adicionado ao jogo!")

    def listar_jogadores(self):
        print("Jogadores no jogo multiplayer:")
        for jogador in self.jogadores:
            print(f"- {jogador.nome}")


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

class MenuAvancado(Menu):
    def __init__(self, titulo):
        super().__init__(titulo)  
        self.configuracoes = {}   

    def salvar_configuracao(self, chave, valor):
        self.configuracoes[chave] = valor
        print(f"Configuração '{chave}' salva com valor: {valor}")

    def listar_configuracoes(self):
        if not self.configuracoes:
            print("Nenhuma configuração personalizada salva.")
        else:
            print("Configurações personalizadas salvas:")
            for chave, valor in self.configuracoes.items():
                print(f"- {chave}: {valor}")





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

    def vencer_desafio(self, pontos_ganhos):
        self.pontos += pontos_ganhos
        print(f"{self.nome} venceu um desafio! Pontuação: {self.pontos}")

class JogadorPremium(Jogador):
    def vencer_desafio(self, pontos_ganhos):
        bonus = 10  
        self.pontos += pontos_ganhos + bonus
        print(f"{self.nome} (Premium) venceu um desafio com bônus! Pontuação: {self.pontos}")


class NPC(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)  

    def atacar(self, alvo):
        print(f"{self.nome} é um NPC pacífico e não pode atacar.")


class Chefe(Inimigo):
    def __init__(self, nome, vida, forca):
        vida *= 2
        forca *= 2
        super().__init__(nome, vida, forca)


class Arma:
    def __init__(self, nome):
        self.nome = nome

    def atacar(self):
        print("Esta arma não tem um ataque definido.")

class Espada(Arma):
    def __init__(self, nome="Espada"):
        super().__init__(nome)

    def atacar(self):
        print(f"A {self.nome} desfere um golpe cortante corpo a corpo!")

class Arco(Arma):
    def __init__(self, nome="Arco"):
        super().__init__(nome)

    def atacar(self):
        print(f"O {self.nome} dispara uma flecha à distância!")

class Missao:
    def __init__(self, descricao):
        self.descricao = descricao

    def concluir(self):
        print("Missão concluída!")
        print("Recompensa: Nenhuma (missão genérica)")

class MissaoPrincipal(Missao):
    def __init__(self, descricao):
        super().__init__(descricao)

    def concluir(self):
        print(f"Missão Principal: {self.descricao} concluída!")
        print("Recompensa: 1000 moedas de ouro e item lendário!")

class MissaoSecundaria(Missao):
    def __init__(self, descricao):
        super().__init__(descricao)

    def concluir(self):
        print(f"Missão Secundária: {self.descricao} concluída!")
        print("Recompensa: 200 moedas de ouro e poção de cura.")
class Item:
    def __init__(self, nome):
        self.nome = nome

    def usar(self, alvo):
        print(f"O item {self.nome} foi usado, mas não tem efeito definido.")

class Pocao(Item):
    def __init__(self, nome="Poção de Cura", cura=50):
        super().__init__(nome)
        self.cura = cura

    def usar(self, alvo):
        alvo.recuperar_energia(self.cura)
        print(f"{alvo.nome} usou {self.nome} e recuperou {self.cura} de energia!")

class Equipamento(Item):
    def __init__(self, nome="Armadura de Ferro", defesa_bonus=10):
        super().__init__(nome)
        self.defesa_bonus = defesa_bonus

    def usar(self, alvo):
        print(f"{alvo.nome} equipou {self.nome} e agora possui +{self.defesa_bonus} de defesa (efeito simbólico).")
class Fase:
    def __init__(self, nome, dificuldade):
        self.nome = nome
        self.dificuldade = dificuldade

    def mostrar_caracteristicas(self):
        print(f"Fase: {self.nome}")
        print(f"Dificuldade: {self.dificuldade}")
        print("Características gerais da fase.")

class FaseFloresta(Fase):
    def __init__(self):
        super().__init__("Floresta", "Média")
        self.inimigos = ["Lobos", "Aranhas"]
        self.ambiente = "Árvores densas, rios e vegetação abundante"

    def mostrar_caracteristicas(self):
        super().mostrar_caracteristicas()
        print(f"Inimigos comuns: {', '.join(self.inimigos)}")
        print(f"Ambiente: {self.ambiente}")

class FaseDeserto(Fase):
    def __init__(self):
        super().__init__("Deserto", "Alta")
        self.inimigos = ["Escorpiões", "Bandidos do deserto"]
        self.ambiente = "Areia quente, dunas e tempestades de areia"

    def mostrar_caracteristicas(self):
        super().mostrar_caracteristicas()
        print(f"Inimigos comuns: {', '.join(self.inimigos)}")
        print(f"Ambiente: {self.ambiente}")

class Aliado:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def mostrar_status(self):
        print(f"{self.nome} | Vida: {self.vida}")

class Mago(Aliado):
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self.mana = mana

    def habilidade_especial(self):
        if self.mana >= 20:
            self.mana -= 20
            print(f"{self.nome} lançou uma bola de fogo! (Mana restante: {self.mana})")
        else:
            print(f"{self.nome} não tem mana suficiente para lançar a bola de fogo.")

class Guerreiro(Aliado):
    def __init__(self, nome, vida, energia):
        super().__init__(nome, vida)
        self.energia = energia

    def habilidade_especial(self):
        if self.energia >= 15:
            self.energia -= 15
            print(f"{self.nome} fez um ataque poderoso com a espada! (Energia restante: {self.energia})")
        else:
            print(f"{self.nome} não tem energia suficiente para o ataque poderoso.")
