class Livro:
    def __init__(self, titulo, autor, isbn, copias_totais):
        self.isbn = isbn
        self.__titulo = titulo
        self.autor = autor
        self.copias_totais = copias_totais
        self.__copias_disponiveis = 0
        self.__emprestimos = []
    
    def get_emprestimos(self):
        return self.__emprestimos
    
    def emprestar(self):
        if self.get_disponibilidade() > 0:
            self.__emprestimos.append('Livro emprestado')
            return("Livro emprestado com sucesso")
        else:
            print("Não ha mais livros para emprestar.")

    def devolver(self, emprestimo):
        self.__emprestimos.remove()

    def get_disponibilidade(self):
        return self.__copias_totais - len(self.__emprestimo)
    
    def get_titulo(self):
        return self.__titulo