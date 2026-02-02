# operadores aritméticos
num1 = int(input("Digite o primeiro número:\n "))
num2 = int(input("Digite o segundo número:\n "))

#  Aritméticos
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
mod = num1 % num2
exp = num1 ** num2

# mostrar resultados
print(f"Resultado da soma: {soma}")
print(f"Resultado da subtração: {subtracao}")
print(f"Resultado da multiplicação: {multiplicacao}")
print(f"Resultado da divisão: {divisao}")
print(f"Resultado do módulo: {mod}")
print(f"Resultado do exponenciação: {exp}")

# operadores de comparação
print("Operadores de comparação:")
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
not_equal = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

# Mostrar resultados das comparações
print(f"{num1} é maior que {num2}?: {bigger}")
print(f"{num1} é menor que {num2}?: {smaller}")
print(f"{num1} é igual a {num2}?: {equal}")
print(f"{num1} é diferente de {num2}?: {not_equal}")
print(f"{num1} é maior ou igual a {num2}?: {bigger_equal}")
print(f"{num1} é menor ou igual a {num2}?: {smaller_equal}")

# atribuição 
num1 += 1 # num1 = num1 + 1
num1 -= 1 # num1 = num1 - 1
num1 *= 2 # num1 = num1 * 2
num1 /= 2 # num1 = num1 / 2