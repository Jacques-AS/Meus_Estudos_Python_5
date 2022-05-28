from time import sleep
print('*** Jogo da Advinhação ***')
numero = 76
chute = int(input('Chute um número entre 0 a 100: '))
print(f'Você digitou: {chute}')
print('ANALISANDO.............')
sleep(3)
acertou = chute == numero
maior = chute > numero
menor = chute < numero
if acertou:
    print(f'Parabéns você acertou!!!\nNúmero Secreto Era {numero}')
elif maior:
    print(f'O seu chute foi maior que o número secreto!!!\nTente novamente.')
elif menor:
    print(f'O seu chute foi menor que o número secreto!!!\nTente novamente.')