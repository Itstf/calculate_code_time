# import bibliotecas 
import time

# inicio de execucao
inicio = time.time()

# codigo principal #### colocar o codigo que deseja calcular o tempo
with open('arquivo.txt','a') as arquivo:
    arquivo.write('Funcionou! - teste')
    time.sleep(3)
    
# ####



# fim da execucao 
fim = time.time()

# delta = fim - inicio 
delta = (round)(fim - inicio,2)

# mostrar tempo de execucao na tela 
print('=-'*15)
print(f"Tempo de execução: {delta}s")
print('=-'*15)
