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

    def eficiencia_uso_equipamentos(self):
        with open('database/equipamentos.csv', 'r') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            next(leitor) 

            with open('database/equipamentos_relatorio.csv', 'w', newline='') as arquivo_relatorio:
                escritor = csv.writer(arquivo_relatorio)
                escritor.writerow(['Equipamento', 'Nota'])

                for linha in leitor:
                    nome = linha[0]
                    print(f'Equipamento: {nome}')
                    nota = input('Dê uma nota para o equipamento: ')
                    escritor.writerow([nome, nota])

            