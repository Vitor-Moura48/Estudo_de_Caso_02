import pandas
import os
import json

class AdmMedicamentos:
    def __init__(self):

        # inicializando os arquivos, caso não tenham sido
        self.caminho_arquivo_medicamentos = "database/medicamentos.csv"
        self.caminho_arquivo_registro = "database/registro_de_lote_medicamentos.csv"
        self.caminho_arquivo_estoque = "database/estoque_de_medicamentos.csv"

        if not os.path.exists(self.caminho_arquivo_medicamentos):
            arquivo = pandas.DataFrame()
            arquivo.to_csv(self.caminho_arquivo_medicamentos, index=False)
        if not os.path.exists(self.caminho_arquivo_registro):
            arquivo = pandas.DataFrame()
            arquivo.to_csv(self.caminho_arquivo_registro, index=False) 
        if not os.path.exists(self.caminho_arquivo_estoque):
            estrutura = {
                'inicialização':0
            }
            arquivo = pandas.DataFrame(estrutura, index=[0])
            arquivo.to_csv(self.caminho_arquivo_estoque, index=False, index_label=None) 
          
    def cadastrar_medicamento(self, nome, principio_ativo, dosagem, forma_adiministracao):
        try:
            arquivo = pandas.read_csv(self.caminho_arquivo_medicamentos)
        except:
            arquivo = pandas.DataFrame()
        
        try:
            arquivo_estoque = pandas.read_csv(self.caminho_arquivo_estoque)
        except:
            arquivo_estoque = pandas.DataFrame({})
       
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
                arquivo_estoque.pop('inicialização')
            else:
                novo_medicamento.to_csv(self.caminho_arquivo_medicamentos, index=False, mode="a", header=False)
            
            # adiciona o medicamento no arquivo de estoque
            arquivo_estoque[nome] = 0
            arquivo_estoque.to_csv(self.caminho_arquivo_estoque, index=False)

    def registrar_lote(self, lote, quantidade, validade, fornecedor):
        try:
            arquivo = pandas.read_csv(self.caminho_arquivo_medicamentos)
        except:
            arquivo = pandas.DataFrame()

        try:
            arquivo_registro = pandas.read_csv(self.caminho_arquivo_registro)
        except:
            arquivo_registro = pandas.DataFrame()
        
        try:
            arquivo_estoque = pandas.read_csv(self.caminho_arquivo_estoque)
        except:
            arquivo_estoque = pandas.DataFrame()

        # se houver algum medicamento cadastrado
        if not arquivo.empty:

            print("\nSelecione o medicamento: ")
            for medicamento in arquivo['nome'].values:
                print(medicamento)

            selecionado = input("medicamento: ")
            # se o registro não estiver vazio e o lote já foi ragistrado
            if not arquivo_registro.empty and lote in arquivo_registro['lote'].astype(str).to_list():    
                print("\nLote já existe!")

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
                if arquivo_registro.empty:
                    novo_lote.to_csv(self.caminho_arquivo_registro, index=False, mode="a")
                else:
                    novo_lote.to_csv(self.caminho_arquivo_registro, index=False, mode="a", header=False)
                
                # adiciona a quantidade no arquivo de estoque
                arquivo_estoque[selecionado] += quantidade
                arquivo_estoque.to_csv(self.caminho_arquivo_estoque, index=False)

        else:
            print("\nSem medicamentos registrados!")
    
    def alerta(self, nome, quantidade):
        print(f"\n{nome}: Estoque baixo, {quantidade}!")
    
    def rastrear_lotes(self, lote):
        try:
            arquivo_registro = pandas.read_csv(self.caminho_arquivo_registro)
        except:
            arquivo_registro = pandas.DataFrame()
        
        if not arquivo_registro.empty:
            if lote in arquivo_registro['lote'].astype(str).to_list():
                print('\nencontrado:')
                print(arquivo_registro.loc[arquivo_registro['lote'].astype(str) == lote].to_csv(index=False))
            else:
                print("\nLote não encontrado, registro de todos os lotes:")
                print(arquivo_registro.to_csv(index=False))
        else:
            print("\nRegistro de lotes vazio!")
            
    
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

adiministrar_medicamento.rastrear_lotes('253255')
adiministrar_medicamento.rastrear_lotes('963635')