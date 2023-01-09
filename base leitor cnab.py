import pega_retorno
import os

pasta = 'retornos'
arquivos = pega_retorno.pega_retornos()

lista_de_caracteres = []
pagos = []


for arquivo in arquivos:
    with open(os.path.join(pasta,arquivo), 'r', encoding="utf-8") as arquivo_atual:
        for line in arquivo_atual:
            line = line.split()
            lista_de_caracteres.append(line)
 


    for line in lista_de_caracteres:
        
        if len(line[4]) == 9 and line[4][0] == 'I':
            if(line [4][2] == '6'):

                valor_pagamento = line[6][107:120]
                valor_pagamento = int(valor_pagamento) /100

                valor_adicional = line[6][32:42]
                valor_adicional = int(valor_adicional) /100

                valor_pagamento_final =  valor_pagamento + valor_adicional
                valor_pagamento_final = "{:.2f}".format(valor_pagamento_final)

                nosso_numero = f'{line[3][:3]}/{line[3][3:11]}-{line[3][11]}'

                data_paga = f'{line[4][3:5]}/{line[4][5:7]}/{line[4][7:9]}'


                pagos.append({
                    'nosso_numero':nosso_numero,
                    'data_pagamento':data_paga,
                    'valor_pago':valor_pagamento_final
                }) 
    
    lista_de_caracteres = []
                
    
print(pagos)