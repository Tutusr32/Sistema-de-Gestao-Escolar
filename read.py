from database import conectar

def ler_aluno():
    conn = None
    try:
        while True:
            ID = int(input('Insira o ID do aluno quer consultar (Todos = 0): '))

            conn = conectar()
            cursor = conn.cursor()

            if ID == 0:
                cursor.execute("SELECT * FROM alunos")

            else:
                cursor.execute("SELECT * FROM alunos WHERE id = ?", (ID,))

            validacao = False
            for aluno in cursor:
                print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} | Curso: {aluno[3]}")
                validacao = True

            if not validacao:
                print("Nenhum registro encontrado.")

            continuar = input('Deseja consultar outro? (S/N): ').strip().upper()
            if continuar == 'N':
                break

    except ValueError:
        print('ID precisa ser um número inteiro.')
    
    finally:
        if conn:
            conn.close()