"""
faça um jogo para o usuario adivinhar qual a palavra secreta
voce vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuario digitar apenas uma letra
quando o usuario digitar uma letra voce vai conferir se a letra digitada esta na palavra secreta
se a letra digitada esta na palavra secreta exiba a letra, else exiba *
Faça a contagem de tentativas do usuario
"""

import os
palavra_secreta= 'perfume'
letras_acertadas=''
tentativas = 0

while True:
    
    letra_digitada= input('Digite uma letra: ')
    tentativas +=1

    if len(letra_digitada) >1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada 

    palavra_formada =''
    for letra_secreta in palavra_secreta:

        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta

        else:
            palavra_formada += '*'

    print(palavra_formada)
    if palavra_formada == palavra_secreta:
        os.system('cls') ##limpando terminal
        print('VOCE GANHOU! PARABENS')
        print('A palavra secreta era:' ,palavra_secreta.capitalize())
        print('Tentativas', tentativas)
        letras_acertadas=''
        tentativas = 0
        break
