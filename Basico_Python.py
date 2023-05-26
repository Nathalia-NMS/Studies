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
