import time 

#variaveis globais 
ligado = False
tempo = 0 
temperatura = 0 

def ligar (novo_tempo, nova_temperatura): 
    global ligado, tempo, temperatura 
    if not ligado: 
        ligado = True 
        tempo = novo_tempo 
        temperatura = nova_temperatura
        print (f"A lava louça está ligada por {tempo} segundos na temperatura {temperatura}°C")  
        iniciar_cronometro(tempo) 
        desligar() #desliga automaticamente 
    else: 
        print("A lava louça já está ligada") 
        
def desligar(): 
    global ligado 
    if ligado: 
        ligado = False 
        print ("A lava louça está desligada")
    else:
        print ("A lava louça já estava desligada")

def iniciar_cronometro(segundos): 
    while segundos >= 0: 
        print(f"Tempo restante: {segundos} segundos", end="\r") 
        time.sleep(1) 
        segundos -= 1 # segundos = segundos -1 
    print("\n Tempo esgotado")  

def vidro():
    ligar(120,100)
    
def plastico():
    ligar(60,21)
    
def metal():
    ligar(120,30)

escolha = input("Digite oque deseja lavar: vidro(1), plastico(2) e metal(3):")
#predefinições do microondas
if escolha == "1":
    vidro()
  
elif escolha== "2":   
    plastico()

elif escolha=="3":
    metal()

else: 
    print("Digite oque deseja lavar: vidro(1), plastico(2) e metal(3):")

         