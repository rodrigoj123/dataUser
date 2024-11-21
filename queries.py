# Importa o módulo sqlite3, que permite interagir com bases de dados SQLite
import sqlite3

# Estabelece uma ligação à base de dados SQLite chamada 'userdata.db'.
conn = sqlite3.connect('userdata.db')

# Cria um objeto cursor que vai ser utilizado para executar os comandos SQL no banco de dados
cursor = conn.cursor()


# Função para listar os dados de um utilizador específico
def mostrarDadosUser(nomePassado):
    cursor.execute("""
        SELECT *
        FROM utilizadores
        WHERE nome = ?
    """, (nomePassado,))  # Passa o parâmetro de forma segura como uma tupla

    # Busca os resultados
    resultados = cursor.fetchall()

    # Verifica se há dados retornados
    if resultados:
        for linha in resultados:
            id_user, nome, idade, altura, peso = linha

            # Calcular o IMC
            alturaEMmetros = altura / 100
            imc = peso / (alturaEMmetros ** 2)

            # Exibir os dados e o IMC
            print("ID:", id_user)
            print("Nome:", nome)
            print("Idade:", idade)
            print("Altura:", altura, "cm")
            print("Peso:", peso, "kg")
            print(f"IMC: {imc:.2f}")  # Mostra o IMC com 2 casas decimais
    else:
        print("Nenhum utilizador encontrado com o nome:", nomePassado)


# Chamar a função para mostrar os dados do utilizador com o nome "jordao"
mostrarDadosUser("tiago")

def mostrarTodosUtilizadores():
    cursor.execute("SELECT * FROM utilizadores")
    # Busca todos os resultados
    utilizadores = cursor.fetchall()

    # Exibe os utilizadores de forma estruturada
    if utilizadores:
        print("\nLista de todos os utilizadores:")
        for utilizador in utilizadores:
            print(f"ID: {utilizador[0]}, Nome: {utilizador[1]}, Idade: {utilizador[2]} anos, "
                  f"Altura: {utilizador[3]} cm, Peso: {utilizador[4]} kg")
    else:
        print("Nenhum utilizador encontrado na base de dados.")

# Mostrar a lista de todos os utilizadores
mostrarTodosUtilizadores()
conn.close()
