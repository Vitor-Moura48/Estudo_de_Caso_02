import csv
import datetime as dt

# Lista de todos os pacientes
lista_de_todos_os_pacientes = []

def adicionar_data():
    data_criacao = dt.datetime.now()
    return data_criacao.strftime("%d/%m/%y %H:%M")

# Função para cadastrar paciente
def cadastrar_paciente():
    while True:
        novo_paciente = {}
        novo_paciente['Data de Criacao'] = adicionar_data()
        novo_paciente['Nome'] = input('Digite o nome do paciente: ')
        novo_paciente['Idade'] = input('Digite a idade do paciente: ')
        novo_paciente['Sexo'] = input('Digite o sexo do paciente: ')
        novo_paciente['Identidade'] = input('Digite a identidade do paciente: ')
        novo_paciente['Contato de Emergencia'] = input('Digite um contato para emergência: ')
        novo_paciente['Estado'] = input('Digite o estado do paciente (Leve, Moderado ou Grave): ')
        novo_paciente['prontuario'] = []

        lista_de_todos_os_pacientes.append(novo_paciente)

        
        with open('database/pacientes.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=novo_paciente.keys())
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(novo_paciente)

        print('Paciente cadastrado com sucesso!\n')

        opcao = input('Deseja cadastrar outro paciente? (S/N): ')
        if opcao.lower() != 's':
            break

# Função para cadastrar prontuario do paciente
def cadastrar_prontuario(paciente):
    while True:
        prontuario = {}
        prontuario['Data do diagnostico'] = adicionar_data()
        prontuario['diagnostico'] = input('Digite o diagnostico do paciente: ')
        prontuario['condicao'] = input('Digite a condicao do paciente: ')
        prontuario['Recomendacao de Medicacao'] = input('Digite a Recomendacao de Medicacao: ')
        prontuario['Historico Medico'] = input('Digite o Historico Medico (opcional): ')
        prontuario['Exames'] = input('Digite os exames (opcional): ')

        paciente['prontuario'].append(prontuario)

        
        nome_paciente = paciente['Nome']
        with open(f'database/prontuarios/{nome_paciente}.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=prontuario.keys())
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(prontuario)

        print('prontuario cadastrado com sucesso!\n')

        opcao = input('Deseja cadastrar outro prontuario para o paciente? (S/N): ')
        if opcao.lower() != 's':
            break

def listar_pacientes_e_prontuarios(pacientes):
    for i, paciente in enumerate(pacientes):
        print(f'\n** Paciente {i + 1} **')
        print(f'Data de Criacao: {paciente["Data de Criacao"]}')
        print(f'Nome: {paciente["Nome"]}')
        print(f'Idade: {paciente["Idade"]}')
        print(f'Sexo: {paciente["Sexo"]}')
        print(f'Identidade: {paciente["Identidade"]}')
        print(f'Contato de Emergencia: {paciente["Contato de Emergencia"]}')
        print(f'Estado: {paciente["Estado"]}')
        print('\n** prontuarios **')
        prontuarios = paciente["prontuario"]
        if prontuarios:
            for j, prontuario in enumerate(prontuarios):
                print(f'** prontuario {j + 1} **')
                print(f'Data do diagnostico: {prontuario["Data do diagnostico"]}')
                print(f'diagnostico: {prontuario["diagnostico"]}')
                print(f'condicao: {prontuario["condicao"]}')
                print(f'Recomendacao de Medicacao: {prontuario["Recomendacao de Medicacao"]}')
                if prontuario['Historico Medico']:
                    print(f'Historico Medico: {prontuario["Historico Medico"]}')
                if prontuario['Exames']:
                    print(f'Exames: {prontuario["Exames"]}')
        else:
            print('Nenhum prontuario cadastrado para este paciente.')

if __name__ == "__main__":
    while True:
        print('\nEscolha uma opção:')
        print('1 - Cadastrar novo paciente')
        print('2 - Cadastrar prontuario para paciente existente')
        print('3 - Listar pacientes e prontuarios')
        print('4 - Sair')

        opcao = input('Opção: ')

        if opcao == '1':
            cadastrar_paciente()
        elif opcao == '2':
            listar_pacientes_e_prontuarios(lista_de_todos_os_pacientes)
            nome_paciente = input('Digite o nome do paciente para cadastrar um prontuario: ')
            paciente_encontrado = next((p for p in lista_de_todos_os_pacientes if p['Nome'] == nome_paciente), None)
            if paciente_encontrado:
                cadastrar_prontuario(paciente_encontrado)
            else:
                print('Paciente não encontrado.')
        elif opcao == '3':
            listar_pacientes_e_prontuarios(lista_de_todos_os_pacientes)
        elif opcao == '4':
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')
