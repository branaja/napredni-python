import pickle


def require(method):
    def isfloat(*args):
        if not isinstance(args[-1], float) and not isinstance(args[-1], int):
            raise TypeError("Argument nije broj")
        return method(*args)
    return isfloat


class Zaposlenik:
    def __init__(self,ime_i_prezime, placa):
        self.ime, self.prezime = ime_i_prezime.split()
        self.placa = placa

    @require
    def daj_povisicu(self, postotak):
        self.placa = self.placa * (1 + postotak / 100)

    def porez(self):
        return 0.24 * self.placa

    def __str__(self):
        return "{} {}". format(self.ime, self.prezime)

    __repr__ = __str__


def velika(method):
    def promijeni(*args, **kw):
        result = method(*args, **kw)
        return result.upper()
    return promijeni


class Poduzece:
    def __init__(self, ime, lokacija):
        self.ime = ime
        self.lokacija = lokacija
        self.zaposlenici = []

    def dodaj_zaposlenika(self, zaposlenik):
        if zaposlenik in self.zaposlenici:
            raise ErrZap("Zaposlenik {} već postoji".format(zaposlenik))
        self.zaposlenici.append(zaposlenik)

    def izbaci_zaposlenika(self, ime, prezime):
        for i in self.zaposlenici:
            if i.ime == ime and i.prezime == prezime:
                self.zaposlenici.remove(i)
                return
        raise ErrZap("Zaposlenik {} {} ne postoji".format(ime, prezime))

    @require
    def daj_povisicu_svima(self, postotak):
        for i in self.zaposlenici:
            i.daj_povisicu(postotak)

    def ukupan_porez(self):
        return sum(zap.porez() for zap in self.zaposlenici)
        '''
        ukupno = 0
        for i in self.zaposlenici:
            ukupno += i.porez()
        '''

    @velika
    def __str__(self):
        return "poduzeće: {}, lokacija: {}, zaposlenici: {}".format(self.ime, self.lokacija, ", ".join(str(zap) for zap in self.zaposlenici))

    def __iter__(self):
        self.tren = 0
        return  self

    def __next__(self):
        zap = self.tren
        self.tren += 1
        if self.tren > len(self.zaposlenici):
            raise StopIteration
        return self.zaposlenici[zap]


class Student(Zaposlenik):
    def porez(self):
        return self.placa * 0.10


class ErrZap(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


if __name__ == "__main__":
    a = Zaposlenik("Pero Perić", 9000)
    #a.daj_povisicu(15)
    print(a.porez())
    z = Poduzece("PBZ", "Zagreb")
    print(z.ime)

    print(z)

    z.dodaj_zaposlenika(a)
    print (z.ukupan_porez())
    b = Student("Ana Anić", 5000)
    z.dodaj_zaposlenika(b)

    print(z)

    z.izbaci_zaposlenika("Pero", "Perić")
    try:
        z.izbaci_zaposlenika("Pero", "Perić")
    except ErrZap as ez:
        print(ez)

    print(z.ukupan_porez())
    z.dodaj_zaposlenika(a)
    c = Zaposlenik("Cvita Cvitić", 9000)
    d = Zaposlenik("Danica Danić", 9000)

    z.dodaj_zaposlenika(c)
    z.dodaj_zaposlenika(d)

    print(z.ukupan_porez())
    z.daj_povisicu_svima(5)
    print(z.ukupan_porez())

    try:
        d2 = Zaposlenik("Danica Danić", 7000)
        z.dodaj_zaposlenika(d2)
    except ErrZap as ez:
        print(ez)
        ez.args

    for zap in z:
        print(zap)

    print(z)

    with open("poduzece.dat", "wb") as file:
        pickle.dump(z, file)