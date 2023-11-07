import pandas
import csv

class RelatorioAnalise:
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


m = RelatorioAnalise()
m.gerar_relatorio_txt('Muito','Corinthians')