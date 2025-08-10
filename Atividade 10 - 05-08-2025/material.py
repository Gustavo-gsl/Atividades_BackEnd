class Material:

    def __init__(self, titulo):
        
        self.titulo = titulo
        self.disponivel = True

class Livro(Material):

    def __init__(self, titulo, autor, ano_publicacao):
        
        super().__init__(titulo)
        self.autor = autor
        self.ano_publicacao = ano_publicacao

class DVD(Material):

    def __init__(self, titulo, duracao):
        
        super().__init__(titulo)
        self.duracao = duracao