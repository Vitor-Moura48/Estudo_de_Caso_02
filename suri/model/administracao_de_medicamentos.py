import pandas
import os

class AdmMedicamentos:
    def __init__(self):
        self.caminho_arquivo = "suri/database/medicamentos.csv"
        if not os.path.exists(self.caminho_arquivo):
            arquivo = pandas.DataFrame()
            arquivo.to_csv(self.caminho_arquivo, index=False)
          
    def cadastrar_medicamento(self, nome, principio_ativo, dosagem, forma_adiministracao):
        try:
            arquivo = pandas.read_csv(self.caminho_arquivo)
        except:
            arquivo = pandas.DataFrame()

        if nome in arquivo.columns:
            print("medicamento já cadastrado!")
        else:
            arquivo[nome] = [principio_ativo, dosagem, forma_adiministracao]
    
        arquivo.to_csv(self.caminho_arquivo, index=False)
        

        

        

adiministrar_medicamento = AdmMedicamentos()
adiministrar_medicamento.cadastrar_medicamento("remedio", "ingerir", "200ml", "tomar")
adiministrar_medicamento.cadastrar_medicamento("remedio 2", "ingerir 2", "200ml 2", "tomar 2")