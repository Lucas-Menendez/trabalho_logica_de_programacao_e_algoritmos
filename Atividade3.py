#Mensagem de boas-vindas.
print("\nOlá, seja bem-vindo ao Pet Shop do Lucas Menezes Mendes!!! 🐶\n")

#Dicionário contendo informações pertinentes aos pelos.
pelos = {
    "c": {
        "nome": "Curto",
        "multiplicador": 1
    },
    "m": {
        "nome": "Médio",
        "multiplicador": 1.5
    },
    "l": {
        "nome": "Longo",
        "multiplicador": 2
    },
}

#Dicionário contendo informações pertinentes aos adicionais.
adicionais = {
    "1": {
        "nome": "Cortar unhas",
        "valor": 10
    },
    "2": {
        "nome": "Escovar dentes",
        "valor": 12
    },
    "3": {
        "nome": "Limpar orelhas",
        "valor": 15
    },    
}

#Função que verifica a entrada do usuário e caso a mesma seja feita corretamente retorna o valor de peso correto selecionado.
def cachorro_peso():
    #Loop que força o usuário a inserir um valor numérico do tipo inteiro.
    while True:
        try:
            peso = int(input("\nEntre com o peso do cachorro:  "))
            #Compara a entrada do usuário com as condições impostas e caso ultrapasse todas elas uma mensagem de erro é apresentada.
            if peso < 3:
                return 40
            elif peso >= 3 and peso < 10:
                return 50
            elif peso >= 10 and peso < 30:
                return 60
            elif peso >= 30 and peso < 50:
                return 70
            else:
                print("Não aceitamos cachorros tão grandes. 😢")
        except:
            print("Você digitou um valor não númerico. ")

        print("Por favor, entre com o peso do cachorro novamente: ")

#Função que verifica a entrada do usuário e caso a mesma seja feita corretamente retorna o valor de pelo correto selecionado.
def cachorro_pelo():
#Loop que força o usuário a inserir um valor especifico da lista.
    while True:
        print("\nEntre com o pelo do cachorro")
        #Utilizada a estrutura "For" para iterar o dicionário onde o usuário seleciona um dos itens.
        for tipo_pelo, info_pelo in pelos.items():
            print(f"{tipo_pelo} - Pelo {info_pelo['nome']}")
        pelo = input()
        #Verifica se a entrada do usuário existe na lista, caso não, uma mensagem de erro é apresentada.
        if pelo not in pelos:
            print("Opção de pelo inválida.")
        else:
            #Retorna o multiplicador dentro de um dicionário com base na entrada do usuário.
            return pelos[pelo]["multiplicador"]
        
#Função que verifica a entrada do usuário e caso a mesma seja feita corretamente retorna o valor de adicionais corretos selecionados.
def cachorro_extra(): 
    #Variável onde ficará armazenado todo o valor somado da função. 
    val_total = 0
    #Loop onde é possível o usuário inserir uma quantidade infinita de serviços adicionais até que a entrada seja zero (0).
    while True:
        print("\nDeseja adicionar mais algum serviço? ")
        #Utilizada a estrutura "For" para iterar o dicionário onde o usuário seleciona um dos itens.
        for tipo_add, info_add in adicionais.items():
            print(f"{tipo_add} - {info_add['nome']} - R$ {info_add['valor']:.2f}.")
        print("0 - Não desejo mais nada. ")
        extra = input()
        #Valida a entrada do usuário, caso válida,  ela é somada com a variável de valor total.
        if extra in adicionais:
            val_total = val_total + adicionais[extra]["valor"]
        elif extra == "0":
            return val_total
        else:
            print("Valor inválido. ")

#Atruibindo o valor retornado de cada função para as variáveis que serão utilizadas para calculo do valor final.
total_peso = cachorro_peso()
total_pelo = cachorro_pelo()
total_extra = cachorro_extra()

#Atribuindo à variável o cálculo utilizado para obtenção do valor final a ser cobrado.
total = total_peso * total_pelo + total_extra

#Imprimi o valor final ao usuário e descreve como foi feita a operação.
print(f"\nValor total a pagar é de R$ {total:.2f}. (Peso: {total_peso} * pelo: {total_pelo} + adicional(is): {total_extra}).\n")
print("🐶😄 Obrigado por utilizar nossos serviços, volte sempre! 🐶😄")
print("\n")