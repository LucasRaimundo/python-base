"""Hello multi languages
"""

__author__="LMR"
__version__="0.0.1"

import os

languages = {"portuguese": "Olá mundo", "italian": "Ciao mondo", "english": "Hello world"}

print(f"Olá, por favor, escolha a linguagem: ")
for language in languages:
    print(f"  {language} ({languages[language]})")

language = input("Linguagem: ")

if language == "portuguese":
    print(languages.get(language))
elif language == "italian":
    print(languages.get(language))
elif language == "english":    
    print(languages.get(language))
else:    print("Linguagem não reconhecida.")