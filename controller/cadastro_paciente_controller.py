import inquirer
from model.cadastro_paciente import SistemaHospital
from colorama import init, Fore, Style

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
            modulo_cadastro_pacientes.listar_pacientes_e_prontuarios(input("Digite o nome"))
            nome_paciente = input('Digite o nome do paciente para cadastrar um prontuario: ')
            paciente_encontrado = next((p for p in modulo_cadastro_pacientes.lista_de_todos_os_pacientes if p['Nome'] == nome_paciente), None)
            if paciente_encontrado:
                modulo_cadastro_pacientes.cadastrar_prontuario(paciente_encontrado)
            else:
                print('Paciente não encontrado.')
        elif opcao == '3':
            modulo_cadastro_pacientes.listar_pacientes_e_prontuarios(input("Digite o nome"))
        elif opcao == '4':
            print('Saindo do módulo de cadastro de pacientes...')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')


