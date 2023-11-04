import os
import pandas

class AgendamentoControleVisitas:
    def __init__(self):
        self.caminho_arquivo_restricoes = "database/restricoes_de_visitas.csv"
        self.caminho_arquivo_visitantes = "database/registo_de_visitantes.csv"

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
    
    def agendar_visita(self, nome_paciente, data, horario):
        caminho_arquivo_agenda = f"database/agenda_de_visitas_{nome_paciente}.csv"

        if not os.path.exists(caminho_arquivo_agenda):
            estrutura = [
                [True] * 24 for i in range(30)
                ]
            arquivo = pandas.DataFrame(estrutura)
            arquivo.to_csv(caminho_arquivo_agenda, index=False)

        agenda = pandas.read_csv(caminho_arquivo_agenda)
        restricoes = pandas.read_csv(self.caminho_arquivo_restricoes)

        if agenda.iloc[int(data)].iloc[int(horario)] == True:
            if horario in restricoes.columns.astype(str).to_list():
                print("\nEste horário está restrito!")
            else:
                print('\npode agendar')
                agenda.iloc[data].iloc[horario] = False 
                agenda.to_csv(caminho_arquivo_agenda, index=False)
        else:
            print("Não foi possível agendar! Horário indisponível!")
        
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
        
        novo_registro = pandas.DataFrame({'nome_visitante': [nome_visitante], 'identificacao': [identificacao], 'relacao_com_paciente': [relacao_com_paciente], 'nome_paciente': [nome_paciente]})

        if arquivo_visitantes.empty:
            novo_registro.to_csv(self.caminho_arquivo_visitantes, index=False, mode="a")
        else:
            novo_registro.to_csv(self.caminho_arquivo_visitantes, index=False, mode="a", header=False)

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