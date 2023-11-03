import pandas
import os
import json

class AdmMedicamentos:
    def __init__(self):
        self.caminho_arquivo_medicamentos = "suri/database/medicamentos.csv"

        if not os.path.exists(self.caminho_arquivo_medicamentos):
            arquivo = pandas.DataFrame()
            arquivo.to_csv(self.caminho_arquivo_medicamentos, index=False)
          
    def cadastrar_medicamento(self, nome, principio_ativo, dosagem, forma_adiministracao, lote, quantidade, validade, fornecedor):
        try:
            arquivo = pandas.read_csv(self.caminho_arquivo_medicamentos)
        except:
            arquivo = pandas.DataFrame()
        
        arquivo = arquivo.to_dict()
        
        
        if nome in arquivo:
            if lote in arquivo[nome]:
                print("tudo encontrado!!")
            else: 
                print("nome encontrado, lote não")
        else:
            novo_medicamento = {"principio_ativo": principio_ativo, 
                             "dosagem": dosagem, 
                             "forma_adiministracao": forma_adiministracao,
                             "lotes": {lote: [quantidade, validade, fornecedor]}}
            
            novo_medicamento = pandas.DataFrame(novo_medicamento)
            arquivo = pandas.DataFrame(arquivo)
            novo_medicamento.to_csv(self.caminho_arquivo_medicamentos, index=False, mode="a")

            print("nada encontrado")

        
        
    

        

        

        

adiministrar_medicamento = AdmMedicamentos()
adiministrar_medicamento.cadastrar_medicamento("remedio", "ingerir", "200ml", "tomar", "654235485", 25, "14/07/2024", "GRFJE")
adiministrar_medicamento.cadastrar_medicamento("remedio", "ingerir", "200ml", "tomar", "654235485", 25, "14/07/2024", "GRFJE")
adiministrar_medicamento.cadastrar_medicamento("remedio", "ingerir", "200ml", "tomar", "123456789", 25, "14/07/2024", "GRFJE")
adiministrar_medicamento.cadastrar_medicamento("remedio 2", "ingerir 2", "200ml 2", "tomar 2", "643516345", 19, "21/02/2024", "KMWXU")