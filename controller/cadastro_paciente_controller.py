import inquirer
from model.cadastro_paciente import SistemaHospital
from colorama import init, Fore, Style
import pandas

init()
cor_mensagem_erro = Fore.RED
modulo_cadastro_pacientes = SistemaHospital()

def run():
    while True:
        print('\nEscolha uma opção:')
        print('1 - Cadastrar novo paciente')
        print('2 - Cadastrar prontuario para paciente existente')
        print('3 - Listar pacientes e prontuarios')
        print('4 - Sair')

        opcao = input('Opção: ')

        if opcao == '1':
            modulo_cadastro_pacientes.cadastrar_paciente()
        elif opcao == '2':
            nome_paciente = input('Digite o nome do paciente para cadastrar um prontuario: ')

            try:
                arquivo = pandas.read_csv('database/pacientes.csv')
            except:
                arquivo = pandas.DataFrame()

            if not arquivo.empty and nome_paciente in arquivo['Nome'].astype(str).to_list(): 
                modulo_cadastro_pacientes.cadastrar_prontuario(nome_paciente)
            else:
                print('Paciente não encontrado.')
        elif opcao == '3':
            modulo_cadastro_pacientes.listar_pacientes_e_prontuarios(input("Digite o nome"))
        elif opcao == '4':
            print('Saindo do módulo de cadastro de pacientes...')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')


