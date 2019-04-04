import unittest
from poduz import *


class TestPoduzece(unittest.TestCase):
    def test_porez(self):
        p = Poduzece("PBZ", "Zagreb")
        a = Zaposlenik("Pero Perić", 9000)
        p.dodaj_zaposlenika(a)
        self.assertEqual(p.ukupan_porez(), 2160)

    def test_str(self):
        p = Poduzece("PBZ", "Zagreb")
        a = Zaposlenik("Pero Perić", 9000)
        p.dodaj_zaposlenika(a)
        self.assertEqual(str(p), "PODUZEĆE: PBZ, LOKACIJA: ZAGREB, ZAPOSLENICI: PERO PERIĆ")

    def test_exception(self):
        p = Poduzece("PBZ", "Zagreb")
        a = Zaposlenik("Pero Perić", 9000)
        p.dodaj_zaposlenika(a)
        with self.assertRaises(ErrZap):
            p.dodaj_zaposlenika(a)
        with self.assertRaises(TypeError):
            p.daj_povisicu_svima("qqq")


if __name__ == '__main__':
    unittest.main()