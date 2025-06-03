enviado = ("ABC123", "JKL321", "STU741")
recebido = ("XYZ789", "MNO654")
transito = ("DEF456", "PQR987")

print("Escolha uma opção:")
print("1 - Ver quantos pedidos foram enviados")
print("2 - Ver quantos foram recebidos")
print("3 - Ver quantos estão em trânsito")
print("4 - Ver os códigos dos pedidos em trânsito")
print("5 - Digitar um código para saber o status")

num = int(input("Digite o número da opção: "))

if num == 1:
    print("Pedidos enviados:", len(enviado))
elif num == 2:
    print("Pedidos recebidos:", len(recebido))
elif num == 3:
    print("Pedidos em trânsito:", len(transito))
elif num == 4:
    print("Códigos em trânsito:", transito)
elif num == 5:
    codigo = input("Digite o código do pedido: ")
    if codigo in enviado:
        print("Seu pedido foi ENVIADO.")
    elif codigo in recebido:
        print("Seu pedido foi RECEBIDO.")
    elif codigo in transito:
        print("Seu pedido está EM TRÂNSITO.")
    else:
        print("Código não encontrado.")
else:
    print("Opção inválida.")
    
    
    
    
    
    
