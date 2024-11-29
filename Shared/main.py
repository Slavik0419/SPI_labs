import unittest
import Data.lab1.lab1_main as lab1
import Data.Lab2.runner as lab2
import Data.lab3.lab3_main as lab3
import Data.lab4.lab4_main as lab4
import Data.lab5.lab5_main as lab5
import Data.lab7.lab7_main as lab7
import Data.lab8.lab8_main as lab8

def run_lab(lab_number):
    if lab_number == 1:
        lab1.main()
    elif lab_number == 2:
        lab2.main()
    elif lab_number == 3:
        lab3.run_ascii_art_generator()
    elif lab_number == 4:
        lab4.run_ascii_art_generator()
    elif lab_number == 5:
        lab5.main()
    elif lab_number == 6:
        run_lab6_tests()  # Викликаємо функцію для запуску тестів
    elif lab_number == 7:
        lab7.run_lab7()
    elif lab_number == 8:
        lab8.main()
    else:
        print("Неправильний номер лабораторної роботи.")

def run_lab6_tests():
    # Створюємо тестовий лоудер і вказуємо директорію тестів
    loader = unittest.TestLoader()
    tests = loader.discover("Data.lab6.UTest")  # Вказуємо шлях до папки з тестами
    test_runner = unittest.TextTestRunner()
    test_runner.run(tests)

if __name__ == "__main__":
    print("Виберіть лабораторну для запуску:")
    lab_number = int(input("1 - Lab1, 2 - Lab2, 3 - Lab3, 4 - Lab4, 5 - Lab5, 6 - Lab6 (Unit Tests), 7 - Lab7, 8 - Lab8: "))
    run_lab(lab_number)
