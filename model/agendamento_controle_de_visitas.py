import os
import pandas
import time
from colorama import init, Fore, Style

init()
cor_mensagem_erro = Fore.RED
cor_verde = Fore.GREEN

class AgendamentoControleVisitas:
    def __init__(self):
        self.caminho_arquivo_agenda = "database/agenda_de_visitas.csv"
        self.caminho_arquivo_restricoes = "database/restricoes_de_visitas.csv"
        self.caminho_arquivo_visitantes = "database/registo_de_visitantes.csv"
        self.caminho_arquivo_acesso = "database/controle_de_acesso_de_visitantes.csv"

        if not os.path.exists(self.caminho_arquivo_agenda):
            arquivo = pandas.DataFrame()
            arquivo.to_csv(self.caminho_arquivo_agenda, index=False)
        if not os.path.exists(self.caminho_arquivo_restricoes):
            estrutura = {
                'max de visitantes': [1],
                'duracao_maxima': [10],
            }
            arquivo = pandas.DataFrame(estrutura)
            arquivo.to_csv(self.caminho_arquivo_restricoes, index=False)
        if not os.path.exists(self.caminho_arquivo_visitantes):
            arquivo = pandas.DataFrame()
            arquivo.to_csv(self.caminho_arquivo_visitantes, index=False)
        if not os.path.exists(self.caminho_arquivo_acesso):
            arquivo = pandas.DataFrame()
            arquivo.to_csv(self.caminho_arquivo_acesso, index=False)
    
    def agendar_visita(self, nome_paciente, data, horario):
        try:
            agenda = pandas.read_csv(self.caminho_arquivo_agenda)
        except:
            agenda = pandas.DataFrame()

        restricoes = pandas.read_csv(self.caminho_arquivo_restricoes)

        try:
            arquivo_pacientes = pandas.read_csv("database/pacientes.csv")
        except:
            arquivo_pacientes = pandas.DataFrame()

        if nome_paciente in arquivo_pacientes['Nome'].astype(str).to_list():
        
            # confere se o horário selecionado está restrito
            if horario in restricoes.columns.astype(str).to_list():
                print(f"\n{cor_mensagem_erro}Este horário está restrito!{Style.RESET_ALL}\n")

            # se não estiver, agenda a visita
            else:
                # se já houver visita naquele horario para o paciente, não pode agendar
                if not agenda.empty and nome_paciente in agenda['nome'].astype(str).to_list():
                    if str(agenda[agenda["nome"] == nome_paciente]['data'].values[0]) == data and str(agenda[agenda["nome"] == nome_paciente]['horario'].values[0]) == horario:
                        print(f"\n{cor_mensagem_erro}Horário indisponível{Style.RESET_ALL}\n")
                
                # se estiver disponível, agenda normalmente
                else:
                    print(f'\n{cor_verde}Agendando...{Style.RESET_ALL}\n')
                    paciente = pandas.DataFrame({'nome': [nome_paciente], 'data': [data], 'horario': [horario]})

                    if agenda.empty:
                        paciente.to_csv(self.caminho_arquivo_agenda, index=False, mode="a")
                    else:
                        paciente.to_csv(self.caminho_arquivo_agenda, index=False, mode="a", header=False)

        else:
            print(f"\n{cor_mensagem_erro}Paciente não encontrado{Style.RESET_ALL}\n")
       
    def restringir_visitas(self, visitantes_por_paciente, duracao_maxima, horario_restrito):
        restricoes = pandas.read_csv(self.caminho_arquivo_restricoes)

        # altera os dados de acordo com os argumentos
        restricoes['max de visitantes'] = [visitantes_por_paciente]
        restricoes['duracao_maxima'] = [duracao_maxima]
   
        # adiciona uma coluna restringindo a hora selecionada
        if horario_restrito not in restricoes.columns.astype(str).to_list():
           restricoes[horario_restrito] = 'restrito'
        # se aquela hora já estava restrita, apenas manda uma mensagem
        else:
            print(f'\n{cor_mensagem_erro}Este horário já está restrito{Style.RESET_ALL}\n')

        restricoes.to_csv(self.caminho_arquivo_restricoes, index=False)
    
    def registrar_visitante(self, nome_visitante, identificacao, relacao_com_paciente, nome_paciente):
        try:
            arquivo_visitantes = pandas.read_csv(self.caminho_arquivo_visitantes)
        except:
            arquivo_visitantes = pandas.DataFrame()

        try:
            arquivo_acesso = pandas.read_csv(self.caminho_arquivo_acesso)
        except:
            arquivo_acesso = pandas.DataFrame()
        
        try:
            arquivo_pacientes = pandas.read_csv("database/pacientes.csv")
        except:
            arquivo_pacientes = pandas.DataFrame()

        if nome_paciente in arquivo_pacientes['Nome'].astype(str).to_list():

            # confere se aquele visitante está com acesso restrito ao paciente
            if not arquivo_acesso.empty and  identificacao in arquivo_acesso['identificacao_visitante'].astype(str).to_csv(index=False) and nome_paciente in arquivo_acesso['nome_paciente'].astype(str).to_csv(index=False):
                print(f"\n{cor_mensagem_erro}Visitante com restrição!{Style.RESET_ALL}\n")

            # se não estiver, cria um registro do visitante
            else:
                # verifica se já existe um registro igual, se não houver, cria o registro
                if arquivo_visitantes.empty or arquivo_visitantes[(arquivo_visitantes['identificacao'] == int(identificacao)) & (arquivo_visitantes['nome_paciente'] == nome_paciente)].empty:

                    print(f'\n{cor_verde}registrando visitante...{Style.RESET_ALL}\n')
                    novo_registro = pandas.DataFrame({'nome_visitante': [nome_visitante], 'identificacao': [identificacao], 'relacao_com_paciente': [relacao_com_paciente], 'nome_paciente': [nome_paciente]})
                    if arquivo_visitantes.empty:
                        novo_registro.to_csv(self.caminho_arquivo_visitantes, index=False, mode="a")
                    else:
                        novo_registro.to_csv(self.caminho_arquivo_visitantes, index=False, mode="a", header=False)
                # se já houver, não cria outro
                else:
                    print(f"\n{cor_mensagem_erro}Visitante já registrado com esse paciente{Style.RESET_ALL}\n")
        
        else:
            print(f"\n{cor_mensagem_erro}Paciente não encontrado{Style.RESET_ALL}\n")
    
    def controlar_acesso(self, identificacao_visitante, nome_paciente):
        try:
            arquivo_acesso = pandas.read_csv(self.caminho_arquivo_acesso)
        except:
            arquivo_acesso = pandas.DataFrame()
        
        try:
            arquivo_pacientes = pandas.read_csv("database/pacientes.csv")
        except:
            arquivo_pacientes = pandas.DataFrame()

        if nome_paciente in arquivo_pacientes['Nome'].astype(str).to_list():
    
            # se o visitande já estiver restrito para aquele paciente, apenas printa uam mensagem
            if not arquivo_acesso.empty and identificacao_visitante in arquivo_acesso['identificacao_visitante'].astype(str).to_csv(index=False) and nome_paciente in arquivo_acesso['nome_paciente'].astype(str).to_csv(index=False):
                print(f"\n{cor_mensagem_erro}Visitante já está restrito!{Style.RESET_ALL}\n")
            # se não, adiciona aquele visitante como restrito para o paciente do argumento
            else:
                novo_controle = pandas.DataFrame({'identificacao_visitante': [identificacao_visitante], 'nome_paciente': [nome_paciente]})

                if arquivo_acesso.empty:
                    novo_controle.to_csv(self.caminho_arquivo_acesso, index=False, mode="a")
                else:
                    novo_controle.to_csv(self.caminho_arquivo_acesso, index=False, mode="a", header=False)

        else:
            print(f"\n{cor_mensagem_erro}Paciente não encontrado{Style.RESET_ALL}\n")
    
    def notificar_visita(self):

        # (deve ser chamada por outra função), printa a data do dia de amanhã. Deve ser chamada quando faltar um dia para uma determinada visita
        tempo_atual = time.localtime()
        ano = tempo_atual.tm_year
        mes = tempo_atual.tm_mon
        dia = tempo_atual.tm_mday

        print(f'\n{cor_verde}Visita Marcada para amanhã: {ano}-{mes}-{dia}{Style.RESET_ALL}\n')
    
    def cancelar_visita(self, nome_paciente, data, horario):
        try:
            agenda = pandas.read_csv(self.caminho_arquivo_agenda)
        except:
            agenda = pandas.DataFrame()

        # se aquele paciente estiver no registro:
        if not agenda.empty and nome_paciente in agenda['nome'].astype(str).to_list():

            # confere se a visita naquela data e horário estão no registro, se estiver, remove
            if str(agenda[agenda["nome"] == nome_paciente]['data'].values[0]) == data and str(agenda[agenda["nome"] == nome_paciente]['horario'].values[0]) == horario:

                print(f'\n{cor_verde}Removendo...{Style.RESET_ALL}\n')
                indice = agenda[(agenda["nome"] == nome_paciente) & (agenda["data"] == int(data)) & (agenda['horario'] == int(horario))].index[0]
                agenda.drop(indice, inplace=True)
                agenda.to_csv(self.caminho_arquivo_agenda, index=False)
            
            # se a visita não estiver, printa a informação
            else:
                print(f"\n{cor_mensagem_erro}Data/Horário não encontrados{Style.RESET_ALL}\n")

        # se o paciente não estiver no registro, apenas nofica a situação
        else:
            print(f"\n{cor_mensagem_erro}Paciente não encontrado{Style.RESET_ALL}\n")

    def reagendar_visita(self, nome_paciente, data, horario, nova_data, novo_horario):
        try:
            agenda = pandas.read_csv(self.caminho_arquivo_agenda)
        except:
            agenda = pandas.DataFrame()
        
        # confere se o paciente está na lista de registro
        if not agenda.empty and nome_paciente in agenda['nome'].astype(str).to_list():

            # se aquela data e horário estiverem na lista de registro, altera os dados com os argumentos passados
            if str(agenda[agenda["nome"] == nome_paciente]['data'].values[0]) == data and str(agenda[agenda["nome"] == nome_paciente]['horario'].values[0]) == horario:

                print(f"\n{cor_verde}Alterando...{Style.RESET_ALL}")
                indice = agenda[(agenda["nome"] == nome_paciente) & (agenda["data"] == int(data)) & (agenda['horario'] == int(horario))].index[0]
                agenda.loc[indice, ['data']] = [int(nova_data)]
                agenda.loc[indice, ['horario']] = [int(novo_horario)]
                agenda.to_csv(self.caminho_arquivo_agenda, index=False)

            # se não encontrar, notifica
            else:
                print(f"\n{cor_mensagem_erro}Data/Horário não encontrados{Style.RESET_ALL}\n")
            
        # se não estiver, notifica
        else:
            print(f"\n{cor_mensagem_erro}Paciente não encontrado{Style.RESET_ALL}\n")


# testando as funções
agenda = AgendamentoControleVisitas()

'''
# argumentos: nome do paciente, data, hora
agenda.agendar_visita('joao', '4', '15')
agenda.agendar_visita('julia', '16', '5')
agenda.agendar_visita('jose', '4', '19')
agenda.agendar_visita('jonas', '28', '22')
agenda.agendar_visita('jamile', '1', '3')

# argumentos máximo de visitantes por vez, tempo máximo de visita, horário para restringir
agenda.restringir_visitas('2', '15', '13')
agenda.restringir_visitas('3', '20', '14')
agenda.restringir_visitas('2', '25', '14')

# argumentos: nome do visitante, identificação do visitante, relação com paciente, nome do paciente
agenda.registrar_visitante('carlos', '54342632', 'amigo', 'jose')
agenda.registrar_visitante('isadora', '92658651', 'amiga', 'joao')

# argumentos: identificação do visitante, nome do paciente
agenda.controlar_acesso('54342632', 'jose')
agenda.controlar_acesso('92658651', 'ana')

agenda.notificar_visita()

# argumentos: nome do paciente, data, hora
agenda.cancelar_visita('julia', '16', '5')
agenda.cancelar_visita('julia', '6', '11')

# argumentos: nome do paciente, data, hora, nova data, nova hora
agenda.reagendar_visita('jonas', '28', '22', '14', '7')
'''