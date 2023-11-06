import pandas
import os
from colorama import init, Fore, Style

init()
cor_mensagem_erro = Fore.RED
cor_verde = Fore.GREEN

class AdmMedicamentos:
    def __init__(self):

        # inicializando os arquivos, caso não tenham sido
        self.caminho_arquivo_medicamentos = "database/medicamentos.csv"
        self.caminho_arquivo_registro_lotes = "database/registro_de_lote_medicamentos.csv"
        self.caminho_arquivo_estoque = "database/estoque_de_medicamentos.csv"
        self.caminho_arquivo_registro_administracao = "database/registro_de_administracao.csv"

        if not os.path.exists(self.caminho_arquivo_medicamentos):
            arquivo = pandas.DataFrame()
            arquivo.to_csv(self.caminho_arquivo_medicamentos, index=False)
        if not os.path.exists(self.caminho_arquivo_registro_lotes):
            arquivo = pandas.DataFrame()
            arquivo.to_csv(self.caminho_arquivo_registro_lotes, index=False) 
        if not os.path.exists(self.caminho_arquivo_estoque):
            estrutura = {
                'inicialização':0
            }
            arquivo = pandas.DataFrame(estrutura, index=[0])
            arquivo.to_csv(self.caminho_arquivo_estoque, index=False, index_label=None) 
        if not os.path.exists(self.caminho_arquivo_registro_administracao):
            arquivo = pandas.DataFrame()
            arquivo.to_csv(self.caminho_arquivo_registro_administracao, index=False) 
          
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
            print(f"\n{cor_mensagem_erro}Medicamento já cadastrado!!{Style.RESET_ALL}\n")
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
            arquivo_registro = pandas.read_csv(self.caminho_arquivo_registro_lotes)
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
            # se o registro não estiver vazio e o lote já foi registrado
            if not arquivo_registro.empty and lote in arquivo_registro['lote'].astype(str).to_list():    
                print(f"\n{cor_mensagem_erro}Lote já existe!{Style.RESET_ALL}\n")

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
                    novo_lote.to_csv(self.caminho_arquivo_registro_lotes, index=False, mode="a")
                else:
                    novo_lote.to_csv(self.caminho_arquivo_registro_lotes, index=False, mode="a", header=False)
                
                # adiciona a quantidade no arquivo de estoque
                arquivo_estoque[selecionado] += int(quantidade)
                arquivo_estoque.to_csv(self.caminho_arquivo_estoque, index=False)

        else:
            print(f"\n{cor_mensagem_erro}Sem medicamentos registrados!{Style.RESET_ALL}\n")
    
    def alerta(self, nome, quantidade):
        print(f"\n{cor_mensagem_erro}{nome} -- Estoque baixo: {quantidade}!{Style.RESET_ALL}\n")
    
    def rastrear_lotes(self, lote):
        try:
            arquivo_registro = pandas.read_csv(self.caminho_arquivo_registro_lotes)
        except:
            arquivo_registro = pandas.DataFrame()
        
        if not arquivo_registro.empty:
            # se o lote for encontrado, printa as informações
            if lote in arquivo_registro['lote'].astype(str).to_list():
                print(f'\n{cor_verde}encontrado:')
                print(f"{arquivo_registro.loc[arquivo_registro['lote'].astype(str) == lote].to_csv(index=False)}\n")
                print(Style.RESET_ALL)
            # se não for encontrado, printa todos os lotes
            else:
                print(f"\n{cor_mensagem_erro}Lote não encontrado, registro de todos os lotes:{Style.RESET_ALL}\n")
                print(arquivo_registro.to_csv(index=False))
        else:
            print(f"\n{cor_mensagem_erro}Registro de lotes vazio!{Style.RESET_ALL}\n")
    
    def registrar_administracao(self, nome, data, horario, paciente, dosagem, responsavel):
        try:
            arquivo_estoque = pandas.read_csv(self.caminho_arquivo_estoque)
        except:
            arquivo_estoque = pandas.DataFrame({})

        try:
            arquivo_registro_adiministracao = pandas.read_csv(self.caminho_arquivo_registro_administracao)
        except:
            arquivo_registro_adiministracao = pandas.DataFrame({})

        # subtrai o medicamento no arquivo de estoque
        if arquivo_estoque[nome][0] > 0:
            arquivo_estoque[nome] -= 1
            arquivo_estoque.to_csv(self.caminho_arquivo_estoque, index=False)

            novo_registro = pandas.DataFrame({'nome': [nome], 'data': [data], 'horario': [horario], 'paciente': [paciente], 'dosagem': [dosagem], 'responsavel': [responsavel]})

            if arquivo_registro_adiministracao.empty:
                novo_registro.to_csv(self.caminho_arquivo_registro_administracao, index=False, mode="a")
            else:
                novo_registro.to_csv(self.caminho_arquivo_registro_administracao, index=False, mode="a", header=False)

            if arquivo_estoque[nome][0] < 10:
                self.alerta(nome, arquivo_estoque[nome][0])
        else:
            print(f"\n{cor_mensagem_erro}Medicamento indisponível! Fora de estoque!{Style.RESET_ALL}\n")
    
    def informacoes_de_medicacao(self, nome):
        try:
            arquivo = pandas.read_csv(self.caminho_arquivo_medicamentos)
        except:
            arquivo = pandas.DataFrame()
       
        # se o arquivo não estiver vazio e o nome não estiver na lista já registrada
        if not arquivo.empty:    
            if nome in arquivo['nome'].astype(str).to_csv():
               print(f"\n{cor_verde}{arquivo.loc[arquivo['nome'].astype(str) == nome].to_csv(index=False)}{Style.RESET_ALL}")
            else:
               print(f"\n{cor_mensagem_erro}Medicamento não encontrado!{Style.RESET_ALL}\n")
        else:
            print(f"\n{cor_mensagem_erro}Não há medicamentos para serem consultados{Style.RESET_ALL}\n")
    
            
    
# # testando as funções
# adiministrar_medicamento = AdmMedicamentos()

# # argumentos: nome do remedio, principio ativo, dose do remedio, instruções de uso
# adiministrar_medicamento.cadastrar_medicamento("remedio", "ingerir", "200ml", "tomar")
# adiministrar_medicamento.cadastrar_medicamento("remedio", "ingerir", "200ml", "tomar")
# adiministrar_medicamento.cadastrar_medicamento("remedio", "ingerir", "200ml", "tomar")
# adiministrar_medicamento.cadastrar_medicamento("remedio 2", "ingerir 2", "200ml 2", "tomar 2")

# # argumentos: número de lote, quantidade de medicamentos, data de validade, nome da fornecedora
# adiministrar_medicamento.registrar_lote('253255', 46, '14/03/2024', 'NEUXFJ')
# adiministrar_medicamento.registrar_lote('253255', 35, '14/03/2024', 'NEUXFJ')
# adiministrar_medicamento.registrar_lote('435636', 65, '14/07/2025', 'FEWFJ')
# adiministrar_medicamento.registrar_lote('789655', 465, '24/03/2024', 'REWBS')

# # argumentos: número de lote
# adiministrar_medicamento.rastrear_lotes('253255')
# adiministrar_medicamento.rastrear_lotes('963635')

# # argumentos: nome do remédio, data da aplicação, horário da aplicação, nome do paciente, dose aplicada, nome do responsável
# adiministrar_medicamento.registrar_administracao('remedio', '04/11/2023', '12:00', 'rafael', '500ml', 'otton')
# adiministrar_medicamento.registrar_administracao('remedio 2', '04/11/2023', '15:00', 'otton', '350ml', 'rafael')

# # argumentos: nome do remédio
# adiministrar_medicamento.informacoes_de_medicacao('remedio')
# adiministrar_medicamento.informacoes_de_medicacao('ergvefdg')