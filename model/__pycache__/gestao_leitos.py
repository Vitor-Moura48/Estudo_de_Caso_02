import csv

class gestao_leito:
    def __init__(self):
        self.numeros_leitos_UTI = 20
        self.numeros_leitos_amarela = 10
        self.numeros_leitos_intermediario = 5

    def monitoramento_tempo_real(self, numero_leitos_UTI, numeros_leitos_amarela, numeros_leitos_intermediario):
        print('''
              [ 1 ] ESTADO CRITÍCO
              [ 2 ] ESTADO DE MENOR GRAVIDADE
              [ 3 ] ESTADO INTERMEDIÁRIO
              ''')
        resp = int(input("QUAL O ESTADO DO PACIENTE? "))
        if resp == 1:
            cont_vagas_UTI +=1
            if cont_vagas_UTI == numero_leitos_UTI:
                print("ALERTA! SEM VAGAS NA UTI")
            else:
                print(f'{numero_leitos_UTI-cont_vagas_UTI} VAGAS DISPONÍVEIS NA UTI')
        
        elif resp == 2:
            cont_vagas_amarela +=1
            if cont_vagas_amarela == numeros_leitos_amarela:
                print("ALERTA! SEM VAGAS NA ALA AMARELA")
            else:
                print(f'{numero_leitos_UTI-cont_vagas_amarela} VAGAS DISPONÍVEIS NA ALA AMARELA')
        
        elif resp == 3:
            cont_vagas_intermediario +=1
            if cont_vagas_amarela == numeros_leitos_intermediario:
                print("ALERTA! SEM VAGAS NA ALA INTERMEDIÁRIA")
            else:
                print(f'{numero_leitos_UTI-cont_vagas_UTI} VAGAS DISPONÍVEIS NA ALA INTERMEDIÁRIA')
        
        print("-="*40)
        print(f'NÚMERO DE VAGAS NA UTI OCUPADAS: {cont_vagas_UTI}')
        print(f'NÚMERO DE VAGAS NA ALA AMARELA OCUPADAS: {cont_vagas_amarela}')
        print(f'NÚMERO DE VAGAS NA ALA INTERMEDIÁRIA OCUPADAS: {cont_vagas_intermediario}')

