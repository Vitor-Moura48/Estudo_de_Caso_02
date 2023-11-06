import csv
import datetime as dt
import pandas

class SistemaHospital:
    def __init__(self):
        self.caminho_pacientes = 'database/pacientes.csv'

    def adicionar_data(self):
        data_criacao = dt.datetime.now()
        return data_criacao.strftime("%d/%m/%y %H:%M")

    def cadastrar_paciente(self):
        while True:
            novo_paciente = {}
            novo_paciente['Data de Criacao'] = self.adicionar_data()
            novo_paciente['Nome'] = input('Digite o nome do paciente: ')
            novo_paciente['Idade'] = input('Digite a idade do paciente: ')
            novo_paciente['Sexo'] = input('Digite o sexo do paciente: ')
            novo_paciente['Identidade'] = input('Digite a identidade do paciente: ')
            novo_paciente['Contato de Emergencia'] = input('Digite um contato para emergência: ')
            novo_paciente['Estado'] = input('Digite o estado do paciente (Leve, Moderado ou Grave): ')
            novo_paciente['prontuario'] = []

            novo_paciente = pandas.DataFrame(novo_paciente)
            novo_paciente.to_csv(self.caminho_pacientes, index=False, mode="a")

            with open('database/pacientes.csv', mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=novo_paciente.keys())
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(novo_paciente)

            print('Paciente cadastrado com sucesso!\n')

            opcao = input('Deseja cadastrar outro paciente? (S/N): ')
            if opcao.lower() != 's':
                break

    def cadastrar_prontuario(self, paciente):
        while True:
            prontuario = {}
            prontuario['Data do diagnostico'] = [self.adicionar_data()]
            prontuario['diagnostico'] = [input('Digite o diagnostico do paciente: ')]
            prontuario['condicao'] = [input('Digite a condicao do paciente: ')]
            prontuario['Recomendacao de Medicacao'] = [input('Digite a Recomendacao de Medicacao: ')]
            prontuario['Historico Medico'] = [input('Digite o Historico Medico (opcional): ')]
            prontuario['Exames'] = [input('Digite os exames (opcional): ')]

            prontuario = pandas.DataFrame(prontuario)
            prontuario.to_csv(f'database/prontuarios/{paciente}.csv', mode='a')

            print('prontuario cadastrado com sucesso!\n')

            opcao = input('Deseja cadastrar outro prontuario para o paciente? (S/N): ')
            if opcao.lower() != 's':
                break

    def listar_pacientes_e_prontuarios(self, nome):
        try:
            arquivo = pandas.read_csv('database/pacientes.csv')
        except:
            arquivo = pandas.DataFrame()
        
        if not arquivo.empty and nome in arquivo['Nome'].astype(str).to_list(): 
            try:
                arquivo_prontuario = pandas.read_csv(f'database/prontuarios/{nome}.csv')
            except:
                arquivo_prontuario = pandas.DataFrame()

            print(arquivo[arquivo['Nome'] == nome])
            print(arquivo_prontuario.to_csv(index=False))
        else:
            print("Nome não encontrado")

       