from colorama import init, Fore, Style
from model.controle_equipamento import ControleEquipamentos

init()
cor_mensagem_erro = Fore.RED

modulo_controle_equipamento = ControleEquipamentos()

def run():
    modulo_controle_equipamento.executar()