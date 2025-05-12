import time 

#variaveis globais 
ligado = False
tempo = 0 
potencia = 0 

def ligar (novo_tempo, nova_potencia): 
    global ligado, tempo, potencia 
    if not ligado: 
        ligado = True 
        tempo = novo_tempo 
        potencia = nova_potencia 
        print (f"Microndas ligado por {tempo} segundos na potência {potencia}")  
        iniciar_cronometro(tempo) 
        desligar() #desliga automaticamente 
    else: 
        print("O microondas já está ligado") 
        
def desligar(): 
    global ligado 
    if ligado: 
        ligado = False 
        print ("O microondas está ligado")
    else: 
        print ("O microndas já está desligado")
        
def status():
    if ligado:
        print(f"Tempo: {tempo} segundos /n potência: {potencia}") 
    else: 
        print("desligado") 

def iniciar_cronometro(segundos): 
    while segundos > 0: 
        print(f"Tempo restante: {segundos} segundos", end="\r") 
        time.sleep(1) 
        segundos -= 1 # segundos = segundos -1 
    print("\n Tempo esgotado")  

#predefinições do microondas
def pipoca(): 
    ligar(30, 100)  

pipoca()
    
#rodar a função 
         