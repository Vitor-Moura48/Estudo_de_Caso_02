import click

from flask import Flask
from core import init_gui

app = Flask(__name__)

from routes import *

@click.command()
@click.option('--inspector', is_flag=True, help='Enable debugging mode')

def suri_init(inspector):
    init_gui(app, port=5200, window_title="Sistema de Informação de Gerenciamento Hospitalar (SIGH)", inspector_mode=inspector)

if __name__ == '__main__':
    suri_init()
