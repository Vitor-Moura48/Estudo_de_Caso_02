import inquirer
from model.administracao_de_medicamentos import AdmMedicamentos
from colorama import init, Fore, Style

init()
cor_mensagem_erro = Fore.RED

modulo_administacao_medicamentos =AdmMedicamentos()
def run():
    while True:
        perguntas = [
            inquirer.List('opcao',
                          message='Selecione o que deseja fazer',
                          choices=[
                              ('1 - Cadastrar medicamento', '1'),
                              ('2 - Registrar lote', '2'),
                              ('3 - Rastrear lote', '3'),
                              ('4 - Registrar administração', '4'),
                              ('5 - Informações de medicação', '5'),       
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
                inquirer.Text('nome', message='Digite o nome do medicamento'),
                inquirer.Text('principio ativo', message='Digite principio ativo'),
                inquirer.Text('dose', message='Dose do remédio'),
                inquirer.Text('instrucoes', message='Instruções de uso'),
            ]
            respostas_registro = inquirer.prompt(perguntas_registro)

            nome = respostas_registro['nome']
            principio_ativo = respostas_registro['principio ativo']
            dose = respostas_registro['dose']
            instrucoes = respostas_registro['instrucoes']

            modulo_administacao_medicamentos.cadastrar_medicamento(nome, principio_ativo, dose, instrucoes)

        elif opcao == '2':

            perguntas_registro = [
                inquirer.Text('numero', message='Digite o número de lote'),
                inquirer.Text('quantidade', message='Digite a quantidade do medicamento'),
                inquirer.Text('validade', message='Validade do medicamento'),
                inquirer.Text('fornecedor', message='Fornecedor'),
            ]
            respostas_registro = inquirer.prompt(perguntas_registro)
            
            numero = respostas_registro['numero']
            quantidade = respostas_registro['quantidade']
            validade = respostas_registro['validade']
            fornecedor = respostas_registro['fornecedor']

            modulo_administacao_medicamentos.registrar_lote(numero, quantidade, validade, fornecedor)
            
        elif opcao == '3':
            perguntas_registro = [
                inquirer.Text('numero', message='Digite o número de lote'),
            ]
            respostas_registro = inquirer.prompt(perguntas_registro)
            
            numero = respostas_registro['numero']

            modulo_administacao_medicamentos.rastrear_lotes(numero)
    
        elif opcao == '4':

            perguntas_registro = [
                inquirer.Text('nome', message='Digite o nome do medicamento'),
                inquirer.Text('data', message='Digite a data da aplicação'),
                inquirer.Text('horario', message='Digite o horario da aplicação'),
                inquirer.Text('paciente', message='Digite o nome do paciente'),
                inquirer.Text('dose', message='Digite a dose aplicada'),
                inquirer.Text('responsavel', message='Digite o nome do responsável'),
            ]
            respostas_registro = inquirer.prompt(perguntas_registro)
            
            nome = respostas_registro['nome']
            data = respostas_registro['data']
            horario = respostas_registro['horario']
            paciente = respostas_registro['paciente']
            dose = respostas_registro['dose']
            responsavel = respostas_registro['responsavel']

            modulo_administacao_medicamentos.registrar_administracao(nome, data, horario, paciente, dose, responsavel)
        
        elif opcao == '5':

            perguntas_registro = [
                inquirer.Text('nome', message='Digite o nome do medicamento'),
            ]
            respostas_registro = inquirer.prompt(perguntas_registro)
            
            nome = respostas_registro['nome']
            
            modulo_administacao_medicamentos.informacoes_de_medicacao(nome)