import sys
import time
import math
import random
from collections import Counter

from PySide6.QtCore import Qt, QSize, QMetaObject, QCoreApplication
from PySide6.QtWidgets import QMainWindow, QApplication, QRadioButton, QLabel, QVBoxLayout, QWidget, QGridLayout, \
    QSizePolicy, QTextBrowser, QLineEdit, QPushButton
from PySide6 import QtUiTools

def rabinMiller(n, trials=5):
    s = n - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1

    for trial in range(trials):
        a = random.randrange(2, n - 1)
        v = pow(a, s, n)
        if v != 1:
            i = 0
            while v != n - 1:
                if i == t - 1:
                    return False
                else:
                    i += 1
                    v = (v * v) % n
    return True

def is_prime(n):
    if n < 2:
        return False
    # Примерно в 1/3 случаев простоту числа можно быстро определить путем деления на первые несколько десятков простых чисел
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if n in lowPrimes:
        return True

    for prime in lowPrimes:
        if n % prime == 0:
            return False

    return rabinMiller(n)

def pollard_rho(n):
    f = lambda x: (x * x + c) % n

    while True:
        x, c = random.randrange(1, n), random.randrange(1, n)

        y = f(x)
        while (d := math.gcd(abs(x - y), n)) == 1:
            x, y = f(x), f(f(y))

        if d != n:
            return d

def get_factors(n):
    if is_prime(n) or n == 1:
        return Counter([n])
    r = pollard_rho(n)
    return get_factors(r) + get_factors(n // r)

def get_dividers(n):
    d = []
    for k,v in get_factors(n).items():
        for i in range(v):
            d.append(k)
    return d

def trial_division(n):
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    if n > 1:
        factors.append(n)
    return factors

def fermat_factorization(n):
    # Проверяем, является ли число чётным
    if n % 2 == 0:
        return 2, n // 2

    # Начинаем с a, которое равно округлённому вверх квадратному корню из n
    a = math.isqrt(n) + 1

    while True:
        # Вычисляем b^2 = a^2 - n
        b_squared = a * a - n
        b = math.isqrt(b_squared)

        # Проверяем, является ли b_squared полным квадратом
        if b * b == b_squared:
            return a - b, a + b
        else:
            a += 1

def get_all_factors(n):
    factors = []  # Множество для хранения всех делителей
    stack = [n]  # Стек для чисел, которые нужно разложить

    while stack:
        current = stack.pop()
        if current == 1:
            continue

        # Если текущее число простое, добавляем его в множители
        if is_prime1(current):
            factors.append(current)
            continue

        # Ищем делители с помощью метода Ферма
        factor1, factor2 = fermat_factorization(current)

        # Добавляем найденные делители в стек для дальнейшего разложения
        stack.append(factor1)
        stack.append(factor2)

    return sorted(factors)

def is_prime1(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =QtUiTools.QUiLoader().load("design.ui", self)
        self.setCentralWidget(self.ui)
        self.ui.show()

        # Применение стилей
        self.setStyleSheet("""
                    QLineEdit#le_entry_dells {
                        font-size: 16px;
                        min-height: 60px;  /* Чтобы вместить многострочный вывод */
                    }
                    QMainWindow {
                        background-color: #f5f5f5;
                        font-family: 'Segoe UI';
                    }
                    QLabel#lbl_temp {
                        font-size: 28px;
                        font-weight: bold;
                        color: #2c3e50;
                        border: 1px solid #cccccc;
                        border-radius: 4px;
                        background-color: white;
                        padding: 5px 10px;
                    }
                    QLineEdit {
                        font-size: 20px;
                        border: 1px solid #cccccc;
                        border-radius: 4px;
                        padding: 5px;
                        background-color: white;
                    }
                    QPushButton {
                        font-size: 18px;
                        font-weight: bold;
                        color: white;
                        background-color: #4CAF50;
                        border: none;
                        border-radius: 4px;
                        padding: 10px;
                        min-width: 50px;
                    }
                    QPushButton:hover {
                        background-color: #45a049;
                    }
                    QPushButton:pressed {
                        background-color: #3d8b40;
                    }
                    QRadioButton {
                        font-size: 14px;
                        spacing: 5px;
                    }
                    QTextEdit#le_entry_dells {
                        font-size: 14px;
                        border: 1px solid #cccccc;
                        border-radius: 4px;
                        padding: 5px;
                        background-color: white;
                    }
                    
                    QScrollBar:vertical {
                        width: 12px;
                        background: #f1f1f1;
                        border-radius: 6px;
                    }
                    
                    QScrollBar::handle:vertical {
                        background: #a0a0a0;
                        min-height: 20px;
                        border-radius: 6px;
                    }
                    
                    QScrollBar::handle:vertical:hover {
                        background: #808080;
                    }
                    QTextBrowser {
                        font-size: 12px;
                        border: none;
                        background-color: transparent;
                    }
                    #btn_C, #btn_back {
                        background-color: #f44336;
                    }
                    #btn_C:hover, #btn_back:hover {
                        background-color: #d32f2f;
                    }
                    #btn_C:pressed, #btn_back:pressed {
                        background-color: #b71c1c;
                    }
                    #btn_ans {
                        background-color: #2196F3;
                    }
                    #btn_ans:hover {
                        background-color: #1976D2;
                    }
                    #btn_ans:pressed {
                        background-color: #0D47A1;
                    }
                """)
        # digits
        self.ui.btn_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.btn_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.btn_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.btn_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.btn_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.btn_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.btn_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.btn_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.btn_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.btn_9.clicked.connect(lambda: self.add_digit('9'))

        # actions
        self.ui.btn_C.clicked.connect(lambda: self.clear_all())

        # math
        self.ui.btn_ans.clicked.connect(lambda:self.calculate())

    def add_digit(self, btn_text:str) -> None:
        if self.ui.lbl_temp.text() == '0':
            self.ui.lbl_temp.setText(btn_text)
        else:
            self.ui.lbl_temp.setText(self.ui.lbl_temp.text() + btn_text)

    def clear_all(self) -> None:
        self.ui.lbl_temp.clear()

    def calculate(self):
        try:
            number = int(self.ui.lbl_temp.text())
            if number < 1:
                self.ui.le_entry_dells.setHtml("<div style='color:red; font-size:14pt;'>Введите число > 0</div>")
                return

            start_time = time.perf_counter()  # Более точное время

            if self.ui.radioButton.isChecked():  # Поллард
                method_name = "Ро-алгоритм Полларда"
                factors = get_dividers(number)
            elif self.ui.radioButton_2.isChecked():  # Пробное деление
                method_name = "Метод пробного деления"
                factors = trial_division(number)
            elif self.ui.radioButton_3.isChecked():  # Ферма
                method_name = "Метод Ферма"
                factors = get_all_factors(number)
            else:
                return

            exec_time = time.perf_counter() - start_time

            # Форматируем вывод
            factor_counts = Counter(factors)
            prime_factors = []
            for factor, count in sorted(factor_counts.items()):
                if count > 1:
                    prime_factors.append(f"{factor}<sup>{count}</sup>")
                else:
                    prime_factors.append(str(factor))

            # Форматируем время выполнения
            if exec_time < 0.001:
                time_str = f"{exec_time * 1e6:.2f} μs"
            elif exec_time < 1:
                time_str = f"{exec_time * 1e3:.2f} ms"
            else:
                time_str = f"{exec_time:.5f} s"

            # Создаем HTML-контент
            html_content = f"""
            <div style='font-family: Segoe UI; font-size: 14pt;'>
                <div style='margin-bottom: 10px; padding: 5px; background-color: #f8f9fa; border-radius: 4px;'>
                    <p><b>Метод:</b> {method_name}</p>
                    <p><b>Время выполнения:</b> <span style='color: #2c7be5;'>{time_str}</span></p>
                </div>

                <p><b>Исходное число:</b> {number}</p>
                <p><b>Каноническое разложение:</b> {' × '.join(prime_factors)}</p>

                <div style='margin-top: 10px;'>
                    <b>Все делители ({len(set(factors))}):</b>
                    <div style='max-height: 150px; overflow-y: auto; border: 1px solid #eee; padding: 5px; margin-top: 5px;'>
                        {', '.join(sorted(map(str, set(factors)), key=int))}
                    < / div >
                < / div >
            < / div >
            """

            self.ui.le_entry_dells.setHtml(html_content)

        except ValueError:
            self.ui.le_entry_dells.setHtml("<div style='color:red; font-size:14pt;'>Ошибка: введите целое число</div>")


app = QApplication(sys.argv)
w = AppWindow()
sys.exit(app.exec())
