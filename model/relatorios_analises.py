import pandas
import csv

class RelatorioAnalise:
    def gerar_relatorio_txt(self, perfomance_uti, perfomance_hospital):
        
        with open('database/relatorio_txt/relatorio.txt','a') as arquivo_txt:
            arquivo_txt.write(f'UTI: {perfomance_uti}/ HOSPITAL: {perfomance_hospital}')
    
    def gerar_relatorio_csv(self, perfomance_uti, perfomance_hospital):
        try:
            arquivo = pandas.read_csv('database/relatorio.csv')
        except:
            arquivo = pandas.DataFrame()
        
        analise = pandas.DataFrame({'performance_util': [perfomance_uti], 'performance_hospital': [perfomance_hospital]})

        if arquivo.empty:
            analise.to_csv('database/relatorio.csv', mode='a', index=False)
        else:
            analise.to_csv('database/relatorio.csv', mode='a', index=False, header=False)

        print(f'Média_útil --> {(arquivo["performance_util"].astype(int).sum() / len(arquivo)).round(2)}') 
        print(f'Média_hospital --> {(arquivo["performance_hospital"].astype(int).sum() / len(arquivo)).round(2)}')

    def metricas_de_ocupacao(self):
        pass

    def eficiencia_uso_equipamentos(self):
        pass


m = RelatorioAnalise()
m.gerar_relatorio_txt('8','9')
m.gerar_relatorio_csv('7','6')
m.gerar_relatorio_csv('8','5')