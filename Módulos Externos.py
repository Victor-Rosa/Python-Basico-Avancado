"""
Módulos Externos

- Utilizamos o gerenciador de pacotes Python chamado de: Pip - Pyyhon Installer Package

# colorama -> impressão de textos coloridos no terminal
from colorama import init, Fore
init()
print(Fore.RED + "Victor Rosa")

"""

import pydf

pdf = pydf.generate_pdf('<h1>Victor Rosa</h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
