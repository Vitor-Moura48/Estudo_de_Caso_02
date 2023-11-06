import inquirer
from model.cadastro_paciente import SistemaHospital
from colorama import init, Fore, Style

init()
cor_mensagem_erro = Fore.RED
sistema_hospital = SistemaHospital()

def run():

    while True:
        print('\nEscolha uma opção:')
        print('1 - Cadastrar novo paciente')
        print('2 - Cadastrar prontuário para paciente existente')
        print('3 - Listar pacientes e prontuários')
        print('4 - Sair')

        opcao = input('Opção: ')

        if opcao == '1':
            sistema_hospital.cadastrar_paciente()
        elif opcao == '2':
            sistema_hospital.listar_pacientes_e_prontuarios()
            nome_paciente = input('Digite o nome do paciente para cadastrar um prontuário: ')
            paciente_encontrado = next((p for p in sistema_hospital.lista_de_todos_os_pacientes if p['Nome'] == nome_paciente), None)
            if paciente_encontrado:
                sistema_hospital.cadastrar_prontuario(paciente_encontrado)
            else:
                print('Paciente não encontrado.')
        elif opcao == '3':
            sistema_hospital.listar_pacientes_e_prontuarios()
        elif opcao == '4':
            break

