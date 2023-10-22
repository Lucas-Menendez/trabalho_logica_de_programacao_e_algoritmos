#Mensagem de boas-vindas.
print("\n")
print("💳 Seja bem-vindo a loja do Lucas Menezes Mendes! 💳")
print("\n")

#Inserção dos valores para variáveis pelo usuário.
val_produto = int(input("Insira o valor do produto: "))
qnt_produto = int(input("Insira a quantidade do produto: "))

#Saída no console com valor sem desconto do produto.
print(f"\nO valor SEM desconto é de R$ {(val_produto * qnt_produto):.2f}.")

#Condições para cálculo do desconto do produto.
if qnt_produto < 200 :
    print(f"O valor COM desconto é de R$ {(val_produto * qnt_produto):.2f}.")

elif qnt_produto >= 200 and qnt_produto < 1000 :
    print(f"O valor COM desconto de 5% é R$ {(val_produto * 0.95 * qnt_produto):.2f}.")
    
elif qnt_produto >= 1000 and qnt_produto < 2000 :
    print(f"O valor COM desconto de 10% é R$ {(val_produto * 0.9 * qnt_produto):.2f}.")

else :
    print(f"O valor COM desconto de 15% é R$ {(val_produto * 0.85 * qnt_produto):.2f}.")

print("\n")
print("Encerrando o programa... 👋")
print("\n")