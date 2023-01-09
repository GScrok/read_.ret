import os

def pega_retornos():
    
    caminho_retornos = 'retornos'
    arquivo = []

    for file in os.listdir(caminho_retornos):
        arquivo.append(file)
        
    return arquivo
        
