def kalkulator_bmi(waga, wzrost):
    wzor = round(waga / (wzrost/100)**2,2)

    if wzor > 25:
        print('Nadwaga')
    elif wzor <= 18.49:
        print('Niedwaga')
    else:
        print('Twoja waga jest w normie')

kalkulator_bmi(90,190)
print()
