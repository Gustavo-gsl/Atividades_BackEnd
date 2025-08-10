class Biblioteca:

    def __init__(self, nome):
        
        self.nome = nome
        self.acervo = []
        self.membros = []
    
    def adicionar_material(self, material):

        self.acervo.append(material.titulo)

    def registrar_membro(self, membro):

        self.membros.append(membro.numero_membro)
    
    def realizar_emprestimo(self, material, membro):

        print(f"\n--- Tentativa de Empréstimo - Material: \"{material.titulo}\" | Membro: \"{membro.nome}\" ---")

        if material.titulo not in self.acervo:

            print(f"\n{f"Erro: Material inexistente no Acervo":^50}\n")

        elif material.disponivel == False:

            print(f"\n{f"Erro: Material indisponível":^50}\n")

        elif membro.numero_membro not in self.membros:

            print(f"\n{f"Erro: Membro não cadastrado":^50}\n")
        
        else:

            membro.materiais_emprestados.append(material.titulo)
            material.disponivel = False
            print(f"\n{f"\"{material.titulo}\" foi emprestado por {membro.nome}":^50}\n")

    def realizar_devolucao(self, material, membro):

        print(f"\n--- Tentativa de Devolução - Material: \"{material.titulo}\" | Membro: \"{membro.nome}\" ---")

        if material.titulo in membro.materiais_emprestados:

            membro.materiais_emprestados.remove(material.titulo)
            material.disponivel = True
            print(f"\n{f"\"{material.titulo}\" foi devolvido por {membro.nome}":^50}\n")

        else:

            print(f"\n{f"Erro: Material não estava com o membro":^50}\n")