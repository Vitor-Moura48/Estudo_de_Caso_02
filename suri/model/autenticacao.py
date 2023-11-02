from . import *

class Autenticacao:
    def __init__(self) -> None:
        self.arquivo_usuarios = 'usuarios.csv'
        #Verifica se o csv usuarios.csv existe caso não exista vai criar o csv usuarios.csv

        if not os.path.exists(self.arquivo_usuarios):
            with open(self.arquivo_usuarios, 'w') as arquivo:
                arquivo.write('usuario,senha\n')
                arquivo.write('admin,admin\n')
                arquivo.write('user,user\n')
                arquivo.write('teste,teste\n')
                arquivo.write('teste2,teste2\n')

    def autenticar(self, usuario: str, senha: str) -> bool:
        pass