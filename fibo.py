# Input de dados
print("Digite um numero para validar se ele pertence ou não a sequência de fibonnaci:")
numero = int(input())

# Variaveis usadas para o fibonnaci
numero_anterior = 0
contador = 1
soma = 0
pertence = False

# loop de interação com fim o numero+1 que o usuário digitou
for x in range(0, numero+1):
	numero_anterior = contador
	contador = soma
	soma = numero_anterior+ contador
	print(soma)
	if soma == numero:
		pertence = True

# Se a soma em algum momento for igual ao numero digitado ao fim do programa
# ele printa a mensagem 'Pertence a sequência'
if pertence == True:
	print('Pertence a sequência!')
else:
	print('Não pertence')

