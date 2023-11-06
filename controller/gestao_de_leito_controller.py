import inquirer
from colorama import init, Fore, Style
from model.gestao_leito import SistemaGestaoLeitos

init()
cor_mensagem_erro = Fore.RED

modulo_gestao_leito = SistemaGestaoLeitos()

def run():
    while True:
        perguntas = [
            inquirer.List('opcao',
                          message='Selecione o que deseja fazer',
                          choices=[
                              ('1 - Monitorar leitos', '1'),
                              ('2 - Visualizar Histórico', '2'),
                              ('3 - Sair', '3') 
                          ])
        ]

        respostas = inquirer.prompt(perguntas)

        if respostas is None:
            raise KeyboardInterrupt
        
        opcao = respostas['opcao']

        if opcao == '1':
            modulo_gestao_leito.monitorar_leitos()

        elif opcao == '2':
            modulo_gestao_leito.imprimir_historico()

        elif opcao == '3':
            break
