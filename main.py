import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('userdata.db')
cursor = conn.cursor()

# Criar a tabela 'utilizadores'
cursor.execute('''
CREATE TABLE IF NOT EXISTS utilizadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    altura INTEGER NOT NULL,
    peso INTEGER NOT NULL
)
''')



for i in range(5):
    print("INCIO DE REGISTO DE UTILIZADORES:\n")
    print(f"\nInserindo os dados do utilizador {i + 1}:")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    altura = int(input("Digite a altura (em cm): "))
    peso = int(input("Digite o peso (em kg): "))

    cursor.execute('''
    INSERT INTO utilizadores (nome, idade, altura, peso)
    VALUES (?, ?, ?, ?)
    ''', (nome, idade, altura, peso))

# Salvar as alterações
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()

print("Usuários inseridos com sucesso!")
