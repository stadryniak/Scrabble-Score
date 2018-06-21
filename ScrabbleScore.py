def wczytaj_slownik():
    '''Wczytanie słownika'''
    print ('Inicjalizacja słownika...')
    with open("slowa.txt", 'r', encoding='utf-8') as f:
        slownik=f.readlines()
    slownik=[x.strip() for x in slownik]
    print('Słownik gotowy')
    print ('')
    return slownik

def wprowadz_slowo():
    '''Wczytanie słowa od użytkownika'''
    slowo=input('Podaj slowo do sprawdzenia lub 0, aby zakończyć: ')
    print('')
    slowo=slowo.lower()
    return slowo

def wybor():
    '''Odpowiada za wybór funkcji programu'''
    print ('Wybierz co chcesz zrobić')
    print ('[1] Sprawdzić czy istnieje')
    print ('[0] Wyjście')
    print ('')
    try:
        wybor=int(input('Wybór: '))
        print('')
        if wybor>1:
            print('Nieprawidłowy wybór')
            print('')
            return None
        return wybor
    except ValueError:
        print('')
        print ('Nieprawidłowy wybór')
        print('')
        return None


slownik=wczytaj_slownik()
wyb=-1
while wyb!=0:
    sprawdz=wprowadz_slowo()
    if sprawdz=='0':
        print ('Koniec pracy')
        break
    wyb=wybor()
    if wyb==1:
        if sprawdz in slownik: 
            print ('Słowo istnieje')
            print('')
        else:
            print ('Słowo nie istnieje')
            print('')

    