menu = {1 : ('Pizza', 42), 2 : ('Krewetki', 58), 3 : ('Pomidorowa', 19), 4 : ('Schabowy', 28), 5 : ('Frytki', 10), 6 : ('Piwo', 15)}
zamowienie = []
koszt = 0
wybor = 'Tak'

for nr, danie in menu.items():
    print(f'{nr}. {danie}')

while wybor != 'Nie':
    pozycja = int(input('Wybierz pozycję dania z listy Menu: '))
    ilosc = int(input('Ile?'))
    cena = menu[pozycja][1] * ilosc
    produkt = menu[pozycja][0]
    koszt += cena 
    zamowienie.append(produkt + ' x ' + str(ilosc) + ' - ' + str(cena))
    print(f'Do zamówienia dodano {ilosc} x {produkt} - {cena} zł')
    wybor = input('Czy chcesz dodać jeszcze coś do zamówienia? Tak/Nie: ')
    
print('Twoje zamówienie: ')
for nr, el in enumerate(zamowienie):
    print(f'{nr + 1}. {el} zł')
    
print(f'Koszt zamowienia wynosi {koszt} zł')
