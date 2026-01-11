from database import conectar

def atualizar_aluno():
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        while True:
            ID = int(input('Selecione o ID do aluno que deseja atualizar dados: '))

            cursor.execute("SELECT id FROM alunos WHERE id = ?", (ID,))
            if not cursor.fetchone():
                print(f"ID {ID} não encontrado.")
                continue
        
            opcao = int(input(""" 
            O que deseja mudar?:
            Sair = 0
            Nome = 1
            Idade = 2
            Curso = 3                                                           
            """))
        
            match opcao:
                case 1:
                    novo_valor = input('Digite o novo nome: ')
                    cursor.execute("UPDATE alunos SET nome = ? WHERE id = ?", (novo_valor, ID))
                case 2:
                    novo_valor = int(input('Digite a nova idade: '))
                    cursor.execute("UPDATE alunos SET idade = ? WHERE id = ?", (novo_valor, ID))
                case 3:
                    novo_valor = input('Digite o novo curso: ')
                    cursor.execute("UPDATE alunos SET curso = ? WHERE id = ?", (novo_valor, ID))
                case 0:
                    print("Opção inválida. Operação abortada.")
                    return 

            conn.commit()

            print("Dados atualizados com sucesso!")

            continuar = input('Deseja atualizar outro? (S/N): ').strip().upper()
            if continuar == 'N':
                break
            
    except ValueError:
        print('Apenas valores válidos, por favor.')
    finally:
        if conn:
            conn.close()