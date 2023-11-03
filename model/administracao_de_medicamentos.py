import pandas
import os
import json

class AdmMedicamentos:
    def __init__(self):
        self.caminho_arquivo_medicamentos = "database/medicamentos.csv"

        if not os.path.exists(self.caminho_arquivo_medicamentos):
            arquivo = pandas.DataFrame()
            arquivo.to_csv(self.caminho_arquivo_medicamentos, index=False) 
          
    def cadastrar_medicamento(self, nome, principio_ativo, dosagem, forma_adiministracao):
        try:
            arquivo = pandas.read_csv(self.caminho_arquivo_medicamentos)
        except:
            arquivo = pandas.DataFrame()
       
        if not arquivo.empty and nome in arquivo['nome'].values:    
            print("Medicamento já cadastrado!!")
        else:
            novo_medicamento = {'nome': [nome],
                                "principio_ativo": [principio_ativo], 
                                "dosagem": [dosagem], 
                                "forma_adiministracao": [forma_adiministracao],
                                }  
            novo_medicamento = pandas.DataFrame(novo_medicamento)
            if arquivo.empty:
                novo_medicamento.to_csv(self.caminho_arquivo_medicamentos, index=False, mode="a")
            else:
                novo_medicamento.to_csv(self.caminho_arquivo_medicamentos, index=False, mode="a", header=False)

    def adicionar_lote(self, lote, quantidade, validade, fornecedor):
        try:
            arquivo = pandas.read_csv(self.caminho_arquivo_medicamentos)
        except:
            arquivo = pandas.DataFrame()

        if not arquivo.empty:
            print("Selecione o medicamento: ")
            for medicamentos in arquivo['nome'].values:
                print(medicamentos)
        else:
            print("Sem medicamentos registrados!")

        
        
    

adiministrar_medicamento = AdmMedicamentos()
adiministrar_medicamento.cadastrar_medicamento("remedio", "ingerir", "200ml", "tomar")
adiministrar_medicamento.cadastrar_medicamento("remedio", "ingerir", "200ml", "tomar")
adiministrar_medicamento.cadastrar_medicamento("remedio", "ingerir", "200ml", "tomar")
adiministrar_medicamento.cadastrar_medicamento("remedio 2", "ingerir 2", "200ml 2", "tomar 2")

adiministrar_medicamento.adicionar_lote('253255', 4365, '14/03/2024', 'NEUXFJ')