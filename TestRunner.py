from Lesson_12_1 import Runner
import unittest
# Изменяемые данные для теста
number = 10
compare_walk = 50
compare_run = 100

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        resrun = Runner("Тест Walk")
        for _ in range(number):
            resrun.walk()
        self.assertEqual(resrun.distance, compare_walk)

    def test_run(self):
        resrun = Runner("Тест Run")
        for _ in range(number):
            resrun.run()
        self.assertEqual(resrun.distance, compare_run)

    def test_challenge(self):
        resrun = Runner("Runner")
        reswalk = Runner("Walker")

        for _ in range(number):
            resrun.run()
            reswalk.walk()

        self.assertNotEqual(resrun.distance, reswalk.distance)


if __name__ == '__main__':
    unittest.main()