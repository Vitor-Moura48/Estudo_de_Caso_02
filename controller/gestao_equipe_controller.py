import inquirer
from model.gestao_equipe import GestaoEquipe
from colorama import init, Fore, Style

init()
cor_mensagem_erro = Fore.RED

modulo_gestao_equipe  = GestaoEquipe()
def run():
    while True:
        perguntas = [
            inquirer.List('opcao',
                          message='Selecione o que deseja fazer',
                          choices=[
                              ('1 - Adicionar profissional de saúde', '1'),
                              ('2 - Editar profissional', '2'),
                              ('3 - Registrar batimento de ponto', '3'),
                              ('4 - Sair do módulo', '4')
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
                inquirer.Text('nome', message='Digite o nome do profissional'),
                inquirer.Text('cargo', message='Digite o cargo'),
                inquirer.Text('experiencia', message='Digite a experiência do profissional(anos)'),
                inquirer.Text('dados', message='Digite dados para contato (Telefone)'),
                inquirer.List('competencia', 
                    message='Escolha a competencia',
                    choices=['Ruim', 'Media', 'Boa']),
                inquirer.List('inicio_turno', 
                    message='Escolha o inicio do turno',
                    choices=[6, 14, 22]),
                inquirer.List('fim_turno', 
                    message='Escolha o final do turno',
                    choices=[2, 6, 10, 14, 18, 22]),
                inquirer.Text('dias', message='Quais dias você trabalha? (Separados por vírgula)')

            ]
            respostas_registro = inquirer.prompt(perguntas_registro)

            nome = respostas_registro['nome']
            cargo = respostas_registro['cargo']
            experiencia = respostas_registro['experiencia']
            dados = respostas_registro['dados']
            competencia = respostas_registro['competencia']
            inicio_turno = respostas_registro['inicio_turno']
            fim_turno = respostas_registro['fim_turno']
            dias = respostas_registro['dias']
        
            modulo_gestao_equipe.cadastro_alocar_plantoes(nome, cargo, experiencia, dados, competencia, inicio_turno, fim_turno, dias) 
            modulo_gestao_equipe.criar_grupos_e_salvar()
        
        elif opcao == '2':
            perguntas_registro = [
                inquirer.Text('nome_profissional', message='Digite o nome do profissional'),
                inquirer.Text('nova_experiencia', message='Digite a experiência do profissional(anos)'),
                inquirer.Text('novo_dados', message='Digite dados para contato (Telefone)'),
                inquirer.List('nova_competencia', 
                    message='Escolha a nova competencia',
                    choices=['Ruim', 'Media', 'Boa']),
                inquirer.List('novo_inicio_turno', 
                    message='Escolha o novo inicio do turno',
                    choices=[6, 14, 22]),
                inquirer.List('novo_fim_turno', 
                    message='Escolha o novo final do turno',
                    choices=[2, 6, 10, 14, 18, 22]),
                inquirer.Text('novo_dias', message='Quais os novos dias que você trabalha? (Separados por vírgula)')

            ]
            respostas_registro = inquirer.prompt(perguntas_registro)

            nome_profissional = respostas_registro['nome_profissional']
            nova_experiencia = respostas_registro['nova_experiencia']
            novo_dados = respostas_registro['novo_dados']
            nova_competencia = respostas_registro['nova_competencia']
            novo_inicio_turno = respostas_registro['novo_inicio_turno']
            novo_fim_turno = respostas_registro['novo_fim_turno']
            novo_dias = respostas_registro['novo_dias']

            modulo_gestao_equipe.editar_profissional(nome_profissional, nova_experiencia, novo_dados, nova_competencia, novo_inicio_turno, novo_fim_turno, novo_dias)
            modulo_gestao_equipe.criar_grupos_e_salvar() 

        elif opcao == '3':
            perguntas_registro = [
                inquirer.Text('nome_prof', message='Digite o nome do profissional'),
                inquirer.Text('dia', message='Digite qual o dia (01,02,03...)'),
                inquirer.List('turno_inicio', 
                    message='Escolha o inicio do turno',
                    choices=[6, 14, 22]),
                inquirer.List('turno_fim', 
                    message='Escolha o final do turno',
                    choices=[2, 6, 10, 14, 18, 22]),
                inquirer.List('pausas', 
                    message='Escolha o tempo de pausa',
                    choices=[1, 1.30, 2, 2.30, 3, 3.30]),
                inquirer.List('horas_extras', 
                    message='Escolha o tempo de horas extras',
                    choices=[1, 1.30, 2, 2.30, 3, 3.30])

            ]
            respostas_registro = inquirer.prompt(perguntas_registro)

            nome_prof = respostas_registro['nome_prof']
            dia = respostas_registro['dia']
            turno_inicio = respostas_registro['turno_inicio']
            turno_fim = respostas_registro['turno_fim']
            pausas = respostas_registro['pausas']
            horas_extras = respostas_registro['horas_extras']

            modulo_gestao_equipe.registrar_horas(nome_prof, dia, turno_inicio, turno_fim, pausas, horas_extras)

        elif opcao == '4':
            print('Saindo do módulo de gestão de grupos profissionais....')
            break