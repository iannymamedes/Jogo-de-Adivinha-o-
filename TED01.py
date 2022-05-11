from random import randint
maquina = randint(0, 100)
print('Olá, acabei de pensar em um número entre 0 e 100.')
print('Vamos ver se você consegue adivinhar? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == maquina:
        acertou = True
    else:
        if jogador < maquina:
            print('O número secreto é maior do que o seu palpite.')
        elif jogador > maquina:
            print('O número secreto é menor do que o seu palpite.')
print('Parabéns, você acertou o número secreto com {} tentativas!' .format(palpites))
