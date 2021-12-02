def jaki_rok(rok):
    if rok >= 1582:
        if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
            print('To jest rok przestępny')
        else:
            print('To jest rok zwykły')
    else:
        print('Ten rok nie jest w kalendarzu gregoriańskim!')

print()

jaki_rok(1999)
jaki_rok(2000)
jaki_rok(1300)
