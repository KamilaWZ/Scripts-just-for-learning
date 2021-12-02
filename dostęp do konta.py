while True:
    haslo = input('Podaj Hasło')
    if haslo == 'Kuku':
        break
    else:
        for i in range(3):
            if haslo != 'Kuku':
                haslo = input(f'Błędne hasło. To Twoja {i + 1} próba z trzech')
            else:
                print: 'Uzyskujesz dostęp'
    break
print('dostęp do konta został zablokowany')
