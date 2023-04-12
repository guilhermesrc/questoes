palavra = input()
invertida = ""
for x in range(len(palavra),0, -1):
	invertida += palavra[x-1]
print(invertida)