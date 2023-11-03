import pandas
import os
import json

class AdmMedicamentos:
    def __init__(self):
        self.caminho_arquivo_medicamentos = "database/medicamentos.csv"
        self.caminho_arquivo_estoque = "database/registro_de_lote_medicamentos.csv"

        if not os.path.exists(self.caminho_arquivo_medicamentos):
            arquivo = pandas.DataFrame()
            arquivo.to_csv(self.caminho_arquivo_medicamentos, index=False)
        if not os.path.exists(self.caminho_arquivo_estoque):
            arquivo = pandas.DataFrame()
            arquivo.to_csv(self.caminho_arquivo_estoque, index=False) 
          
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

    def registrar_lote(self, lote, quantidade, validade, fornecedor):
        try:
            arquivo = pandas.read_csv(self.caminho_arquivo_medicamentos)
        except:
            arquivo = pandas.DataFrame()

        try:
            arquivo_estoque = pandas.read_csv(self.caminho_arquivo_estoque)
        except:
            arquivo_estoque = pandas.DataFrame()


        if not arquivo.empty:

            print("Selecione o medicamento: ")
            for medicamentos in arquivo['nome'].values:
                print(medicamentos)

            selecionado = input("medicamento: ")
            if not arquivo_estoque.empty:
                print(arquivo_estoque['lote'].values)
            if not arquivo_estoque.empty and lote in arquivo_estoque['lote'].values:    
                print("Lote já existe!")

            else:
                
                novo_lote = {'nome': [selecionado],
                             "lote": [lote], 
                             "quantidade": [quantidade],
                             "validade": [validade], 
                             "fornecedor": [fornecedor],
                                }
                novo_lote = pandas.DataFrame(novo_lote)

                if arquivo_estoque.empty:
                    novo_lote.to_csv(self.caminho_arquivo_estoque, index=False, mode="a")
                else:
                    novo_lote.to_csv(self.caminho_arquivo_estoque, index=False, mode="a", header=False)

        else:
            print("Sem medicamentos registrados!")
       
    

adiministrar_medicamento = AdmMedicamentos()
adiministrar_medicamento.cadastrar_medicamento("remedio", "ingerir", "200ml", "tomar")
adiministrar_medicamento.cadastrar_medicamento("remedio", "ingerir", "200ml", "tomar")
adiministrar_medicamento.cadastrar_medicamento("remedio", "ingerir", "200ml", "tomar")
adiministrar_medicamento.cadastrar_medicamento("remedio 2", "ingerir 2", "200ml 2", "tomar 2")

adiministrar_medicamento.registrar_lote('253255', 4365, '14/03/2024', 'NEUXFJ')
adiministrar_medicamento.registrar_lote('253255', 4365, '14/03/2024', 'NEUXFJ')
adiministrar_medicamento.registrar_lote('435636', 65, '14/07/2025', 'FEWFJ')
adiministrar_medicamento.registrar_lote('789655', 465, '24/03/2024', 'REWBS')