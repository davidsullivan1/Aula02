# #### Inteiros (`int`)


menu_exercicio = int(input("Digite o número (Opção de 1 a 25) equivalente ao exercício que deseja Testar: "))
quantidadeImplementada = 0;

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
if menu_exercicio == 1:
    primeiro_numero = int(input("1 - Digite um número inteiro: "))
    segundo_numero = int(input("2 - Digite Mais um número inteiro: "))
    somatorio = primeiro_numero + segundo_numero
    print(f"A soma dos números inteiros informados é: {somatorio}")

quantidadeImplementada += 1;

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
if menu_exercicio == 2:
    numero = float(input("Digite um número: "))
    divisao = numero%5 #Retorna o resto da divisão 
    print(f"O resto da divisão de {numero} por 5 é: {divisao}")

quantidadeImplementada += 1;

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
if menu_exercicio == 3:
    numero1 = int(input("Digite Um Número: "))
    numero2 = int(input("Digite mais um número"))
    resultado = numero1*numero2
    print(f"O Resultado da múltiplicação entre os números fornecidos é: {resultado}")

quantidadeImplementada += 1;

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
if menu_exercicio == 4:
    numero1 = int(input("Digite Um Número: "))
    numero2 = int(input("Digite mais um número"))
    resultado = int(numero1/numero2)
    print(f"O Resultado da Divisão Inteira entre os números fornecidos é: {resultado}")

quantidadeImplementada += 1;

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação



if menu_exercicio > quantidadeImplementada:
    print("Exercício ainda não implementado")