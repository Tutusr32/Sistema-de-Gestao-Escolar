from create import criar_aluno
from read import ler_aluno
from update import atualizar_aluno
from delete import deletar
from database import set_database

def menu():
    set_database()
    try:
        while True:
            print("=-=" * 30)
            print(f"{'Sistema de Cadastro Escolar':^90}")
            print("=-=" * 30)

            print("""
            1. Cadastrar Alunos
            2. Consultar Alunos
            3. Atualizar Alunos
            4. Deletar Alunos
            0. Sair
            """)

            opcao = int(input('Selecione a opção: '))

            match opcao:
                case 1:
                    criar_aluno()
                case 2: 
                    ler_aluno()
                case 3:
                    atualizar_aluno()
                case 4: 
                    deletar()
                case 0:
                    print("Sistema finalizado.")
                    return 
                    break

    except ValueError:
        print('Use somente valores válidos.')
    finally:
        pass

if __name__ == "__main__":
    menu()