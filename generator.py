import random

def generate_Instance(V,r):
    l = []
    for i in range(V):
        #wygeneruj wierzcholek postaci (x, y)
        x = random.randint(1,r)
        y = random.randint(1,r)
        #dodaj wierzcholek do listy wierzcholkow
        l.append((x,y))
    #zapisz liczbe wierzcholkow oraz liste wierzcholkow do pliku zewnetrzengo (.bench)
    f = open("a.bench","w")
    f.write(str(V)+"\n")
    for i in range(V):
        f.write(str(l[i][0])+" "+str(l[i][1])+"\n")
    f.close()