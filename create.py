from database import conectar

def criar_aluno():
    conn = None
    try:
        while True:
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            curso = input("Curso: ")

            conn = conectar()
            cursor = conn.cursor()
        
            cursor.execute("INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)", (nome, idade, curso))

            conn.commit()

            print(f'Aluno {nome} adicionado com sucesso')

            continuar = input('Deseja cadastrar outro? (S/N): ').strip().upper()
            if continuar == 'N':
                break

    except ValueError:
        print('Digite apenas valores válidos')

    finally:
        if conn:
            conn.close()