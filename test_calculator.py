import unittest
from calculator import dodaj, odejmij, pomnoz


class TestCalculator(unittest.TestCase):
    
    def test_dodaj(self):
        self.assertEqual(dodaj(2, 3), 5)
        self.assertEqual(dodaj(-1, 1), 0)
        self.assertEqual(dodaj(0, 0), 0)

    def test_odejmij(self):
        self.assertEqual(odejmij(5, 3), 2)
        self.assertEqual(odejmij(0, 0), 0)
        self.assertEqual(odejmij(-1, -1), 0)

    def test_dodaj_i_odejmij(self):
        result = odejmij(dodaj(10, 5), 3)
        self.assertEqual(result, 12)

    def test_pomnoz(self):
        self.assertEqual(pomnoz(2, 3), 6)
        self.assertEqual(pomnoz(-1, 5), -5)
        self.assertEqual(pomnoz(0, 9), 0)
