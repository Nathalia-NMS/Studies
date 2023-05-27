# 1. Variáveis

idade = 25 # Criando variáveis
nome = "Nathália M." # Sempre coloca-se texto entre aspas

"""
    Tipos de variáveis

    1. int: números inteiros, ou seja, números sem parte decimal: 0, 5, -1, 1000
    2. float: números reais, ou seja, números com parte decimal: 1.0, -2.7, 3.14
    3. str: cadeias de caracteres, ou seja, dados textuais
    4. bool: valores lógicos (booleanos): True ou False
        • True ou False precisa iniciar com letra maiúscula
"""

idade = 25 # int
altura = 1.54 #float
nome = "Nathália M." #str
estudando = True #bool

print(type(idade)) # Imprimir o tipo da variável
print(type(altura))
print(type(nome))
print(type(estudando))

# Obtendo dados de variáveis e salvando em variáveis

linguagem = input("Pergunta?") # O que o usuário digitar no input irá para a variável, nesse caso, "linguagem"

print("Resposta", linguagem)


#2. Operadores

# Operações Matemáticas (Aritméticas)

"""
    Soma: +
    Subtração: -
    Multiplicação: *
    Divisão: /
    Divisão inteira: //
    Resto da divisão: %
    Potência: **
"""

numero1 = 10
numero2 = 20

print(numero1 + numero2)
print(numero1 - numero2)
print(numero1 * numero2)
print(numero1 / numero2)
print(numero1 // numero2) # Descarta a parte decimal
print(20 % 3) # Resultado é o resto da divisão
print(2 ** 3)

# Operadores Booleanos

"""
Operadores Booleanos são operadores de comparação
"""

idade1 = 10
idade2 = 15
altura1 = 1.77
altura2 = 1.65
altura3 = altura2

print(idade1 > idade2)
print(idade1 <= idade2)
print("Python" == "python")
print("banana" != "abacaxi")
print(altura1 >= altura2)
print(altura2 > altura3)

# 3. Conversão de Tipos

idade = '26'

print(idade, type(idade)) # Tipo Str

idade_inteira = int(idade) #Conversão do tipo da variável idade de str para int

print(idade_inteira, type(idade_inteira)) # Tipo int

"""
    int() - Converte qualquer tipo de variável para inteira
    str() - Converte para string
    float() - Converte para o tipo float
    bool() - Converte para booleana
"""

altura = input('Informe a sua altura: ') 

print(altura, type(altura)) # Toda informação fornecida no input será uma variável tipo str

altura = float(input('Informe a sua altura: ')) # Conversão automática de str para float

print(altura, type(altura))

# 4. Estruturas Condicionais

idade = 20

if idade >= 18:
    print("Você é maior de iadae.")
else:
    print("Você é menor de idade.")

"""
    Imagine que você queira imprimir "Aprovado(a)", caso o estudante tenha uma média superior
    ou igual a 7, e "Reprovado", caso a média seja inferior a 7.


media = float(input("Informe a média do estudante: "))

if media >= 7:
    print("Você foi aprovado(a)")
elif media <= 5: # Elif = Else + If
    print("Recuperação.")
else:
    print("Você foi reprovado(a)")
"""

media = 10
presenca = 100

if media >= 7 and presenca >= 70: # And ou Or
    print("Aprovado!")
else: 
    print("Reprovado.")

# 5. Estrutura de repetição (While)

"""
    Irá repetir até a condição se concretizar
"""

numero_sorteado = 15

numero_escolhido = int(input("Informe um número entre 1 e 20: "))

while numero_escolhido != numero_sorteado:
    print("Você errou o número, tente novamente...")

    numero_escolhido = int(input("Informe um número entre 1 e 20: "))

print("Parabéns! Você acertou!")

# Estrutura com contador

"""
contador = 0
while contador < 5:
    print(contador)

    contador = contador * 1
 """

# 6. Laços de Repetição (For)

"""
for variavel in range(10): # Para uma determinada variável em uma determinada faixa, faça...
    print(variavel)

for variavel in range(1, 11): # Ele vai do 1 até o menor do que o valor de parada
    print(variavel)    

for variavel in range(1, 12, 3): # Vai de 1 a 12, pulando de 3 em 3 
    print(variavel)    
"""

soma = 0

for i in range(1, 4):
    nota = float(input(f"Informe a sua nota {i} "))

    soma = soma + nota 

print(soma / 3) # Chega na media das 3 notas

# 7. Listas

# Antes

nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com listas

notas = [7.9, 9.7, 8.2] # [] se referem a listas

# Criando listas

lista_vazia = []
lista_vazia = list()
lista = [26, "Nat", 3.14159, False] # Permite diferentes tipos de texto
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices (fatiamento)

lista = [10, "Nat", 3.14159, True]

print(lista[0]) # A indexação sempre começa em 0
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1]) # Acessa o último elemento
print(lista[-2]) # Penúltimo elemento

#Slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3]) # Pega do índica 0 até o menor que o 3
print(lista[3:]) # Se não determinar o termino, ele vai até o final
print(lista[2:6:2]) # Pega do índice 2 até o menor que o índice 6, pulando de 2 em 2

# Interações com FOR

for elemento in lista: # Para cada elemento dentro da lista, imprima cada elemento
    print(elemento)

print("Comprimento da lista:", len(lista)) # len te dá a quantidade de elementos

for i in range(len(lista)):
    print(i) # Imprime a quantidade de elemento
    print(lista[i]) # Imprime a lista na posição i, agora pelo índice

# 8. Métodos de Listas

lista = [1, 3, 12, 8, 2]

# append

print("Antes do append:", lista)

lista.append(3) # Adiciona um elemneto no final da lista

print("Depois do append:", lista) 

# insert - Eu escolho onde adiciono o elemento

lista.insert(2, 10) # O 2 é o índice em que eu quero adicionar e o 10 é o valor

print("Depois do insert:", lista)

# extend - Serve para juntar duas listas

lista2 = [1, 2, 3]

lista.extend(lista2)

print("Depois do extend:", lista)

# pop

lista.pop() # Elimina o último elemento

print("Lista após o pop:", lista)

lista.pop(0) # Elimina o elemento do índice entre parênteses

print("Lista após o pop:", lista)

# remove

lista.remove(3) # Remove o elemento que eu quero, NÃO O ÍNDICE

print("Depois do remove:", lista) # Sempre remove o primeiro elemento que ele encontra, mesmo que haja outros

# count

print("Quantidade de 2 na lista:", lista.count(2)) # Conta quantas vezes aquele elemento aparece

# index

print("índice do elemento 12:", lista.index(12)) # Diz a posição do elemento

# sort

lista.sort() # Ordena na forma crescente
lista.sort(reverse=True) # Decrescente

print(lista)

# 9. Funções de Lista

# len

print(len(lista)) # Quantos elemento há na lista

# sum

print(sum(lista)) # Soma todos os elemnentos da lista

# max

print("Maior elemento da lista:", max(lista))

# min 

print("Menor elemento da lista:", min(lista))
