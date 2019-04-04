def fja(filename):
    with open(filename) as f:
        counter = 0
        ime = {}
        prezime = {}
        for line in f:
            osoba = line.split(' ')
            counter += 1
            if osoba[0] in ime:
                ime[osoba[0]] += 1
            else:
                ime [osoba[0]] = 1
            if osoba[1] in prezime:
                prezime[osoba[1][:-1]] += 1
            else:
                prezime[osoba[1][:-1]] = 1
    maxime = 0
    for i in ime:
        if ime[i] > maxime:
            maxime = ime[i]
            najcesceime = i

    maxprezime = 0
    for i in prezime:
        if prezime[i] > maxprezime:
            maxprezime = prezime[i]
            najcesceprezime = i
    print("najčešće ime: {}, najčešće prezime: {}, broj redaka: {}".format(najcesceime,najcesceprezime, counter))



fja("input.txt")