# tupla não pode ser alterada pelo usuário, após ser cria 
numero = (5, 8, 12, 8, 7, 8, 3) 
#para ser uma tupla precisa estar entre parenteses 
print("tupla original:", numero) 
#imprimindo para o usuário a tupla original, sem manipulações 
print("Tamanho da tupla:", len (numero)) 
print("acessando pelo indice",numero[2])
#escolhendo qual item será mostrado através do indice, lembrando que começa em zero 
print("fazendo um slicing do 2 ao 5", numero[2:5]) 
#o slicing ele não pega o ultimo elemento defenido no recorte 
print("quantas vezes o numero 8 repete:",numero.count(8))
print("posição da primeira ocorrencia do numero 7:", numero.index(7)) 
minimu_tupla = min(numero) 
print("o menor numero é: ",minimu_tupla)
maximo_tupla = max (numero)
print("o maior numero é: ", maximo_tupla) 
print("a soma dos numeros da tupla é:", sum(numero)) 
print("organiza os elementos da tupla em ordem:", sorted(numero)) 

print("o numero 4 esta na tupla?",4 in numero) 

numero2= (15,20)
tupla_concatenada = numero + numero2 
print("a concatenação das tuplas 1 e 2 resulta na nova tupla:", tupla_concatenada) 

tupla_duplicada = numero * 2 
print("tupla 1 duplicada: ", tupla_duplicada) 
