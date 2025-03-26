#Criar classe
class hq:
    def __init__(self):
        self.nome = None
        self.preco = None
        self.quantidade = None
        

seila = hq()
seila.nome = "Preacher"
print(seila.nome)

# Definir uma classe com dois atributos
class vidaemana:
    def __init__(self, vida, mana):
        self.vida = vida
        self.mana = mana

destri = vidaemana(32, 34)
print(destri.vida)
print(destri.mana)