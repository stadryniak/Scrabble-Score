def wczytaj_slownik():
    '''Wczytanie słownika'''
    print('Inicjalizacja słownika...')
    with open("slowa.txt", 'r', encoding='utf-8') as f:
        slownik=f.readlines()
    slownik=[x.strip() for x in slownik]
    print('Słownik gotowy')
    print('')
    return slownik

def wprowadz_slowo():
    '''Wczytanie słowa od użytkownika'''
    slowo=input('Podaj słowo do sprawdzenia lub 0, aby zakończyć: ')
    slowo=slowo.lower()
    print('')
    return slowo

def wybor():
    '''Odpowiada za wybór funkcji programu'''
    print('Wybierz, co chcesz zrobić')
    print('[1] Sprawdź czy istnieje')
    print('[2] Oblicz punkty za słowo')
    print('[3] Sprawdź i oblicz')
    print('[0] Wyjście')
    try:
        wybor=int(input('Wybór: '))
        print('')
        if wybor>3 or wybor<0: #zmienić w przypadku dodania funkcji
            print('Nieprawidłowy wybór')
            print('')
            return None
        return wybor
    except ValueError:
        print('')
        print ('Nieprawidłowy wybór')
        print('')
        return None

def istnieje(slowo):
    if sprawdz in slownik: 
        return 'Słowo istnieje'
    else:
        return'Słowo nie istnieje'

def premia_literowa(slowo,pkt,litery):
    try:
        ile=int(input('Liczba premii literowych: '))
        print('')
        if ile<0:
            print('Nieprawidłowy wybór, premia nia naliczona')
            print('')
            return pkt
    except ValueError:
        print('')
        print ('Nieprawidłowy wybór, premia nie naliczona')
        print('')
        return pkt
    lit=[]
    for i in range(0,ile):
        try:
            mnoznik=int(input('Podaj mnożnik dla podanej litery: '))
            if mnoznik!=2 and mnoznik!=3:
                print('Nieprawidłowy wybór, premia nie naliczona')
                print('')
                return pkt
        except ValueError:
            print('')
            print ('Nieprawidłowy wybór, premia nie naliczona')
            print('')
            return pkt
        lit.append(input('Podaj literę '+str(i+1)+' : '))
        if lit[i] in slowo:
            if mnoznik==2:
                pkt+=litery[lit[i]]
            elif mnoznik==3:
                pkt+=litery[lit[i]]*2
        else:
            print('Brak takiej litery w słowie')
    return pkt

def premia_slowna(pkt):
    try:
        mnoznik=int(input('Mnożnik premii słownej: '))
        print('')
        if mnoznik!=2 and mnoznik!=3:
            print('Nieprawidłowy wybór, premia nia naliczona')
            print('')
            return pkt
    except ValueError:
        print('')
        print ('Nieprawidłowy wybór, premia nie naliczona')
        print('')
        return pkt
    if mnoznik==2:
        pkt*=2
        return pkt
    elif mnoznik==3:
        pkt*=3
        return pkt

def punkty(slowo):
    '''Oblicza punkty za słowo i premie'''
    litery={'a':1, 'ą':5, 'b':3, 'c':2,
            'ć':6, 'd':2, 'e':1, 'ę':5,
            'f':5, 'g':3, 'h':3, 'i':1,
            'j':3, 'k':2, 'l':2, 'ł':3,
            'm':2, 'n':1, 'ń':7, 'o':1,
            'ó':5, 'p':2, 'r':1, 's':1,
            'ś':5, 't':2, 'u':3, 'w':1,
            'y':2, 'z':1, 'ź':9, 'ż':5}
    
    pkt=0
    for litera in slowo:
        pkt+=litery[litera]
    print('[1] Premia literowa')
    print('[2] Premia słowna')
    print('[3] Premia literowa i słowna')
    print('[0] Brak premii')
    try:
        t=int(input('Premia: '))
        print('')
        if t<0 and t>3:
            print('Nieprawidłowy wybór, premia nia naliczona')
            print('')
            return pkt
    except ValueError:
        print('')
        print ('Nieprawidłowy wybór, premia nie naliczona')
        print('')
        return pkt
    if t==1:
        pkt=premia_literowa(slowo,pkt,litery)
    if t==2:
        pkt=premia_slowna(pkt)
        print('')
    if t==3:
        pkt=premia_literowa(slowo,pkt,litery)
        pkt=premia_slowna(pkt)
        return pkt
    return pkt

slownik=wczytaj_slownik()
wyb=-1
while wyb!=0:
    sprawdz=wprowadz_slowo()
    if sprawdz=='0':
        break
    wyb=wybor()
    if wyb==1:
        print(istnieje(sprawdz))
        print('')
    if wyb==2:
        print(punkty(sprawdz))
        print('')
    if wyb==3:
        if istnieje(sprawdz)=='Słowo istnieje':
            print('Słowo istnieje')
            print('')
            print('Wartość punktowa słowa '+str(punkty(sprawdz)))
        else:
            print('Słowo nie istnieje')
            print('')
print('Koniec pracy')

    