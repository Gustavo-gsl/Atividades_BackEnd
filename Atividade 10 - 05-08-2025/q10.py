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
maus = Livro("Maus", "Art Spiegelman", 1986)
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