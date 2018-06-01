def wczytaj_slownik():
    slownik=[]
    with open("slowa.txt") as f:
        data = f.readlines()
    for line in data:
        slownik.append(line)
    return slownik

def wprowadz_slowo():
    slowo=input('Podaj slowo do sprawdzenia lub 0 aby wyjść: ')
    return slowo

def wybor():
    print ('Wybierz co chcesz zrobić')
    print ('[1] Sprawdzić czy istnieje')
    wybor=input('Decyzja: ')
    return int(wybor)

slownik=wczytaj_slownik()
a='a'
print ('NIE DZIAŁAJĄ POLSKIE ZNAKI')
if a!=0:
    a=wprowadz_slowo()
    wybor=wybor()
    if wybor==1:
        flag=0
        for i in slownik:
            if a==i:
                flag=1
        if flag==1:
            print ('Slowo istnieje')
        else:
            print ('Słowo nie istnieje')

    