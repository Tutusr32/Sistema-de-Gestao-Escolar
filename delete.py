from database import conectar

def deletar():
    conn = None
    try:
        while True:
            conn = conectar()
            cursor = conn.cursor()

            ID = int(input('Selecione o ID do aluno que deseja deletar: '))

            cursor.execute("DELETE FROM alunos WHERE id = ?",(ID,))

            if cursor.rowcount == 0:
                print("Nenhum registro encontrado para deletar.")
                break
            else:
                conn.commit()
                print(f"{cursor.rowcount} registro(s) deletado(s).")

            continuar = input('Deseja deletar outro? (S/N): ').strip().upper()
            if continuar == 'N':
                break

    except ValueError:
        print('Digite número válidos')

    finally:
        if conn:
            conn.close()