import csv
import os

class GestaoEquipe:
    def __init__(self):
        self.profissionais = "database/profissionais.csv"
        self.equipes = "database/equipes.csv"
        self.registrarhoras = "database/registrar_ponto_profissionais.csv"

        if not os.path.isfile(self.profissionais):
            with open(self.profissionais, 'w', newline='') as arquivo_csv:
                escritor = csv.writer(arquivo_csv, delimiter=';')
                escritor.writerow(['Nome', 'Cargo', 'Experiencia', 'Dados do Contato', 'Disponibilidade', 'Carga Horaria', 'Competencia', 'Inicio do Turno', 'Fim do Turno', 'Dias'])

        if not os.path.isfile(self.registrarhoras):
            with open(self.registrarhoras, 'w', newline='') as arquivo_csv:
                escritor = csv.writer(arquivo_csv, delimiter=';')
                escritor.writerow(['Nome', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'])

    def cadastro_alocar_plantoes(self, nome, cargo, experiencia, dados, competencia, inicio_turno, fim_turno, dias):  
        carga_horaria = fim_turno - inicio_turno
        disponibilidade = None  

        if inicio_turno == 6:
            disponibilidade = 'Manha'
        elif inicio_turno == 14:
            disponibilidade = 'Tarde'
        elif inicio_turno == 22:
            disponibilidade = 'Noite'
        
        lista = [nome, cargo, experiencia, dados, disponibilidade, str(carga_horaria), competencia, str(inicio_turno), str(fim_turno), dias]

        with open(self.profissionais, 'a', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv, delimiter=';')
            escritor.writerow(lista)
        
            # Adiciona o nome do profissional no registro de horas
        with open(self.registrarhoras, 'a', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv, delimiter=';')
            # Criando uma linha vazia para colocar apenas o nome
            nome_profissional = [nome] + [''] * 30
            escritor.writerow(nome_profissional)

    def editar_profissional(self, nome, nova_experiencia, novo_dados, nova_competencia, novo_inicio_turno, novo_fim_turno, novo_dias):
        carga_horaria = novo_fim_turno - novo_inicio_turno
        disponibilidade = None  

        if novo_inicio_turno == 6:
            disponibilidade = 'Manha'
        elif novo_inicio_turno == 14:
            disponibilidade = 'Tarde'
        elif novo_inicio_turno == 22:
            disponibilidade = 'Noite'

        # Ler o arquivo CSV
        with open(self.profissionais, 'r', newline='') as arquivo_csv:
            leitor = csv.reader(arquivo_csv, delimiter=';')
            linhas = list(leitor)

        encontrado = False

        # Percorre as linhas do arquivo para verificar se o nome já existe
        for linha in linhas:
            if linha and linha[0] == nome:
                # Modificando os dados da linha se o nome já existir
                linha[2] = nova_experiencia
                linha[3] = novo_dados
                linha[4] = disponibilidade
                linha[5] = str(carga_horaria)
                linha[6] = nova_competencia
                linha[7] = str(novo_inicio_turno)
                linha[8] = str(novo_fim_turno)
                linha[9] = novo_dias
                encontrado = True

        if encontrado:
            # Escreve as modificações de volta no arquivo CSV
            with open(self.profissionais, 'w', newline='') as arquivo_csv:
                escritor = csv.writer(arquivo_csv, delimiter=';')
                for linha in linhas:
                    escritor.writerow(linha)
        else:
            print("Profissional não encontrado.")

    def criar_grupos_e_salvar(self):
        grupos = {
            'Manha (6-14)': [],
            'Manha (6-18)': [],
            'Tarde (14-22)': [],
            'Tarde (14-2)': [],
            'Noite (22-6)': [],
            'Noite (22-10)': []
        }

        with open(self.profissionais, 'r', newline='') as arquivo_csv:
            leitor = csv.reader(arquivo_csv, delimiter=';')
            next(leitor)  # ignora o cabeçalho
            for linha in leitor:
                nome, _, _, _, disponibilidade, _, _, _, fim_turno, _ = linha
                if disponibilidade == 'Manha':
                    if int(fim_turno) == 14:
                        grupos['Manha (6-14)'].append(nome)
                    elif int(fim_turno) == 18:
                        grupos['Manha (6-18)'].append(nome)
                elif disponibilidade == 'Tarde':
                    if int(fim_turno) == 22:
                        grupos['Tarde (14-22)'].append(nome)
                    elif int(fim_turno) == 2:
                        grupos['Tarde (14-2)'].append(nome)
                elif disponibilidade == 'Noite':
                    if int(fim_turno) == 6:
                        grupos['Noite (22-6)'].append(nome)
                    elif int(fim_turno) == 10:
                        grupos['Noite (22-10)'].append(nome)

        with open(self.equipes, 'w', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv, delimiter=';')
            for turno, profissionais in grupos.items():
                escritor.writerow([turno] + profissionais)

    def registrar_horas(self, nome_prof, dia, turno_inicio, turno_fim, pausas, horas_extras):
        dia = int(dia)  
        turno_inicio = int(turno_inicio)  
        turno_fim = int(turno_fim)  

        # Vê as horas trabalhadas para questão de salário
        horas_trabalhadas = (turno_fim - turno_inicio) - pausas + horas_extras
        
        with open(self.registrarhoras, 'r', newline='') as arquivo_csv:
            leitor = csv.reader(arquivo_csv, delimiter=';')
            linhas = list(leitor)

        encontrado = False

        # Percorre as linhas do arquivo para encontrar o profissional pelo nome
        for linha in linhas:
            if linha and linha[0] == nome_prof:
                # Quando encontra a linha do profissional
                encontrado = True
                # Adicionando as horas trabalhadas ao dia especificado
                if 1 <= dia <= 30:
                    linha[dia] = horas_trabalhadas

        if encontrado:
            # Escreve as modificações de volta no arquivo CSV
            with open(self.registrarhoras, 'w', newline='') as arquivo_csv:
                escritor = csv.writer(arquivo_csv, delimiter=';')
                for linha in linhas:
                    escritor.writerow(linha)
        else:
            print("Profissional não encontrado.")

Gestao = GestaoEquipe()

while True:
    opcao = input("1 - Adicionar profissional de saúde\n2 - Editar profissional\n3 - Registrar horas\n4 - Sair\nEscolha uma opção: ")
    
    if opcao == '1':
        nome = input('Nome: ')
        cargo = input('Cargo: ')
        experiencia = input('Experiência: ')
        dados = input('Dados do Contato: ')
        competencia = input('Competência: ')
        inicio_turno = int(input('Início do turno: '))
        fim_turno = int(input('Fim do turno: '))
        dias = input('Dias de trabalho (Separados por vírgula): ')
        Gestao.cadastro_alocar_plantoes(nome, cargo, experiencia, dados, competencia, inicio_turno, fim_turno, dias)
        Gestao.criar_grupos_e_salvar()
    
    elif opcao == '2':
        nome_profissional = input('Nome do profissional que deseja editar: ')
        nova_experiencia = input('Nova Experiência: ')
        novo_dados = input('Novos Dados do Contato: ')
        nova_competencia = input('Nova Competência: ')
        novo_inicio_turno = int(input('Novo Início do turno: '))
        novo_fim_turno = int(input('Novo Fim do turno: '))
        novo_dias = input('Novos Dias de trabalho (Separados por vírgula): ')
        Gestao.editar_profissional(nome_profissional, nova_experiencia, novo_dados, nova_competencia, novo_inicio_turno, novo_fim_turno, novo_dias)
        Gestao.criar_grupos_e_salvar() 
    
    elif opcao == '3':
        nome_prof = input('Nome: ')
        dia = float(input('Dia: '))
        turno_inicio = float(input('Início do turno: '))
        turno_fim = float(input('Fim do turno: '))
        pausas = float(input('Pausas: '))
        horas_extras = float(input('Horas extras: '))
        Gestao.registrar_horas(nome_prof, dia, turno_inicio, turno_fim, pausas, horas_extras)
    
    elif opcao == '4':
        break
