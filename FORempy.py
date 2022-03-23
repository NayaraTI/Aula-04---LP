
## Estrutura de Dados Lista

# Uma lista e uma sequencia de Objetos pode ser de qualquer tipo(int, float, string) 
# A lista é composta por [] colchetes

# Estrutura de dados lista
# Matriz 
frutas = ["Manga", "Pera", "Uva", "Morango"]

print(frutas[1])                          ## A posição 0 começa com Manga, posição de memória zero (0)

## Utilizando FOR no Phyton

for f in frutas:
    print(f)

#####  Percorrer uma lista de números

for intervalonumeros in range(0,20):
    print(intervalonumeros)


#########  Percorrer uma string

nome = "Phyton"

for letras in nome:
    print(letras)


# Nunca podemos declarar uma variável no for com o mesmo nome da estrutura de dados
for f, frutos in enumerate(frutas):
    print(f, frutos)

# O laço continua executando mesmo com a saida de memória travada
for f in frutas:
    print(frutas[2])

for f in frutas:
    print(f[0:4])

###### Criar uma estrutura de dados dentro do for

for multiplicacao in [1,2,3,4,5]:
    print(multiplicacao*10)