import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            dvd = DigitalVideoDisc(f"DVD {i+1}")
            cart.add_dvd(dvd)
        dvd_21 = DigitalVideoDisc("DVD 21")
        self.assertFalse(cart.add_dvd(dvd_21))

    def test_discount_calculation(self):
        cart = Cart()
        dvd = DigitalVideoDisc("Test DVD")
        dvd.cost = 100.0
        cart.add_dvd(dvd)
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80.0)

    def test_discount_invalid_percent(self):
        cart = Cart()
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

    def test_sort_by_title(self):
        cart = Cart()
        d1 = DigitalVideoDisc("Zootopia")
        d2 = DigitalVideoDisc("Aladdin")
        cart.add_dvd(d1)
        cart.add_dvd(d2)
        cart.sort_by_title()
        self.assertEqual(cart.items[0].title, "Aladdin")
        self.assertEqual(cart.items[1].title, "Zootopia")

    def test_sort_by_cost(self):
        cart = Cart()
        d1 = DigitalVideoDisc("Cheap DVD")
        d1.cost = 10.0
        d2 = DigitalVideoDisc("Expensive DVD")
        d2.cost = 50.0
        cart.add_dvd(d1)
        cart.add_dvd(d2)
        cart.sort_by_cost()
        self.assertEqual(cart.items[0].cost, 50.0)
        self.assertEqual(cart.items[1].cost, 10.0)

if __name__ == '__main__':
    unittest.main()
