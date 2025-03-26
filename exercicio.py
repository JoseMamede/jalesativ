#Faça as seguintes classes com seus aributos: Livro,ContaBancaria,Tarefa
class livro:
    def __init__(self):
        self.autor = None
        self.nome = None
        self.preco = None
        self.quantidade = None
        self.editora = None
        
test = livro()
test.autor = "Boichi"
print(test.autor)

class contabancaria:
    def __init__(self):
        self.agencia = None
        self.nomebanco = None
        self.tipoconta = None
        self.user = None
        self.user = None
        self.senha = None

teste = contabancaria
teste.nomebanco = "Nubanks"
print(teste.nomebanco)

class tarefa:
    def __init__(self):
        self.data = None
        self.evento = None
        self.horario = None
        self.oqlevar = None
        self.vestes = None

tete = tarefa
tete.evento = "BGS"
print(tete.evento)

#Dificil ヾ｜￣ー￣｜ﾉ
class termostato:
    def __init__(self):
        self.aparelho = None
        self.temperatura = None
        self.tipo = None
        self.saida = None

tezte = termostato
tezte.tipo = "Termostato mecânico."
print(tezte.tipo)

class dna:
    def __init__(self):
        self.bases = None
        self.formas = None
        self.cromosomos = None

tet = dna
tet.formas = "forma A"
print(tet.formas)

class pixel:
    def __init__(self):
        self.cor = None
        self.saturacao = None
        self.brilho = None
    
teszte = pixel
teszte.cor = "cinza"
print(teszte.cor)
