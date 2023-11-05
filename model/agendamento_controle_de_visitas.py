import os
import pandas
import time

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
        
        if horario in restricoes.columns.astype(str).to_list():
            print("\nEste horário está restrito!")

        else:
            if not agenda.empty and nome_paciente in agenda['nome'].astype(str).to_list():
                if agenda[agenda["nome"] == nome_paciente]['data'].values[0] and agenda[agenda["nome"] == nome_paciente]['horario'].values[0]:
                    print("Horário indisponível")
                
            else:
                print('\npode agendar')
                paciente = pandas.DataFrame({'nome': [nome_paciente], 'data': [data], 'horario': [horario]})

                if agenda.empty:
                    paciente.to_csv(self.caminho_arquivo_agenda, index=False, mode="a")
                else:
                    paciente.to_csv(self.caminho_arquivo_agenda, index=False, mode="a", header=False)
       
    def restringir_visitas(self, visitantes_por_paciente, duracao_maxima, horario_restrito):
        restricoes = pandas.read_csv(self.caminho_arquivo_restricoes)

        restricoes['max de visitantes'] = [visitantes_por_paciente]
        restricoes['duracao_maxima'] = [duracao_maxima]
   
        if horario_restrito not in restricoes.columns.astype(str).to_list():
           restricoes[horario_restrito] = 'restrito'
        else:
            print('\nEste horário já está restrito')

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

        if not arquivo_acesso.empty and  identificacao in arquivo_acesso['identificacao_visitante'].astype(str).to_csv(index=False) and nome_paciente in arquivo_acesso['nome_paciente'].astype(str).to_csv(index=False):
            print("\nVisitante com restrição!")
        else:
            novo_registro = pandas.DataFrame({'nome_visitante': [nome_visitante], 'identificacao': [identificacao], 'relacao_com_paciente': [relacao_com_paciente], 'nome_paciente': [nome_paciente]})

            if arquivo_visitantes.empty:
                novo_registro.to_csv(self.caminho_arquivo_visitantes, index=False, mode="a")
            else:
                novo_registro.to_csv(self.caminho_arquivo_visitantes, index=False, mode="a", header=False)
    
    def controlar_acesso(self, identificacao_visitante, nome_paciente):
        try:
            arquivo_acesso = pandas.read_csv(self.caminho_arquivo_acesso)
        except:
            arquivo_acesso = pandas.DataFrame()
    
        if not arquivo_acesso.empty and identificacao_visitante in arquivo_acesso['identificacao_visitante'].astype(str).to_csv(index=False) and nome_paciente in arquivo_acesso['nome_paciente'].astype(str).to_csv(index=False):
            print("\nVisitante já cadastrado!")
        else:
            novo_controle = pandas.DataFrame({'identificacao_visitante': [identificacao_visitante], 'nome_paciente': [nome_paciente]})

            if arquivo_acesso.empty:
                novo_controle.to_csv(self.caminho_arquivo_acesso, index=False, mode="a")
            else:
                novo_controle.to_csv(self.caminho_arquivo_acesso, index=False, mode="a", header=False)
    
    def notificar_visita(self):

        tempo_atual = time.localtime()
        ano = tempo_atual.tm_year
        mes = tempo_atual.tm_mon
        dia = tempo_atual.tm_mday

        print(f"\nVisita Marcada para amanhã: {ano}-{mes}-{dia}")
    
    def cancelar_visita(self):
        pass
    
    def reagendar_visita(self):
        pass

agenda = AgendamentoControleVisitas()

agenda.agendar_visita('joao', '4', '15')
agenda.agendar_visita('julia', '16', '5')
agenda.agendar_visita('jose', '4', '19')
agenda.agendar_visita('jonas', '28', '22')
agenda.agendar_visita('jamile', '1', '3')

agenda.restringir_visitas('2', '15', '13')
agenda.restringir_visitas('3', '20', '14')
agenda.restringir_visitas('2', '25', '14')

agenda.registrar_visitante('carlos', '54342632', 'amigo', 'jose')
agenda.registrar_visitante('isadora', '92658651', 'amiga', 'joao')

agenda.controlar_acesso('54342632', 'jose')
agenda.controlar_acesso('92658651', 'ana')

agenda.notificar_visita()