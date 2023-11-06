import csv
import datetime

class SistemaGestaoLeitos:
    def __init__(self, leitos_uti=40, leitos_amarela=20, leitos_intermediario=20, capacidade_maxima=80):
        self.leitos_uti = leitos_uti
        self.leitos_amarela = leitos_amarela
        self.leitos_intermediario = leitos_intermediario
        self.capacidade_maxima = capacidade_maxima
        self.leitos_ocupados = {
            "UTI": 0,
            "Amarela": 0,
            "Intermediario": 0,
        }
        self.historico_ocupacao = []

    def monitorar_leitos(self):
        while True:
            print('''
                [ 1 ] ESTADO CRÍTICO
                [ 2 ] ESTADO DE MENOR GRAVIDADE
                [ 3 ] ESTADO INTERMEDIARIO
                [ 4 ] PARA O MONITORAMENTO
                ''')
            resp = int(input("QUAL O ESTADO DO PACIENTE? "))
            if resp == 1:
                self.priorizar_leito("UTI")
            elif resp == 2:
                self.priorizar_leito("Amarela")
            elif resp == 3:
                self.priorizar_leito("Intermediario")
            elif resp == 4:
                break

            # Registre a ocupação atual no histórico
            registro = {
                "Data e Hora": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "UTI": self.leitos_uti - self.leitos_ocupados["UTI"],
                "Amarela": self.leitos_amarela - self.leitos_ocupados["Amarela"],
                "Intermediario": self.leitos_intermediario - self.leitos_ocupados["Intermediario"]
            }
            self.historico_ocupacao.append(registro)

            # Emite alertas de capacidade máxima
            if (registro["UTI"] + registro["Amarela"] + registro["Intermediario"]) >= self.capacidade_maxima:
                print("ALERTA! Capacidade máxima atingida ou próxima de ser atingida.")
                self.liberar_alas_se_necessario()

            if len(self.historico_ocupacao) % 10 == 0:
                self.gerar_relatorio()

    def priorizar_leito(self, ala):
        if self.leitos_ocupados[ala] < self.leitos_uti:
            self.leitos_ocupados[ala] += 1
        else:
            print("Todos os leitos da UTI estão ocupados. Alocando na ala de menor gravidade.")
            self.leitos_ocupados["Amarela"] += 1

    def liberar_alas_se_necessario(self):
        total_leitos = self.leitos_uti + self.leitos_amarela + self.leitos_intermediario
        if (self.leitos_ocupados["UTI"] + self.leitos_ocupados["Amarela"] + self.leitos_ocupados["Intermediario"]) == total_leitos:
            print("Todos os leitos estão ocupados. Liberação de alas necessária.")
            self.liberar_alas()

    def liberar_alas(self):
        if self.leitos_ocupados["Amarela"] > 0:
            self.leitos_ocupados["Amarela"] -= 1
            print("Liberação de leitos na ala Amarela.")
        elif self.leitos_ocupados["Intermediario"] > 0:
            self.leitos_ocupados["Intermediario"] -= 1
            print("Liberação de leitos na ala Intermediária.")
        elif self.leitos_ocupados["UTI"] > 0:
            self.leitos_ocupados["UTI"] -= 1
            print("Liberação de leitos na UTI.")
        else:
            print("Não há leitos disponíveis para liberar.")


    def salvar_historico_csv(self):
        with open('database/historico_ocupacao.csv', 'w', newline='') as arquivo_csv:
            campos = ["Data e Hora", "UTI", "Amarela", "Intermediario"]
            escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
            escritor_csv.writeheader()
            escritor_csv.writerows(self.historico_ocupacao)

    def gerar_relatorio(self):
        nome_arquivo = f'database/relatorio_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
        with open(nome_arquivo, 'w', newline='') as arquivo_csv:
            campos = ["Data e Hora", "UTI", "Amarela", "Intermediario"]
            escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
            escritor_csv.writeheader()
            escritor_csv.writerows(self.historico_ocupacao)

if __name__ == "__main__":
    sistema = SistemaGestaoLeitos()
    sistema.monitorar_leitos()
    sistema.salvar_historico_csv()
    sistema.gerar_relatorio()
