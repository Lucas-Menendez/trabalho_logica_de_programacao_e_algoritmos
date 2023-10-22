
#Dicionário com os códigos dos sabores presentes no cardápio e seus respectivos valores.
cardapio = {
    "tr": [6, 11, 15],
    "pr": [7, 13, 18],
    "es": [8, 15, 21]
}

#Dicionário com os códigos dos sabores presentes no cardápio e seus respectivos nomes.
sabores = {
    "tr": "TRADICIONAL",
    "pr": "PREMIUM",
    "es": "ESPECIAL"
}

#Mensagem de boas-vindas.
print("\nSeja bem-vindo a sorveteria do Lucas Menezes Mendes!!! 🍨😎\n")

#Tabela o cardápio com os sabores e valores de cada sorvete por quantidade de bolas.
print("+----------------------------------Cardápio---------------------------------------+")
print("| Nº De Bolas | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |")
print("|      1      |        R$ 6,00         |      R$ 7,00       |       R$ 8,00       |")
print("|      2      |        R$ 11,00        |      R$ 13,00      |       R$ 15,00      |")
print("|      3      |        R$ 15,00        |      R$ 18,00      |       R$ 21,00      |")
print("+---------------------------------------------------------------------------------+")

#Variável com valor total que será somado até que o usuário encerre o programa.
val_total = 0

while True:

    #Usuário escolhe o sabor.
    sabor_sorvete = input("\nInsira o sabor do sorvete desejado (tr, es e pr): ")

    #Validação do sabor inserido pelo usuário.
    if sabor_sorvete not in cardapio:
        print("Sabor inválido, tente novamente.")
        continue
   
    #Usuário escolhe a quantidade de bolas.
    qnt_bolas = input("Insira a quantidade de bolas (1,2 ou 3): ")

    #Validação da quantidade de bolas inserida pelo usuário.
    if qnt_bolas not in ["1", "2", "3"]:
        print("Quantidade de bolas de sorvete inválida, tente novamente.")  
        continue

    #Convertendo a varíavel para números inteiros.
    qnt_bolas = int(qnt_bolas)
    
    #Consultando o preço com base no sabor escolhido e na quantidade de bolas no dicionário de cardápio.
    preco = cardapio[sabor_sorvete][qnt_bolas - 1]
    
    #Acrescenta o valor do preço do último produto ao valor final.
    val_total = val_total + preco

    #Escreve ao usuário informações pertinentes à última da compra.
    print(f"\nVocê pediu {qnt_bolas} bolas de sorvete do sabor {sabores[sabor_sorvete]}: R$ {(preco):.2f}")

    #Verifica se usuário quer continuar comprando.
    mais_sorvete = input("\nDeseja mais algum sorvete? (sim = s / não = qualquer outra tecla): ") 
    
    #Encerra o laço caso o usuário não queira comprar mais.
    if mais_sorvete != "s":
        break  

#Informa ao usuário o somatório de todas as compras realizadas.
print(f"\nO valor total a ser pago é de R$ {(val_total):.2f}\n")
print("Obrigado por comprar conosco, tenha um ótimo dia! 🍨😎")