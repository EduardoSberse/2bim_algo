compras = ["pão", "café", "leite"]
print(compras)  

#pode ser removido pelo nome do produto ou pelo indice 
#compras.remove("café")
compras.remove(compras[0]) 
print(compras) 

#append acrescenta um iten no final da lista, só pode adicionar um por vez 
compras.append("açucar")
print(compras)

# .sort ordena elementos em ordem alfabetica 
compras.sort()
print(compras) 


compras_ordenadas = sorted (compras) 
print(compras_ordenadas) 

# o nome panela é um identificador dos itens dentro da lisata, esses itens podem receber qualquer tipo de nome 
for panela in compras: 
    print("-", panela) 