# O código abaixo implementa um sistema de cadastro de alunos com funcionalidades de cadastro, exibição, busca e estatísticas.
alunos = {}

# Função para cadastrar um aluno
def cadastrar_aluno():
    nome= input('Digite o nome do aluno: ').strip().title()
    idade = int(input('Digite a idade do aluno: '))
    
    # Coleta de notas
    notas = []
    for i in range(1, 4):
        nota = float(input(f'Digite a nota {i}: '))
        notas.append(nota)

    # Cálculo da média e status
    media = sum(notas) / len(notas)
    if media >= 7:
        status = 'Aprovado'
    elif media >= 5:
        status = 'Recuperação'
    else:
        status = 'Reprovado'

    # Armazenando os dados no dicionário
    alunos[nome] = {
        'idade': idade,
        'notas': notas,
        'media': round(media, 2),
        'status': status
    }

    print(f'\nAluno {nome} cadastrado com sucesso!\n')

# Função para exibir todos os alunos cadastrados
def exibir_todos():
    if not alunos:
        print('Nenhum aluno cadastrado. \n')
        return
    
    print('\n===== LISTA DE ALUNOS =====')
    for nome, dados in alunos.items():
        print(f'Nome: {nome}')
        print(f'Idade: {dados["idade"]}')
        print(f'Notas: {dados["notas"]}')
        print(f'Média: {dados["media"]}')
        print(f'Status: {dados["status"]}')
        print('-' * 30)
    print()

# Função para buscar um aluno pelo nome
def buscar_aluno():
    nome = input('Digite o nome do aluno que deseaja buscar: ').strip().title()
    if nome in alunos:
        dados = alunos[nome]
        print(f'\nNome: {nome}')
        print(f'Idade: {dados["idade"]}')
        print(f'Notas: {dados["notas"]}')
        print(f'Média: {dados["media"]}')
        print(f'Status: {dados["status"]}\n')

    else:
        print(f'Aluno {nome} não encontrado.\n')

# Função para exibir estatísticas dos alunos
def estatisticas():
    if not alunos:
        print('Nenhum aluno cadastrado para exibir estatísticas. \n')
        return
    
    total_alunos = len(alunos)
    aprovados = sum(1 for a in alunos.values() if a['status'] == 'Aprovado')
    recuperacao = sum(1 for a in alunos.values() if a['status'] == 'Recuperação')
    reprovados = sum(1 for a in alunos.values() if a['status'] == 'Reprovado')
    media_geral = sum(a['media'] for a in alunos.values()) / total_alunos

    print('\n===== ESTATÍSTICAS DA TURMA =====')
    print(f'Total de alunos: {total_alunos}')
    print(f'Aprovados: {aprovados}')
    print(f'Em recuperação: {recuperacao}')
    print(f'Reprovados: {reprovados}')
    print(f'Média geral da turma: {round(media_geral,2)}\n')

# Função principal para o menu
def menu ():
    while True:
        print('===== MENU =====')
        print('1. Cadastrar aluno')
        print('2. Exibir todos os alunos')
        print('3. Buscar aluno')
        print('4. Exibir estatísticas da turma')
        print('5. Sair')

        opcao = int(input('\nEscolha uma opção: '))

        if opcao == 1:
            cadastrar_aluno()
        elif opcao == 2:
            exibir_todos()
        elif opcao == 3:
            buscar_aluno()
        elif opcao == 4:
            estatisticas()
        elif opcao == 5:
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida. Tente novamente.\n')

# Início do programa
menu()       