"""Hello multi languages
"""

__author__="LMR"
__version__="0.0.1"

import os

languages = {"portuguese": "pt_BR", "italian": "it_IT", "english": "en_EN"}

print(f"Olá, por favor, escolha a linguagem: ")
for language in languages:
    print(f"  {language} ({languages[language]})")

language = input("Linguagem: ")

if language == "portuguese":
    print("Olá, mundo!")
elif language == "italian":
    print("Ciao, mondo!")
elif language == "english":    
    print("Hello, world!")
else:    print("Linguagem não reconhecida.")