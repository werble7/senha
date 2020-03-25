print("Olá, gostaria de agradecer por testar o meu programa!")

senha1 = input("Insira sua senha numérica aqui, por favor: ")
senha2 = input("Insira sua segunda senha numérica, por favor: ")

lista12 = [senha1,senha2]
lista21 = [senha2,senha1]

if len(senha2) > len(senha1):
	print(lista21)
else:
	print(lista12)

