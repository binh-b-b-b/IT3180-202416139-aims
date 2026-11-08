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

if __name__ == '__main__':
    unittest.main()
