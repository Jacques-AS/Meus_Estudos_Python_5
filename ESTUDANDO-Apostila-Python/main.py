print('*** Jogo da Advinhação ***')
numero = 76
chute = int(input('Chute um número entre 0 a 100: '))
print(f'Você digitou: {chute}')
print()
if numero == chute:
    print(f'Parabéns você acertou!!! Era o número {numero}')
elif numero < chute:
    print(f'O seu chute foi maior que o número secreto!!!\nTente novamente.')
else:
    print(f'O seu chute foi menor que o número secreto!!!\nTente novamente.')