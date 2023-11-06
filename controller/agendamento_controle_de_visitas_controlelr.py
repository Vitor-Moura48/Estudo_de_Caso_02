import inquirer
from model.agendamento_controle_de_visitas import AgendamentoControleVisitas
from colorama import init, Fore, Style

init()
cor_mensagem_erro = Fore.RED

modulo_agendamento_visitas  = AgendamentoControleVisitas()
def run():
    while True:
        perguntas = [
            inquirer.List('opcao',
                          message='Selecione o que deseja fazer',
                          choices=[
                              ('1 - Agendar visita', '1'),
                              ('2 - Restringir visita', '2'),
                              ('3 - Registrar visita', '3'),
                              ('4 - Controloar visita', '4'),
                              ('5 - Cancelar visita', '5'),       
                              ('6 - Reagendar_visita', '6'), 
                          ])
        ]

        respostas = inquirer.prompt(perguntas)

        # Verifique se as respostas são nulas
        if respostas is None:
            raise KeyboardInterrupt
        
        opcao = respostas['opcao']

        # Aqui temos uma estrutura de decisão para cada opção do menu
        if opcao == '1':

            perguntas_registro = [
                inquirer.Text('nome', message='Digite o nome do paciente'),
                inquirer.Text('data', message='Digite data da visita'),
                inquirer.Text('hora', message='Digite a hora da visita'),
            ]
            respostas_registro = inquirer.prompt(perguntas_registro)

            nome = respostas_registro['nome']
            data = respostas_registro['data']
            hora = respostas_registro['hora']
        
            modulo_agendamento_visitas.agendar_visita(nome, data, hora)

        elif opcao == '2':

            perguntas_registro = [
                inquirer.Text('visitantes_max', message='Digite o número máximo de visitantes'),
                inquirer.Text('tempo_max', message='Digite tempo máximo por visita'),
                inquirer.Text('horario_paara_restringir', message='Digite um horário para restringir'),
            ]
            respostas_registro = inquirer.prompt(perguntas_registro)
            
            visitantes_max = respostas_registro['visitantes_max']
            tempo_max = respostas_registro['tempo_max']
            horario_para_restringir = respostas_registro['horario_para_restringir']
            
            modulo_agendamento_visitas.restringir_visitas(visitantes_max, tempo_max, horario_para_restringir)
            
        elif opcao == '3':
            perguntas_registro = [
                inquirer.Text('nome_visitante', message='Digite o nome do visitante'),
                inquirer.Text('identificacao_visitante', message='Digite a identificação do visitante'),
                inquirer.Text('relacao_com_paciente', message='Digite a relação do visitante com o paciente'),
                inquirer.Text('nome_paciente', message='Digite o nome do paciente'),
            ]
            respostas_registro = inquirer.prompt(perguntas_registro)
            
            nome_visitante = respostas_registro['nome_visitante']
            identificacao_visitante = respostas_registro['identificacao_visitante']
            relacao_com_paciente = respostas_registro['relacao_com_paciente']
            nome_paciente = respostas_registro['numnome_pacienteero']

            modulo_agendamento_visitas.registrar_visitante(nome_visitante, identificacao_visitante, relacao_com_paciente, nome_paciente)
    
        elif opcao == '4':

            perguntas_registro = [
                inquirer.Text('identificacao_visitante', message='Digite a identificação do paciente'),
                inquirer.Text('nome_paciente', message='Digite o nome do paciente')
            ]
            respostas_registro = inquirer.prompt(perguntas_registro)
            
            identificacao_visitante = respostas_registro['identificacao_visitante']
            nome_paciente = respostas_registro['nome_paciente']
          
            modulo_agendamento_visitas.controlar_acesso(identificacao_visitante, nome_paciente)
        
        elif opcao == '5':

            perguntas_registro = [
                inquirer.Text('nome', message='Digite o nome do paciente'),
                inquirer.Text('data', message='Digite a data da visita'),
                inquirer.Text('hora', message='Digite a hora da visita')
            ]
            respostas_registro = inquirer.prompt(perguntas_registro)
            
            nome = respostas_registro['nome']
            data = respostas_registro['data']
            hora = respostas_registro['hora']
            
            modulo_agendamento_visitas.cancelar_visita(nome, data, hora)
        
        elif opcao == '6':

            perguntas_registro = [
                inquirer.Text('nome', message='Digite o nome do paciente'),
                inquirer.Text('data', message='Digite a data da visita'),
                inquirer.Text('hora', message='Digite a hora da visita'),
                inquirer.Text('nova_data', message='Digite a data da nova visita'),
                inquirer.Text('nova_hora', message='Digite a hora da nova visita')
            ]
            respostas_registro = inquirer.prompt(perguntas_registro)
            
            nome = respostas_registro['nome']
            data = respostas_registro['data']
            hora = respostas_registro['hora']
            nova_data = respostas_registro['nova_data']
            nova_hora = respostas_registro['nova_hora']
            
            modulo_agendamento_visitas.reagendar_visita(nome, data, hora, nova_data, nova_hora)