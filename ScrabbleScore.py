def wczytaj_slownik():
    '''Wczytanie słownika'''
    print ('Inicjalizacja słownika...')
    slownik=[]
    with open("slowa.txt", 'r', encoding='utf-8') as f:
        slownik=f.readlines()
    slownik=[x.strip() for x in slownik]
    print('Słownik gotowy')
    return slownik

def wprowadz_slowo():
    slowo=input('Podaj slowo do sprawdzenia: ')
    return slowo

def wybor():
    print ('Wybierz co chcesz zrobić')
    print ('[1] Sprawdzić czy istnieje')
    print ('[0] Wyjście')
    try:
        wybor=input('Decyzja: ')
        return int(wybor)
    except ValueError:
        print ('Nieprawidłowy wybór!')
    return None

slownik=wczytaj_slownik()
wyb=-1
while wyb!=0:
    sprawdz=wprowadz_slowo()
    wyb=wybor()
    if wyb==1:
        if sprawdz in slownik: 
            print ('Slowo istnieje')
        else:
            print ('Słowo nie istnieje')

    