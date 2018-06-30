def load_words_dictionary():
    '''Wczytanie słownika'''
    print('Słownik pochodzi ze strony www.sjp.pl')
    print('Inicjalizacja słownika...')
    with open("slowa.txt", 'r', encoding='utf-8') as f:
        words_dictionary=f.readlines()
    words_dictionary=[x.strip() for x in words_dictionary]
    print('Słownik gotowy')
    print('')
    return words_dictionary

def word_imput():
    '''Wczytanie słowa od użytkownika'''
    word=input('Podaj słowo do sprawdzenia lub 0, aby zakończyć: ')
    word=word.lower()
    print('')
    return word

def decision():
    '''Odpowiada za wybór funkcji programu'''
    print('Wybierz, co chcesz zrobić')
    print('[1] Sprawdź czy istnieje')
    print('[2] Oblicz punkty za słowo')
    print('[3] Sprawdź i oblicz')
    print('[4] Wyświetl losowe słowo')
    print('[0] Wyjście')
    try:
        decision=int(input('Wybór: '))
        print('')
        if decision>4 or decision<0: #zmienić w przypadku dodania funkcji
            print('Nieprawidłowy wybór')
            print('')
            return None
        return decision
    except ValueError:
        print('')
        print ('Nieprawidłowy wybór')
        print('')
        return None

def exist(word):
    if word in words_dictionary: 
        return 'Słowo istnieje'
    else:
        return'Słowo nie istnieje'

def letter_prem(word,pkt,letters):
    try:
        how_many=int(input('Liczba premii literowych: '))
        print('')
        if how_many<0:
            print('Nieprawidłowy wybór, premia nia naliczona')
            print('')
            return pkt
    except ValueError:
        print('')
        print ('Nieprawidłowy wybór, premia nie naliczona')
        print('')
        return pkt
    lit=[]
    for i in range(how_many):
        try:
            multipler=int(input('Podaj mnożnik dla podanej letters: '))
            if multipler!=2 and multipler!=3:
                print('Nieprawidłowy wybór, premia nie naliczona')
                print('')
                return pkt
        except ValueError:
            print('')
            print ('Nieprawidłowy wybór, premia nie naliczona')
            print('')
            return pkt
        lit.append(input('Podaj literę '+str(i+1)+' : '))
        if lit[i] in word:
            if multipler==2:
                pkt+=letters[lit[i]]
            elif multipler==3:
                pkt+=letters[lit[i]]*2
        else:
            print('Brak takiej letters w słowie')
    return pkt

def word_prem(pkt):
    try:
        multipler=int(input('Mnożnik premii słownej: '))
        print('')
        if multipler!=2 and multipler!=3:
            print('Nieprawidłowy wybór, premia nia naliczona')
            print('')
            return pkt
    except ValueError:
        print('')
        print ('Nieprawidłowy wybór, premia nie naliczona')
        print('')
        return pkt
    if multipler==2:
        pkt*=2
        return pkt
    elif multipler==3:
        pkt*=3
        return pkt

def punkty(word):
    '''Oblicza punkty za słowo i premie'''
    letters={'a':1, 'ą':5, 'b':3, 'c':2,
            'ć':6, 'd':2, 'e':1, 'ę':5,
            'f':5, 'g':3, 'h':3, 'i':1,
            'j':3, 'k':2, 'l':2, 'ł':3,
            'm':2, 'n':1, 'ń':7, 'o':1,
            'ó':5, 'p':2, 'r':1, 's':1,
            'ś':5, 't':2, 'u':3, 'w':1,
            'y':2, 'z':1, 'ź':9, 'ż':5}
    
    pkt=0
    for litera in word:
        pkt+=letters[litera]
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
        pkt=letter_prem(word,pkt,letters)
    if t==2:
        pkt=word_prem(pkt)
        print('')
    if t==3:
        pkt=letter_prem(word,pkt,letters)
        pkt=word_prem(pkt)
        return pkt
    return pkt


import random
words_dictionary=load_words_dictionary()
wyb=-1
while wyb!=0:
    word=word_imput()
    if word=='0':
        break
    wyb=decision()
    if wyb==1:
        print(exist(word))
        print('')
    elif wyb==2:
        print('Wartość punktowa słowa: '+str(punkty(word)))
        print('')
    elif wyb==3:
        if exist(word)=='Słowo istnieje':
            print('Słowo istnieje')
            print('')
            print('Wartość punktowa słowa: '+str(punkty(word)))
            print('')
        else:
            print('Słowo nie istnieje')
            print('')
    elif wyb==4:
        i=random.randint(0,len(words_dictionary))
        print (words_dictionary[i])
        print('')
print('Koniec pracy')   