sexo = int(input('Digite seu sexo: (1) sendo Homem ou (2) sendo mulher: '))

if sexo == 1:
    aH = float(input('Digite sua altura: '))
    vh = (72.7 *aH) - 58


    print('Seu peso ideal é ',vh,' kg')
elif sexo == 2:
    aM = float(input('Digite sua altura: '))
    aM = (62.1 * aM) - 44.7

    print('Seu peso ideal é', aM ,'kg ')