
enviado = ("ABC123", "JKL321", "STU741")
recebido = ("XYZ789", "MNO654")
transito = ("DEF456", "PQR987")


num = int(input("Digite 1 para ver pedidos enviados, 2 para recebidos, 3 para em trânsito e 4 para saber o código, 5 para saber o status: "))
    
if num == 1:
        print("Pedidos enviados:", len(enviado))  
elif num == 2:
        print("Pedidos recebidos:", len(recebido))  
elif num == 3:
        print("Pedidos em trânsito:", len(transito))  
elif num == 4: 
        print("Os códigos dos pedidos em trânsito são:", transito) 
elif num == 5: 
        todos_pedidos = enviado + recebido + transito
        codigo = input("Digite seu código para saber o status do pedido: ")
        if codigo in enviado:
            print(f"O pedido {codigo} foi ENVIADO.")
        elif codigo in recebido:
            print(f"O pedido {codigo} foi RECEBIDO.")
        elif codigo in transito:
            print(f"O pedido {codigo} está EM TRÂNSITO.")
        else:
            print("Código não encontrado.")
else:
        print("Opção inválida.")

    