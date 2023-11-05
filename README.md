# Estudo_de_Caso_02

# Módulo 5 - Carlos Erbe



# Para datas
import datetime as dt


''' será q faço? a = 0 #Aqui é só para eu salvar no canto certo a lista de prontuário/paciente lá no fim da função'''
lista_cadastro_pacinete = []
lista_de_todos_os_pacinetes = []
lista_do_prontuario = []

#Aqui vou criar a função data e hora
def adicionar_data():
    data_criacao = dt.datatime.now()
    data_criacao = data_criacao.strftime("%d/%m/%y %H:%M")


# Função para cadastrar paciente
def cadastro_de_paciente (self):
    while True:
        data_criacao_prontuario = data_criacao()
        print('1 - Para cadastrar novo pacinete\n')
        print('2 - Para encerrar o cadastro', '\n'*4)
        novo_pacinete = input(int('Escolha uma opção para podermos proseguir:\n'))
        if novo_pacinete == 1:
            nome_do_paciente = input(str('Digite o nome do paciente:\n'))
            idade_do_paciente = input(int('Digite a itidade do paciente\n'))
            sexo_do_paciente = input(str('Digite o sexo do paciente:\n'))
            identidade_do_paciente = input(int('Digite o RG do paciente\n'))
            contato_de_emergencia = input(int('Digite um contato para emergência\n'))
            if gravidade_do_paciente == '1':
                gravidade_do_paciente = 'Leve'
            if gravidade_do_paciente == '2':
                gravidade_do_paciente = 'Moderado'
            if gravidade_do_paciente == '3':
                gravidade_do_paciente = 'Grave'
            
            #Verificar se todos os campos estão preenchidos
            if nome_do_paciente is None:
                raise KeyboardInterrupt
            if idade_do_paciente is None:
                raise KeyboardInterrupt
            if sexo_do_paciente is None:
                raise KeyboardInterrupt
            if identidade_do_paciente is None:
                raise KeyboardInterrupt
            if contato_de_emergencia is None:
                raise KeyboardInterrupt
            

            #Usando função data
            data_criacao_do_padiente = data_criacao()

            lista_cadastro_pacinete = [nome_do_paciente, idade_do_paciente, sexo_do_paciente, sexo_do_paciente, identidade_do_paciente, contato_de_emergencia]
            lista_cadastro_pacinete.insert [0,data_criacao_do_padiente]
            lista_de_todos_os_pacinetes.append [lista_cadastro_pacinete]
            a = a+1
            #Função cadastrar prontuário
            def prontuario_do_paciente (self):
                while True:
                    #Tenho que exibir os dados_do_paciente
                    #Aqui vou adicionar o horário que eu criei o prontuário
                    adicionar_data_do_prontuario = data_criacao()

                    #Aqui vou salvar as infomações do prontuário
                    data_do_diagnostico = input(str('Digite a data do diagnóstico:\n'))
                    diagnostico_do_paciente = input(str('Digite o diagnóstico do pacinete:\n'))
                    condicao_do_paciente = input(str('Digite a condição do pacinete:\n'))
                    recomendacao_de_medicacao = input(str('Digite a recomendação da medicação:\n'))

                    '''#Aqui em baixo falta fazer uma lista com os nomes dos médicos
                    medico_que_atendeu = input(str('Selecione o medico que atendeu:\n'))'''
                    '''#Aqui em baixo precisa criar uma função para a receita do paciente
                    receita_dos_medicamentos = input(str(':\n'))'''

                    observacao_sobre_o_paciente = input(str('Observação adicional sobre o paciente:\n'))
                    gravidade_do_paciente = input(str('Digite o número referênte a gravidade\n'))

                    #Salvando dados do prontuário na lista do paciente
                    lista_do_prontuario = [data_do_diagnostico, diagnostico_do_paciente, condicao_do_paciente, recomendacao_de_medicacao]
                    lista_cadastro_pacinete.append [lista_do_prontuario]
                    print("Digite 1 se quiser fazer o uploud")
                    print("Digete 2 se não quiser fazer o uploud")
                    opcao_historico_medico = input(int("Deseja fazer o uploud do Hitórico Médico do paciente?"))
                    if opcao_historico_medico == 1:
                        #Aqui tem que ter como fazer o uploud do histórico do paciente


                        #Aqui estou criando e salvando os dados e a data do medico que atender obs: dá pra melçhorar
                        adicionar_data_historico_medico =  data_criacao()
                        lista_do_prontuario.append [adicionar_data_historico_medico , '''aqui tenho q adicionar o médico''']
                        lista_cadastro_pacinete.append [lista_do_prontuario]
                        print("Iportar arquivo: \nHistórico Médico")


                         
                    if opcao_historico_medico == 2:
                        break

                    else:
                        print("Opção inválida. Por favor, escolha uma opção válida.")


            def uploud_dos_exames ():
                while True:
                    #Aqui tem que ter como fazer o uploud dos exames
                    print("Digite 1 se quiser fazer o uploud")
                    print("Digete 2 se não quiser fazer o uploud")
                    opcao_exames = input(int("Deseja fazer o uploud dos exames?"))
                    if opcao_exames == 1:
                        #Aqui tem que ter como fazer o uploud do histórico do paciente
                        print("Iportar arquivo: Exames")
                        #

                        adicionar_data_do_uploud_exame =  data_criacao()
                        lista_do_prontuario.append [adicionar_data_do_uploud_exame]
                        lista_do_prontuario.append ['''Aqui tenho que salvar o arquivo do uploud''']
                        lista_cadastro_pacinete.append [lista_do_prontuario]

                    if opcao_exames == 2:
                        break

                    else:
                        print("Opção inválida. Por favor, escolha uma opção válida.")

        


            ''' é aqui q eu usaria o a variavel 'a' lista_de_todos_os_pacinetes.append (lista_cadastro_pacinete)'''

        elif novo_pacinete == 2:
            break
            
        else:    
            print("Opção inválida. Por favor, escolha uma opção válida.")





        
