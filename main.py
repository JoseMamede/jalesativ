from auladehoje import Livro
biblioteca = []
livro1 = Livro("Dom Casmurro", "Machado de Assis", "9788574801414", 3)
livro2 = Livro("1984", "George Orwell", "9788535914849", 5)
biblioteca.append(livro1)
biblioteca.append(livro2)

# Realizando operações
print(f"Emprestando '{livro1.get_titulo()}': {livro1.emprestar()}")
print(f"Disponibilidade: {livro1.get_disponibilidade()}")
