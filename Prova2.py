# Escreva um programa em python que pergunte ao usuário a velocidade de um carro. 
#Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
#Nesse caso, exiba o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.

nome = input("Informe o seu nome: ")
velocidade = input("Informe a velocidade do seu automóvel: ")

veloc_int = int(velocidade)

if veloc_int < 80:
    print(f"Olá {nome}. Você está abaixo na velocidade permitida na via de 80Km/h.")
elif veloc_int == 80: 
    print(f"Olá, {nome}. Você na velocidade permitida na via de 80Km/h.")
else: 
    print(f"Olá {nome}. Você excedeu a velocidade permitida na via de 80Km/h.")
    print("Você foi multado.")
    print(f"Você deve pagar uma multa de R${(veloc_int - 80)*20}. ")