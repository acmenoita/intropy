import unittest
from jar import Jar

class TestJar(unittest.TestCase):
    def test_init(self):
        # Teste inicialização padrão e personalizada
        jar = Jar()
        self.assertEqual(jar.capacity, 12)
        self.assertEqual(jar.size, 0)

        jar_custom = Jar(20)
        self.assertEqual(jar_custom.capacity, 20)

        # Teste valores inválidos
        with self.assertRaises(ValueError):
            Jar(-1)

        with self.assertRaises(ValueError):
            Jar("invalid")

    def test_str(self):
        # Teste a representação em string
        jar = Jar()
        self.assertEqual(str(jar), "")
        jar.deposit(3)
        self.assertEqual(str(jar), "🍪🍪🍪")
        jar.withdraw(1)
        self.assertEqual(str(jar), "🍪🍪")

    def test_deposit(self):
        # Teste a funcionalidade de depósito
        jar = Jar()
        jar.deposit(5)
        self.assertEqual(jar.size, 5)

        # Teste exceder a capacidade
        with self.assertRaises(ValueError):
            jar.deposit(8)  # Excede a capacidade padrão de 12

    def test_withdraw(self):
        # Teste a funcionalidade de retirada
        jar = Jar()
        jar.deposit(5)
        jar.withdraw(3)
        self.assertEqual(jar.size, 2)

        # Teste retirar mais do que há no jarro
        with self.assertRaises(ValueError):
            jar.withdraw(5)  # Não há cookies suficientes

if __name__ == "__main__":
    unittest.main()
