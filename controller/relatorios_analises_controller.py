import inquirer
from model.relatorios_analises import RelatorioAnalise
from model.cadastro_paciente import SistemaHospital
from model.gestao_leito import SistemaGestaoLeitos
from colorama import init, Fore, Style

init()
cor_mensagem_erro = Fore.RED

modulo_relatorio  = RelatorioAnalise()
modulo_paciente = SistemaHospital()
modulo_leitos = SistemaGestaoLeitos()

def run():
    while True:
        perguntas = [
            inquirer.List('opcao',
                          message='Selecione o que deseja fazer',
                          choices=[
                              ('1 - Gerar_reatorio_txt', '1'),
                              ('2 - Gerar_relatorio_csv', '2'),
                              ('3 - Métricas de ocupação', '3'),
                              ('4 - Relatório de uso de medicamentos', '4'),
                              ('5 - Sair do módulo', '5')
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
                inquirer.List('nota1', message='Digite eficiência de UTI', choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                inquirer.List('nota1', message='Digite eficiendia do hospital', choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            ]
            respostas_registro = inquirer.prompt(perguntas_registro)

            nota1 = respostas_registro['nota1']
            nota2 = respostas_registro['nota2']
        
     
            modulo_relatorio.gerar_relatorio_txt(nota1, nota2)
        
        if opcao == '2':

            perguntas_registro = [
                inquirer.List('nota1', message='Digite eficiência de UTI', choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                inquirer.List('nota1', message='Digite eficiendia do hospital', choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            ]
            respostas_registro = inquirer.prompt(perguntas_registro)

            nota1 = respostas_registro['nota1']
            nota2 = respostas_registro['nota2']
        
     
            modulo_relatorio.gerar_relatorio_csv(nota1, nota2)
            
        elif opcao == '3':
        
            modulo_leitos = imprimir_historico()  
            
        elif opcao == '4':

            modulo_relatorio.eficiencia_uso_equipamentos()
        
        elif opcao == '5':
            
            modulo_paciente.listar_pacientes_e_prontuarios(input("Nome: "))
        
        elif opcao == '6':
            print('Saindo do módulo de agendamento de visitas...')
            break