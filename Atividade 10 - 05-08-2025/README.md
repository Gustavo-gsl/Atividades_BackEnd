# Atividade 10
## Questão Única
```python
from membro import Membro
from material import Livro, DVD
from biblioteca import Biblioteca

#Instanciando a classe Biblioteca -> Instância: biblioteca
biblioteca = Biblioteca("Babel")

#Instanciando a classe Membro -> Instâncias: jonas, alberto e maria
jonas = Membro("Jonas", 1)
alberto = Membro("Alberto", 2)
maria = Membro("Maria", 3)

#Instanciando as classes Livro (Instâncias: maus e jogos_vorazes) e DVD (Instâncias: shrek3)
maus = Livro("Maus", "Art", 2020)
jogos_vorazes = Livro("Jogos Vorazes", "Suzanne Collins", 2010)
shrek3 = DVD("Shrek 3", 93)

#Registrando membros com o método .registrar_membro()
biblioteca.registrar_membro(jonas)
biblioteca.registrar_membro(maria)

#Adicionando materias com o método .adicionar_material()
biblioteca.adicionar_material(maus)
biblioteca.adicionar_material(shrek3)

#Simulando os processos na biblioteca
biblioteca.realizar_emprestimo(maus, jonas)

biblioteca.realizar_emprestimo(maus, maria)

biblioteca.realizar_emprestimo(shrek3, maria)

biblioteca.realizar_devolucao(maus, jonas)

biblioteca.realizar_emprestimo(jogos_vorazes, jonas)

biblioteca.realizar_devolucao(shrek3, maria)

biblioteca.realizar_emprestimo(shrek3, alberto)

biblioteca.realizar_devolucao(shrek3, jonas)
```
[| Arquivo da questão |](q10.py)
### Arquivos Relacionados
[| membro.py |](membro.py)
```python
class Membro:

    def __init__(self, nome, numero_membro):
        
        self.nome = nome
        self.numero_membro = numero_membro
        self.materiais_emprestados = []
```

---

[| material.py |](material.py)
```python
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
```

---

[| biblioteca.py |](biblioteca.py)
```python
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
```