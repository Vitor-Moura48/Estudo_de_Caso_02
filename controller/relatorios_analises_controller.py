import inquirer
from model.relatorios_analises import RelatorioAnalise
from colorama import init, Fore, Style

init()
cor_mensagem_erro = Fore.RED

modulo_relatorio  = RelatorioAnalise()
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
        if opcao == '1' or opcao == '2':

            perguntas_registro = [
                inquirer.List('nota1', message='Digite eficiência de UTI', choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                inquirer.List('nota1', message='Digite eficiendia do hospital', choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            ]
            respostas_registro = inquirer.prompt(perguntas_registro)

            nota1 = respostas_registro['nota1']
            nota2 = respostas_registro['nota2']
        
            modulo_relatorio.gerar_relatorio_txt(nota1, nota2)
            
        elif opcao == '3':
        
            modulo_relatorio.metricas_de_ocupacao()
    
        elif opcao == '4':

            modulo_relatorio.eficiencei_uso_equipamentos()
        
        elif opcao == '5':
            print('Saindo do módulo de agendamento de visitas...')
            break