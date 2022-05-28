from time import sleep
print('*** Jogo da Advinhação ***')
numero = 76
total_tentativas = 3
rodada = 1
while rodada <= total_tentativas:
    print(f'Tentantivas {rodada} de {total_tentativas}')
    chute = int(input('Chute um número entre 0 a 100: '))
    print(f'Você digitou: {chute}')
    print('ANALISANDO.............')
    sleep(3)

    acertou = numero == chute
    maior = chute > numero
    menor = chute < numero

    if acertou:
        print(f'Parabéns você acertou!!!\nNúmero Secreto Era {numero}')
        break
    elif maior:
        print(f'O seu chute foi maior que o número secreto!!!')
    elif menor:
        print(f'O seu chute foi menor que o número secreto!!!')

    rodada = rodada + 1

print('FIM DE JOGO')