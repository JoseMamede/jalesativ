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

    def iniciar(self):
        print("O jogo multiplayer começou! Aguardando todos os jogadores se conectarem...")

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

    def falar(self):  # Questão 36
        print(f"{self.nome} diz: Estou pronto para a batalha!")

class NPC(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def atacar(self, alvo):
        print(f"{self.nome} é um NPC pacífico e não pode atacar.")

    def falar(self):
        print(f"{self.nome} diz: Bem-vindo à aldeia, viajante. Posso te ajudar?")

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

class Chefe(Inimigo):
    def __init__(self, nome, vida, forca):
        vida *= 2
        forca *= 2
        super().__init__(nome, vida, forca)

    def atacar(self, alvo):
        dano = random.randint(10, 30) + self.forca + 10
        print(f"{self.nome} usa um golpe especial devastador!")
        alvo.tomar_dano(dano)

class Pontuacao:
    def __init__(self):
        self.__pontos = 0

    def zerar_pontos(self):
        self.__pontos = 0
        print("Pontuação zerada!")

    def adicionar_pontos(self, quantidade):
        self.__pontos += quantidade

    def mostrar_pontos(self):
        print(self.__pontos)

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

    def exibir(self): 
        print(f"Menu: {self.titulo}")
        print("1. Iniciar Jogo")
        print("2. Sair")

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

    def exibir(self):
        super().exibir()
        print("3. Configurações Avançadas")

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

    def adicionar_pontos(self, quantidade):
        self.pontos += quantidade

class JogadorPremium(Jogador):
    def vencer_desafio(self, pontos_ganhos):
        bonus = 10
        self.pontos += pontos_ganhos + bonus
        print(f"{self.nome} (Premium) venceu um desafio com bônus! Pontuação: {self.pontos}")

    def adicionar_pontos(self, quantidade):
        self.pontos += quantidade * 2
        print(f"{self.nome} (Premium) ganhou pontos em dobro! Total: {self.pontos}")

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

class Fase:
    def __init__(self, nome, dificuldade):
        self.nome = nome
        self.dificuldade = dificuldade

    def mostrar_caracteristicas(self):
        print(f"Fase: {self.nome}")
        print(f"Dificuldade: {self.dificuldade}")
        print("Características gerais da fase.")

    def gerar_inimigos(self):  # Questão 41
        print("Gerando inimigos genéricos da fase.")

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

    def gerar_inimigos(self):
        print("Gerando escorpiões gigantes e bandidos armados do deserto!")

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

class Voador:
    def voar(self):
        print("Voando pelos céus majestosos!")

class Dragao(Inimigo, Voador):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida, forca)

    def atacar(self, alvo):
        dano = random.randint(15, 35) + self.forca 
        print(f"{self.nome} cospe fogo ferozmente!")
        alvo.tomar_dano(dano)

class Curador:
    def curar(self, aliado):
        cura = 30
        aliado.vida += cura
        print(f"{aliado.nome} foi curado em {cura} pontos de vida! Vida atual: {aliado.vida}")

class Paladino(Guerreiro, Curador):
    def __init__(self, nome, vida, energia):
        super().__init__(nome, vida, energia)

    def habilidade_especial(self):
        if self.energia >= 10:
            self.energia -= 10
            print(f"{self.nome} usa um golpe sagrado poderoso! (Energia restante: {self.energia})")
        else:
            print(f"{self.nome} não tem energia suficiente para o golpe sagrado.")

class MagiaElemental:
    def lancar_magia(self, elemento):
        elementos_validos = ["fogo", "água", "terra", "ar"]
        if elemento.lower() in elementos_validos:
            print(f"Lançando magia de {elemento}!")
        else:
            print("Elemento desconhecido. Escolha entre: fogo, água, terra ou ar.")

class MagoElemental(Mago, MagiaElemental):
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida, mana)

    def habilidade_especial(self):
        if self.mana >= 30:
            self.mana -= 30
            print(f"{self.nome} conjura uma poderosa magia elemental! (Mana restante: {self.mana})")
        else:
            print(f"{self.nome} não tem mana suficiente para conjurar uma magia elemental.")

class AnimalMontaria:
    def montar(self):
        print("Montando na criatura! Preparado para a batalha!")

class Cavaleiro(Guerreiro, AnimalMontaria):
    def __init__(self, nome, vida, energia):
        super().__init__(nome, vida, energia)

    def habilidade_especial(self):
        if self.energia >= 20:
            self.energia -= 20
            print(f"{self.nome} realizou um ataque devastador enquanto montado! (Energia restante: {self.energia})")
        else:
            print(f"{self.nome} está sem energia para o ataque montado.")
