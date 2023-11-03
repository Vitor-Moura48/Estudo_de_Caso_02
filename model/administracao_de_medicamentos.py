import pandas
import os
import json

class AdmMedicamentos:
    def __init__(self):

        # inicializando os arquivos, caso não tenham sido
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
       
        # se o arquivo não estiver vazio e o nome não estiver ne lista já registrada
        if not arquivo.empty and nome in arquivo['nome'].values:    
            print("Medicamento já cadastrado!!")
        # adiciona o nome junto com os dados
        else:
            novo_medicamento = {'nome': [nome],
                                "principio_ativo": [principio_ativo], 
                                "dosagem": [dosagem], 
                                "forma_adiministracao": [forma_adiministracao],
                                }  
            novo_medicamento = pandas.DataFrame(novo_medicamento)

            # se estiver vazio, mantem o cabeçalho, se não, ignora
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

        # se houver algum medicamento cadastrado
        if not arquivo.empty:

            print("Selecione o medicamento: ")
            for medicamentos in arquivo['nome'].values:
                print(medicamentos)

            selecionado = input("medicamento: ")
            # se o registro não estiver vazio e o lote já foi ragistrado
            if not arquivo_estoque.empty and lote in arquivo_estoque['lote'].astype(str).to_list():    
                print("Lote já existe!")

            # adiciona o lote no arquivo de registro
            else: 
                novo_lote = {'nome': [selecionado],
                             "lote": [lote], 
                             "quantidade": [quantidade],
                             "validade": [validade], 
                             "fornecedor": [fornecedor],
                                }
                novo_lote = pandas.DataFrame(novo_lote)

                # mantem o cabeçalho caso seja o primeiro
                if arquivo_estoque.empty:
                    novo_lote.to_csv(self.caminho_arquivo_estoque, index=False, mode="a")
                else:
                    novo_lote.to_csv(self.caminho_arquivo_estoque, index=False, mode="a", header=False)

        else:
            print("Sem medicamentos registrados!")
       
    
# testando as funções
adiministrar_medicamento = AdmMedicamentos()
adiministrar_medicamento.cadastrar_medicamento("remedio", "ingerir", "200ml", "tomar")
adiministrar_medicamento.cadastrar_medicamento("remedio", "ingerir", "200ml", "tomar")
adiministrar_medicamento.cadastrar_medicamento("remedio", "ingerir", "200ml", "tomar")
adiministrar_medicamento.cadastrar_medicamento("remedio 2", "ingerir 2", "200ml 2", "tomar 2")

adiministrar_medicamento.registrar_lote('253255', 4365, '14/03/2024', 'NEUXFJ')
adiministrar_medicamento.registrar_lote('253255', 4365, '14/03/2024', 'NEUXFJ')
adiministrar_medicamento.registrar_lote('435636', 65, '14/07/2025', 'FEWFJ')
adiministrar_medicamento.registrar_lote('789655', 465, '24/03/2024', 'REWBS')