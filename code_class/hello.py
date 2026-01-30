"""Hello multi languages
"""

__author__="LMR"
__version__="0.0.1"

import os

current_language = os.getenv("LANG", "en_EN")
msg = "Hello, World!"

if current_language[:5] == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language [:5]== "it_IT":
    msg = "Ciao, Mudo!"

print(msg)