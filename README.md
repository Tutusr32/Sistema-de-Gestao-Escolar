# Sistema de Gestão Escolar (CRUD)
Um sistema robusto de gerenciamento de alunos via linha de comando (CLI), focado em **resiliência de dados**, **modularidade** e **experiência do usuário (UX)** no terminal. Desenvolvido para demonstrar práticas sólidas de arquitetura de software e manipulação de bancos de dados relacionais.

# Funcionalidades
- **Cadastrar Alunos:** Entrada de dados blindada contra tipos inválidos.
- **Consultar Alunos:** Busca por ID específico ou listagem completa com formatação centralizada.
- **Atualizar Dados:** Alteração seletiva de campos (Nome, Idade, Curso) com validação de existência.
- **Deletar Alunos:** Operação de exclusão segura com feedback de linhas afetadas.

## Estrutura do Projeto
```text
├── main.py          # Ponto de entrada e orquestrador do sistema.
├── database.py      # Lógica de conexão com o SQLite.
├── create.py        # Módulo de inserção de dados.
├── read.py          # Módulo de consulta e exibição.
├── update.py        # Módulo de atualização de registros.
├── delete.py        # Módulo de exclusão de dados.
└── alunos.db        # Banco de dados local (gerado automaticamente).
```
# Como Executar
- Certifique-se de ter o Python 3.x instalado.
- Clone o repositório: git clone [https://github.com/Tutusr32/Sistema-de-Gestao-Escolar.git](https://github.com/Tutusr32/Sistema-de-Gestao-Escolar.git)
- Execute o Sistema: main.py
