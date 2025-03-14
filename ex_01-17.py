# exercise 01
msg_01 = input('Qual o seu nome? ')
print(f'Seja bem-vindo {msg_01}!')

# exercise 02
msg_02 = input('Insira seu objeto favorito: ')
msg_03 = input('Insira sua cor favorita: ')
print(f'Aprecie: {msg_02} {msg_03}')

# exercise 03
msg_04 = input('Insira uma frase: ')
print(f'Palavras na frase: {len(msg_04.split())}')

# exercise 04
msg_05 = input('Insira um número: ')
msg_06 = input('Insira um outro número: ')
print(f'Números somados: {msg_04 + msg_05}')

# exercise 05
msg_07 = input('Insira números separados por vírgula: ')
list_of_numbs1 = [int(num.strip()) for num in msg_07.split(',')]
print(f'Média dos números inseridos: {(sum(list_of_numbs1)/len(list_of_numbs1))}')

# exercise 06
msg_08 = input('Insira números separados por vírgula: ')
list_of_numbs2 = [int(num.strip()) for num in msg_08.split(',')]
print(f'Maior número: {max(list_of_numbs2)} e menor número: {min(list_of_numbs2)}')

# exercise 07
msg_09 = int(input('Insira um número aleatório: '))
answer01 = ''
if (msg_09 > 100):
    answer01 = 'maior que 100'
elif (msg_09 < 100):
    answer01 = 'menor que 100'
else:
    answer01 = 'igual a 100'
print(f'O número {msg_09} é {answer01}')

# exercise 08
msg_10 = input('Insira dois números separados por vírgula: ')
list_of_numbs3 = [int(num.strip()) for num in msg_10.split(',')]
answer02 = 'Estes números são iguais' if list_of_numbs3[0] == list_of_numbs3[1] else 'Os números são diferentes'
print(answer02)

# exercise 09
msg_11 = input('Insira três números separados por vírgula: ')
list_of_numbs4 = [int(num.strip()) for num in msg_11.split(',')]
answer03 = 'Pode-se formar um triângulo' if (list_of_numbs4[0] + list_of_numbs4[1]) == list_of_numbs4[2] else 'Não é possível formar um triângulo'
print(answer03)

# exercise 10
msg_12 = int(input('Insira um número: '))
list_of_numbs5 = []
multiplicator = 1
for i in range(0, 10):
    list_of_numbs5.append(msg_12 * multiplicator)
    multiplicator+=1
print(f'Tabuada do 1 ao 10 do {msg_12}: {list_of_numbs5}')

# exercise 11
msg_13 = int(input('Insira um número: '))
def divisores(num):
    for i in range(1, num//2+1):
        if num % i == 0:
            yield i
    yield num
print(list(divisores(msg_13)))

# exercise 12
msg_14 = int(input('Insira um número: '))