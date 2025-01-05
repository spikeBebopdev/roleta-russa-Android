import os
import random
import shutil

def deletar_pasta(pasta):
    if os.path.exists(pasta):
        shutil.rmtree(pasta)
        print(f"A pasta {pasta} foi deletada com sucesso.")
    else:
        print(f"Você sorteou e não há nada a deletar...")

def roleta_russa():
    pastas = ['emulated', 'android']
    escolha = random.choice(pastas)
    print(f"Sorteando... Você vai tentar deletar a pasta: {escolha}")
    deletar_pasta(escolha)

roleta_russa()
