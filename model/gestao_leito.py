import csv
import datetime
import time


class SistemaGestaoLeitos:
    def __init__(self, leitos_uti=20, leitos_amarela=10, leitos_intermediario=5):
        self.leitos_uti = leitos_uti
        self.leitos_amarela = leitos_amarela
        self.leitos_intermediario = leitos_intermediario
        self.leitos_ocupados = {
            "UTI": 0,
            "Amarela": 0,
            "Intermediário": 0,
        }
        self.historico_ocupacao = []

    def monitorar_leitos(self):
        while True:
            print('''
                [ 1 ] ESTADO CRITÍCO
                [ 2 ] ESTADO DE MENOR GRAVIDADE
                [ 3 ] ESTADO INTERMEDIÁRIO
                ''')
            resp = int(input("QUAL O ESTADO DO PACIENTE? "))
            if resp == 1:
                self.leitos_ocupados["UTI"] += 1
            elif resp == 2:
                self.leitos_ocupados["Amarela"] +=1
            elif resp == 3:
                self.leitos_ocupados["Intermediário"] +=1

            # Registre a ocupação atual no histórico
            registro = {
                "Data e Hora": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "UTI": self.leitos_uti - self.leitos_ocupados["UTI"],
                "Amarela": self.leitos_amarela - self.leitos_ocupados["Amarela"],
                "Intermediário": self.leitos_intermediario - self.leitos_ocupados["Intermediário"]
            }
            for chave, valor in registro.items():
                if chave == "UTI" and valor == 2:
                    print("ALERTA! POUCAS VAGAS NA UTI")
                elif chave == "Amarela" and valor == 2:
                    print("ALERTA! POUCAS VAGAS NA ALA AMRELA")
                elif chave == "Intermediário" and valor == 2:
                    print("ALERTA! POUCAS VAGAS NA ALA INTERMEDIÁRIO")
            
            self.historico_ocupacao.append(registro)

            print('''
                  [ 1 ] UTI
                  [ 2 ] AMARELA
                  [ 3 ] INTERMEDIÁRIA
                  [ 4 ] NENHUMA
                  ''')
            resp2 = int(input("QUAL ALA LIBEROU VAGA: "))
            if resp2 == 1:
                print("LEITO DA UTI DISPONÍVEL")
                self.leitos_ocupados["UTI"] -=1
            elif resp2 == 2:
                print("LEITO DA AMARELA DISPONÍVEL")
                self.leitos_ocupados["Amarela"] -=1
            elif resp2 == 3:
                print("LEITO DA INTERMEDIÁRIA DISPONÍVEL")
                self.leitos_ocupados["Intermediário"] -=1 
            elif resp2 == 4:
                print("NENHUM LEITO DISPONÍVEL")

            if len(self.historico_ocupacao) % 24 == 0:
                self.salvar_historico_csv()

            time.sleep(30)

    def salvar_historico_csv(self):
        with open('historico_ocupacao.csv', 'w', newline='') as arquivo_csv:
            campos = ["Data e Hora", "UTI", "Amarela", "Intermediário"]
            escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
            escritor_csv.writeheader()
            escritor_csv.writerows(self.historico_ocupacao)

if __name__ == "__main__":
    sistema = SistemaGestaoLeitos()
    sistema.monitorar_leitos()
