import csv
import os
from datetime import datetime

class ControleEquipamentos:
    def __init__(self, arquivo_equipamentos='equipamentos.csv'):
        self.arquivo_equipamentos = arquivo_equipamentos
        self.equipamentos = self.carregar_equipamentos()

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

    def salvar_equipamentos(self):
        with open(self.arquivo_equipamentos, 'w', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(['Nome', 'Modelo', 'Número de Série', 'Data de Aquisição'])
            for equipamento in self.equipamentos:
                escritor.writerow([equipamento['nome'], equipamento['modelo'], equipamento['numero_serie'], equipamento['data_aquisicao']])

    def adicionar_equipamento(self, equipamento):
        self.equipamentos.append(equipamento)
        self.salvar_equipamentos()
    
    def listar_equipamentos(self):
        with open(self.arquivo_equipamentos, 'r', newline='') as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                print(f'Nome: {linha[0]}, Modelo: {linha[1]}, Número de Série: {linha[2]}, Data de Aquisição: {linha[3]}')

    def executar(self):
         while True:
            print("\nControle de Equipamentos")
            print("1. Registrar Equipamento")
            print("2. Listar Equipamentos")
            print("3. Sair")

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
                print("Saindo do sistema.")
                break

            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    controle = ControleEquipamentos()
    controle.executar()
