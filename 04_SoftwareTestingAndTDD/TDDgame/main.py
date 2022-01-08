import unittest

'''

'''

from game.Enemy import Enemy

class EnemyConstructorTest(unittest.TestCase):

    # def setUp(self):
    #     print("M-am apelat inainte de functie")
    #     self.orc = Enemy("Orc")
    #
    # def tearDown(self):
    #     print("M-am apelat la finalul fiecarei functii")

    def test_EnemyName(self):
        enemy1 = Enemy("Orc")
        result = enemy1.name
        self.assertEqual(result, "Orc")

    def test_EnemyLives(self):
        enemy1 = Enemy("Orc")
        result = enemy1.lives
        self.assertEqual(result, 10)

    def test_receive_dmg(self):
        orc = Enemy("Ben")
        orc.receive_dmg()
        result = orc.lives
        self.assertEqual(result, 9)


    def test_is_alive(self):
        orc = Enemy("Ben10")
        result = orc.is_alive()
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
    