import csv
import os
from datetime import datetime

class ControleEquipamentos:
    def __init__(self, arquivo_equipamentos='database/equipamentos.csv'):
        self.arquivo_equipamentos = arquivo_equipamentos
        self.equipamentos = self.carregar_equipamentos()

    #Carrega a lista de equipamentos, se não tive cria uma lista vazia
    def carregar_equipamentos(self):
        if os.path.exists(self.arquivo_equipamentos):
            equipamentos = []
            with open(self.arquivo_equipamentos, 'r', newline='') as arquivo:
                leitor = csv.reader(arquivo)
                next(leitor)  # Pular cabeçalho para não repetir duas vezes
                for linha in leitor:
                    nome, modelo, numero_serie, data_aquisicao = linha
                    equipamento = {'nome': nome, 'modelo': modelo, 'numero_serie': numero_serie, 'data_aquisicao': data_aquisicao, 'historico_manutencao': [], 'programacao_manutencao': []}
                    equipamentos.append(equipamento)
            return equipamentos
        return []

    #Depois de adicionado salva no arquivo csv
    def salvar_equipamentos(self):
        with open(self.arquivo_equipamentos, 'w', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(['Nome', 'Modelo', 'Número de Série', 'Data de Aquisição'])
            for equipamento in self.equipamentos:
                escritor.writerow([equipamento['nome'], equipamento['modelo'], equipamento['numero_serie'], equipamento['data_aquisicao']])
    
    #Registra novos equipamentos
    def adicionar_equipamento(self, equipamento):
        self.equipamentos.append(equipamento)
        self.salvar_equipamentos()
    
    #Lista dos equipamentos que já tem no arquivo csv
    def listar_equipamentos(self):
        with open(self.arquivo_equipamentos, 'r', newline='') as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                print(f'Nome: {linha[0]}, Modelo: {linha[1]}, Número de Série: {linha[2]}, Data de Aquisição: {linha[3]}')
    
    #Depois que agenda a manutenção e conclui ela é adicionada no histórico
    def adicionar_historico_manutencao(self, numero_serie, data, tipo, intervencao):
        for equipamento in self.equipamentos:
            if equipamento['numero_serie'] == numero_serie:
                historico = {'data': data, 'tipo': tipo, 'intervencao': intervencao}
                equipamento['historico_manutencao'].append(historico)
                self.salvar_equipamentos()
                print("Histórico de manutenção adicionado com sucesso!")
                return
        print("Equipamento não encontrado.")

    #Lista todas as manutenções feitas a partir do histórico
    def listar_historico_manutencao(self, numero_serie):
        for equipamento in self.equipamentos:
            if equipamento['numero_serie'] == numero_serie:
                print("\nHistórico de Manutenção:")
                for registro in equipamento['historico_manutencao']:
                    print(f'Data: {registro["data"]}, Tipo: {registro["tipo"]}, Intervenção: {registro["intervencao"]}')
                return
        print("Equipamento não encontrado.")

    #Faz o agendamento da manutenção
    def agendar_manutencao_preventiva(self, numero_serie, data, tipo):
        for equipamento in self.equipamentos:
            if equipamento['numero_serie'] == numero_serie:
                programacao = {'data': data, 'tipo': tipo}
                equipamento['programacao_manutencao'].append(programacao)
                self.salvar_equipamentos()
                print("Manutenção preventiva agendada com sucesso!")
                return
        print("Equipamento não encontrado.")

    #Lista das manutenções fututuas
    def listar_programacao_manutencao(self, numero_serie):
        for equipamento in self.equipamentos:
            if equipamento['numero_serie'] == numero_serie:
                print("\nProgramação de Manutenção Preventiva:")
                for programacao in equipamento['programacao_manutencao']:
                    print(f'Data: {programacao["data"]}, Tipo: {programacao["tipo"]}')
                return
        print("Equipamento não encontrado.")

    #Menu do usuário para escolher a tarefa desejada
    def executar(self):
         while True:
            print("\nControle de Equipamentos")
            print("1. Registrar Equipamento")
            print("2. Listar Equipamentos")
            print("3. Adicionar Histórico de Manutenção")
            print("4. Listar Histórico de Manutenção")
            print("5. Agendar Manutenção Preventiva")
            print("6. Listar Programação de Manutenção Preventiva")
            print("7. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                nome = input("Nome do equipamento: ")
                modelo = input("Modelo do equipamento: ")
                numero_serie = input("Número de Série: ")
                data_aquisicao = input("Data de Aquisição (dd/mm/aaaa): ")
                data_aquisicao = datetime.strptime(data_aquisicao, "%d/%m/%Y").strftime("%d/%m/%Y")
                
                equipamento = {'nome': nome, 'modelo': modelo, 'numero_serie': numero_serie, 'data_aquisicao': data_aquisicao, 'historico_manutencao': [], 'programacao_manutencao': []}
                self.adicionar_equipamento(equipamento)
                print("Equipamento registrado com sucesso!")

            elif escolha == '2':
                print("\nEquipamentos Registrados:")
                self.listar_equipamentos()

            elif escolha == '3':
                print("\nAdicionar Histórico de Manutenção:")
                numero_serie = input("Número de Série do equipamento: ")
                data = input("Data da manutenção (dd/mm/aaaa): ")
                data = datetime.strptime(data, "%d/%m/%Y").strftime("%d/%m/%Y")
                tipo = input("Tipo de manutenção: ")
                intervencao = input("Intervenção realizada: ")
                self.adicionar_historico_manutencao(numero_serie, data, tipo, intervencao)

            elif escolha == '4':
                numero_serie = input("Número de Série do equipamento: ")
                self.listar_historico_manutencao(numero_serie)

            elif escolha == '5':
                print("\nAgendar Manutenção Preventiva:")
                numero_serie = input("Número de Série do equipamento: ")
                data = input("Data da manutenção preventiva (dd/mm/aaaa): ")
                data = datetime.strptime(data, "%d/%m/%Y").strftime("%d/%m/%Y")
                tipo = input("Tipo de manutenção preventiva: ")
                self.agendar_manutencao_preventiva(numero_serie, data, tipo)

            elif escolha == '6':
                numero_serie = input("Número de Série do equipamento: ")
                self.listar_programacao_manutencao(numero_serie)

            elif escolha == '7':
                break    

            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    controle = ControleEquipamentos()
    controle.executar()
