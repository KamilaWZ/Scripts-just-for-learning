from random import randint

print('DUŻY LOTEK')
    
wybor = 'Tak'
    
while wybor != 'Nie':
    ilosc_trafien = 0
    moje_nr = []
    wylosowane_nr = []
    
    print('Wybierz swoje numery')
    for i in range(6):
        moj_nr = int(input(str(i + 1) + 'Podaj swoje numery z zakresu od 1 do 49'))
        
        while moj_nr > 49 or moj_nr < 1:
            print('numer spoza zkresu')
            moj_nr = int(input(str(i+1) + 'Podaj numer'))
        
        while moj_nr in moje_nr:
            print('Numer został wybranym wybierz inny')
            moj_nr = int(input(str(i + 1) + 'Podaj swoje numery z zakresu od 1 do 49'))
        
        moje_nr.append(moj_nr)
    
    moje_nr.sort()
    
    for i in range(6):
        los = randint(1,49)
        while los in wylosowane_nr:
            los = randint(1,49)
        
        wylosowane_nr.append(los)
    wylosowane_nr.sort()
    
    print('wylosowane numery:', wylosowane_nr)
    print(f'Twoje numery: {moje_nr}')
    
    for el in moje_nr:
        if el in wylosowane_nr:
            ilosc_trafien += 1
    
    if ilosc_trafien == 6:
        print('wygrywasz wszystko')
    elif ilosc_trafien == 5:
        print('wygrywasz TV')
    else:
        print('nic nie wygrywasz')

    wybor = input('Czy chcesz zagrać jeszcze raz? Tak/Nie').capitalize()
else:
    print('Koniec gry')
