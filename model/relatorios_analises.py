import pandas
import csv

class RelatorioAnalise:
 def gerar_relatorio_txt(self, perfomance_uti, perfomance_hospital):
    with open('database/relatorio_txt/relatorio.txt', 'a') as arquivo_txt:
        arquivo_txt.write(f'{perfomance_uti} {perfomance_hospital}\n')

    with open('database/relatorio_txt/relatorio.txt', 'r') as arquivo_txt:
        cont = 0
        soma_uti = 0
        soma_hospital = 0
        for linha in arquivo_txt:
            valores = linha.split()  
            valor_uti = int(valores[0])
            valor_hospital = int(valores[1])
            soma_uti += valor_uti
            soma_hospital += valor_hospital
            cont += 1

        media_uti = soma_uti / cont
        media_hospital = soma_hospital / cont

        print(f'Média Hospital: {media_hospital}\nMédia UTI: {media_uti}')

    def gerar_relatorio_csv(self):
        pass
    

    def gerar_relatorio_txt(self, perfomance_uti, perfomance_hospital):
        
        with open('database/relatorio_txt/relatorio.txt','a') as arquivo_txt:
            arquivo_txt.write(f'UTI: {perfomance_uti}/ HOSPITAL: {perfomance_hospital}')
    
    def gerar_relatorio_csv(self, perfomance_uti, perfomance_hospital):
        analise = pandas.DataFrame({'performance_util': perfomance_uti, 'performance_hospital': perfomance_hospital})

        analise.to_csv('database/relatorio_txt/relatorio.csv', mode='a')

        arquivo = pandas.read_csv('database/relatorio_txt/relatorio.csv')
        print(arquivo['performance_util'].sum() / len(arquivo))
        print(arquivo['performance_hospital'].sum() / len(arquivo))

    def metricas_de_ocupacao(self):
        pass

    def eficiencia_uso_equipamentos(self):
        pass
