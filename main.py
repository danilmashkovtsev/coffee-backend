import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer

from coffee import Ui_MainWindow
from win2 import Ui_Dialog
from win3 import Ui_Dialog3
from win4 import Ui_Dialog4
from win5 import Ui_Dialog5

# Менять файлы кроме main нельзя. Там интерфейс. Он сбростится если буду изменять его.

type_coffee = ""

# -------------------------------------------------------------------------
class CoffeeStrategy():
    def __init__(self, coffee_machine, sugar_count, syrup_type):
        self.coffee_machine = coffee_machine
        self.sugar_count = sugar_count
        self.syrup_type = syrup_type

    def make_coffee(self):  # Это база для всех
        self.heat_water()
        self.grind_coffee()
        self.stir_coffee()
        self.pour_coffee()

    def heat_water(self):
        print('Подогреваем воду (50 мл)')

    def grind_coffee(self):
        print('Перемалываем кофе (10 грамм)')

    def stir_coffee(self):
        print('Делаем основу кофе')

    def pour_coffee(self):
        print('Выливаем основу кофе в кружку')

    def add_syrup(self, syrup_type):
        if syrup_type == '1':
            print("Добавляем карамельный сироп")
        elif syrup_type == '2':
            print("Добавляем шоколадный сироп")
        elif syrup_type == '3':
            print("Добавляем кокосовый сироп")
        elif syrup_type == '4':
            print("Добавляем ванильный сироп")
        elif syrup_type == '5':
            print("Добавляем банановый сироп")

    def add_sugar(self, sugar_count):
        if sugar_count != '0':
            print(f'Добавляем {sugar_count} ложек сахара')
        else:
            pass

    def use_ingredients(self):
        self.coffee_machine.water_amount -= 50
        self.coffee_machine.coffee_amount -= 10
        if self.syrup_type != '0':
            self.coffee_machine.syrup_amount[self.syrup_type] -= 1
        self.coffee_machine.sugar_amount -= int(self.sugar_count)

# --------------------------------------------------------------------------

class EspressoStrategy(CoffeeStrategy):
    def __init__(self, coffee_machine, sugar_count, syrup_type):
        super().__init__(coffee_machine, sugar_count, syrup_type)
        print("--- Выбрано эспрессо ---")

    def make_coffee(self):
        super().heat_water()
        super().grind_coffee()
        super().stir_coffee()
        super().pour_coffee()
        super().add_sugar(self.sugar_count)
        super().add_syrup(self.syrup_type)

# -------------------------------------------------------------------------

class DoubleEspressoStrategy(CoffeeStrategy):
    def __init__(self, coffee_machine, sugar_count, syrup_type):
        super().__init__(coffee_machine, sugar_count, syrup_type)
        print("--- Выбрано двойное эспрессо ---")

    def make_coffee(self):
        super().heat_water()
        super().grind_coffee()
        super().grind_coffee()
        super().stir_coffee()
        self.pour_coffee()
        super().add_sugar(self.sugar_count)
        super().add_syrup(self.syrup_type)

    def pour_coffee(self):
        self.coffee_machine.water_amount -= 50
        print("Выливаем двойную основу кофе")

# -------------------------------------------------------------------------

class AmericanoStrategy(CoffeeStrategy):
    def __init__(self, coffee_machine, sugar_count, syrup_type):
        super().__init__(coffee_machine, sugar_count, syrup_type)
        print("--- Выбрано американо ---")

    def make_coffee(self):
        super().heat_water()
        super().grind_coffee()
        super().stir_coffee()
        self.add_water()
        super().add_sugar(self.sugar_count)
        super().add_syrup(self.syrup_type)

    def add_water(self):
        self.coffee_machine.water_amount -= 100
        print("Добавляем кипяток (100 мл)")

# -------------------------------------------------------------------------

class MacchiatoStrategy(CoffeeStrategy):
    def __init__(self, coffee_machine, sugar_count, syrup_type):
        super().__init__(coffee_machine, sugar_count, syrup_type)
        print("--- Выбрано маккиато ---")

    def make_coffee(self):
        super().heat_water()
        super().grind_coffee()
        super().stir_coffee()
        self.milk()
        super().add_sugar(self.sugar_count)
        super().add_syrup(self.syrup_type)

    def milk(self):
        self.coffee_machine.milk_amount -= 100
        print("Взбиваем и добавляем молоко (100 мл)")

# -------------------------------------------------------------------------

class LatteStrategy(CoffeeStrategy):
    def __init__(self, coffee_machine, sugar_count, syrup_type):
        super().__init__(coffee_machine, sugar_count, syrup_type)
        print("--- Выбрано латте ---")

    def make_coffee(self):
        super().heat_water()
        super().grind_coffee()
        super().stir_coffee()
        self.milk()
        super().add_sugar(self.sugar_count)
        super().add_syrup(self.syrup_type)

    def milk(self):
        self.coffee_machine.milk_amount -= 200
        print("Взбиваем и добавляем молоко (200 мл)")

# -------------------------------------------------------------------------

class MoccachinoStrategy(CoffeeStrategy):
    def __init__(self, coffee_machine, sugar_count, syrup_type):
        super().__init__(coffee_machine, sugar_count, syrup_type)
        print("--- Выбрано мокачино ---")

    def make_coffee(self):
        self.chocolate()
        super().heat_water()
        super().grind_coffee()
        super().stir_coffee()
        self.milk()
        super().add_sugar(self.sugar_count)
        super().add_syrup(self.syrup_type)

    def milk(self):
        self.coffee_machine.milk_amount -= 200
        print("Взбиваем и добавляем молоко (200 мл)")

    def chocolate(self):
        self.coffee_machine.hot_chocolate -= 20
        print("Добавляем горячий шоколад (20 мл)")

# -------------------------------------------------------------------------

class RafStrategy(CoffeeStrategy):
    def __init__(self, coffee_machine, sugar_count, syrup_type):
        super().__init__(coffee_machine, sugar_count, syrup_type)
        print("--- Выбран раф ---")

    def make_coffee(self):
        super().heat_water()
        super().grind_coffee()
        super().stir_coffee()
        self.milk()
        super().add_sugar(self.sugar_count)
        super().add_syrup(self.syrup_type)

    def milk(self):
        self.coffee_machine.milk_amount -= 300
        print("Взбиваем молоко и сливки (300 мл)")
        print("Добавляем взбитые молоко и сливки")

# -------------------------------------------------------------------------

class CappuccinoStrategy(CoffeeStrategy):
    def __init__(self, coffee_machine, sugar_count, syrup_type):
        super().__init__(coffee_machine, sugar_count, syrup_type)
        print("--- Выбрано капучино ---")

    def make_coffee(self):
        super().heat_water()
        super().grind_coffee()
        super().stir_coffee()
        self.milk()
        super().add_sugar(self.sugar_count)
        super().add_syrup(self.syrup_type)

    def milk(self):
        self.coffee_machine.milk_amount -= 150
        print("Взбиваем и добавляем молоко (150 мл)")

# -------------------------------------------------------------------------

class VienneseStrategy(CoffeeStrategy):
    def __init__(self, coffee_machine, sugar_count, syrup_type):
        super().__init__(coffee_machine, sugar_count, syrup_type)
        print("--- Выбран венский кофе ---")

    def make_coffee(self):
        super().heat_water()
        super().grind_coffee()
        super().grind_coffee()
        super().stir_coffee()
        self.pour_coffee()
        self.milk()
        super().add_sugar(self.sugar_count)
        super().add_syrup(self.syrup_type)

    def milk(self):
        self.coffee_machine.milk_amount -= 150
        print("Взбиваем и добавляем молоко (150 мл)")

    def pour_coffee(self):
        self.coffee_machine.water_amount -= 50
        print("Выливаем двойную основу кофе")

# -------------------------------------------------------------------------

class HotChocolateStrategy(CoffeeStrategy):
    def __init__(self, coffee_machine, sugar_count, syrup_type):
        super().__init__(coffee_machine, sugar_count, syrup_type)
        print("--- Выбран горячий шоколад ---")

    def make_coffee(self):
        self.milk()
        super().add_sugar(self.sugar_count)
        super().add_syrup(self.syrup_type)

    def milk(self):
        self.coffee_machine.milk_amount -= 150
        self.coffee_machine.hot_chocolate -= 50
        print("Взбиваем шоколад и молоко (200 мл)")
        print("Добавляем взбитые шоколад и молоко")

# -------------------------------------------------------------------------

class CocoaStrategy(CoffeeStrategy):
    def __init__(self, coffee_machine, sugar_count, syrup_type):
        super().__init__(coffee_machine, sugar_count, syrup_type)
        print("--- Выбрано какао ---")

    def make_coffee(self):
        self.milk()
        super().add_sugar(self.sugar_count)
        super().add_syrup(self.syrup_type)

    def milk(self):
        self.coffee_machine.milk_amount -= 200
        self.coffee_machine.cocoa -= 50
        print("Взбиваем какао и молоко (250 мл)")
        print("Добавляем взбитые какао и молоко")

# -------------------------------------------------------------------------

class Coffee(QMainWindow):
    def __init__(self):
        # Запускаем главное окно
        super(Coffee, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QTimer(self)
        self.timer.setInterval(25)
        self.timer.timeout.connect(self.plus)
        self.progress = 0

        self.currentStrategy = None # Выбор кофе

        self.sugar_count = '0'
        self.syrup_type = '1'

        self.water_amount = 5000  # количество воды в мл
        self.coffee_amount = 500  # количество кофе в граммах
        self.sugar_amount = 100  # количество сахара в ложках
        self.syrup_amount = {'1': 5, '2': 5, '3': 5, '4': 5, '5': 5} # количество сиропа каждого типа
        self.milk_amount = 1000 # количество молока
        self.hot_chocolate = 200 # количество шоколада
        self.cocoa = 100 # количество какао


        self.ui.btn_start.clicked.connect(self.openWindow2)

    def setStrategy(self, strategy: CoffeeStrategy):
        self.currentStrategy = strategy

    def plus(self): # Таймер для прогрессбара
        if self.progress == 0:
            self.new_window = QtWidgets.QDialog()
            self.ui_window = Ui_Dialog4()
            self.ui_window.setupUi(self.new_window)
            self.new_window.show()

        self.progress += 1
        self.ui_window.progressBar.setValue(self.progress)
        if self.progress == 100:
            self.timer.stop()
            self.openWindow5()
            self.progress = 0


    def openWindow2(self): # Окно выбора кофе
        self.syrup_type = '0'
        self.sugar_count = '0'
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.close()
        self.ui_window.btn_end.clicked.connect(self.openWindow1)
        self.ui_window.btn_coffee_1.clicked.connect(self.openWindow3_1)
        self.ui_window.btn_coffee_2.clicked.connect(self.openWindow3_2)
        self.ui_window.btn_coffee_3.clicked.connect(self.openWindow3_3)
        self.ui_window.btn_coffee_4.clicked.connect(self.openWindow3_4)
        self.ui_window.btn_coffee_5.clicked.connect(self.openWindow3_5)
        self.ui_window.btn_coffee_6.clicked.connect(self.openWindow3_6)
        self.ui_window.btn_coffee_7.clicked.connect(self.openWindow3_7)
        self.ui_window.btn_coffee_8.clicked.connect(self.openWindow3_8)
        self.ui_window.btn_coffee_9.clicked.connect(self.openWindow3_9)
        self.ui_window.btn_coffee_10.clicked.connect(self.openWindow3_10)
        self.ui_window.btn_coffee_11.clicked.connect(self.openWindow3_11)
        self.ui_window.btn_coffee_12.clicked.connect(self.openWindow3_12)


    def openWindow5(self): # Последнее окно
        print("--- Напиток готов ---\n")
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog5()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.btn_home.clicked.connect(self.openWindow1)

    def openWindow4(self): # Прогрессбар
        self.timer.start()
        if type_coffee == "espresso":
            self.setStrategy(EspressoStrategy(self, self.sugar_count, self.syrup_type))
        elif type_coffee == "double_espresso":
            self.setStrategy(DoubleEspressoStrategy(self, self.sugar_count, self.syrup_type))
        elif type_coffee == "americano":
            self.setStrategy(AmericanoStrategy(self, self.sugar_count, self.syrup_type))
        elif type_coffee == "macchiato":
            self.setStrategy(MacchiatoStrategy(self, self.sugar_count, self.syrup_type))
        elif type_coffee == "latte":
            self.setStrategy(LatteStrategy(self, self.sugar_count, self.syrup_type))
        elif type_coffee == "moccachino":
            self.setStrategy(MoccachinoStrategy(self, self.sugar_count, self.syrup_type))
        elif type_coffee == "raf":
            self.setStrategy(RafStrategy(self, self.sugar_count, self.syrup_type))
        elif type_coffee == "cappuccino":
            self.setStrategy(CappuccinoStrategy(self, self.sugar_count, self.syrup_type))
        elif type_coffee == "viennese":
            self.setStrategy(VienneseStrategy(self, self.sugar_count, self.syrup_type))
        elif type_coffee == "hot_chocolate":
            self.setStrategy(HotChocolateStrategy(self, self.sugar_count, self.syrup_type))
        elif type_coffee == "cocoa":
            self.setStrategy(CocoaStrategy(self, self.sugar_count, self.syrup_type))
        else:
            return



        if self.currentStrategy:
            self.currentStrategy.make_coffee()
            self.currentStrategy.use_ingredients()


    # Проблемная часть. Не могу объеденить в функцию, так как self.ui_window.btn_home.clicked.connect(self.openWindow1)
    # Нельзя передать аргумент. А надо задавать иконки.
    def openWindow3_1(self):
        global type_coffee
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/espresso.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        if self.water_amount < 50 or self.coffee_amount < 10:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.syrup_type != '0' and self.syrup_amount[self.syrup_type] < 1:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif int(self.sugar_count) > self.sugar_amount:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        else:
            self.ui_window.btn_make.clicked.connect(self.openWindow4)
            self.ui_window.btn_back.clicked.connect(self.openWindow2)

        type_coffee = "espresso"

        def change():
            self.sugar_count = self.ui_window.spinBox1.text() # Используйте value() для получения числа
            self.syrup_type = self.ui_window.spinBox2.text()

            if self.ui_window.spinBox2.text() == "1":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/caramel.png"))
            elif  self.ui_window.spinBox2.text() == "2":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/chocolate.png"))
            elif  self.ui_window.spinBox2.text() == "3":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/coconut.png"))
            elif  self.ui_window.spinBox2.text() == "4":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/vanilla.png"))
            elif  self.ui_window.spinBox2.text() == "5":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/bananas.png"))
            elif  self.ui_window.spinBox2.text() == "0":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap(""))


        self.ui_window.spinBox2.valueChanged.connect(change)
        self.ui_window.spinBox1.valueChanged.connect(change)

    def openWindow3_2(self):
        global type_coffee
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/espresso.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        if self.water_amount < 100 or self.coffee_amount < 20:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.syrup_type != '0' and self.syrup_amount[self.syrup_type] < 1:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif int(self.sugar_count) > self.sugar_amount:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        else:
            self.ui_window.btn_make.clicked.connect(self.openWindow4)
            self.ui_window.btn_back.clicked.connect(self.openWindow2)


        type_coffee = "double_espresso"

        def change():
            self.sugar_count = self.ui_window.spinBox1.text()  # Используйте value() для получения числа
            self.syrup_type = self.ui_window.spinBox2.text()

            if self.ui_window.spinBox2.text() == "1":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/caramel.png"))
            elif self.ui_window.spinBox2.text() == "2":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/chocolate.png"))
            elif self.ui_window.spinBox2.text() == "3":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/coconut.png"))
            elif self.ui_window.spinBox2.text() == "4":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/vanilla.png"))
            elif self.ui_window.spinBox2.text() == "5":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/bananas.png"))
            elif self.ui_window.spinBox2.text() == "0":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap(""))



        self.ui_window.spinBox2.valueChanged.connect(change)
        self.ui_window.spinBox1.valueChanged.connect(change)

    def openWindow3_3(self):
        global type_coffee
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/americano.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        if self.water_amount < 150 or self.coffee_amount < 10:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.syrup_type != '0' and self.syrup_amount[self.syrup_type] < 1:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif int(self.sugar_count) > self.sugar_amount:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        else:
            self.ui_window.btn_make.clicked.connect(self.openWindow4)
            self.ui_window.btn_back.clicked.connect(self.openWindow2)


        type_coffee = "americano"

        def change():
            self.sugar_count = self.ui_window.spinBox1.text()  # Используйте value() для получения числа
            self.syrup_type = self.ui_window.spinBox2.text()

            if self.ui_window.spinBox2.text() == "1":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/caramel.png"))
            elif self.ui_window.spinBox2.text() == "2":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/chocolate.png"))
            elif self.ui_window.spinBox2.text() == "3":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/coconut.png"))
            elif self.ui_window.spinBox2.text() == "4":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/vanilla.png"))
            elif self.ui_window.spinBox2.text() == "5":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/bananas.png"))
            elif self.ui_window.spinBox2.text() == "0":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap(""))

        self.ui_window.spinBox2.valueChanged.connect(change)
        self.ui_window.spinBox1.valueChanged.connect(change)

    def openWindow3_4(self):
        global type_coffee
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/macchiato.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        if self.water_amount < 100 or self.coffee_amount < 20:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.syrup_type != '0' and self.syrup_amount[self.syrup_type] < 1:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif int(self.sugar_count) > self.sugar_amount:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.milk_amount < 100:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        else:
            self.ui_window.btn_make.clicked.connect(self.openWindow4)
            self.ui_window.btn_back.clicked.connect(self.openWindow2)

        type_coffee = "macchiato"

        def change():
            self.sugar_count = self.ui_window.spinBox1.text()  # Используйте value() для получения числа
            self.syrup_type = self.ui_window.spinBox2.text()

            if self.ui_window.spinBox2.text() == "1":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/caramel.png"))
            elif self.ui_window.spinBox2.text() == "2":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/chocolate.png"))
            elif self.ui_window.spinBox2.text() == "3":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/coconut.png"))
            elif self.ui_window.spinBox2.text() == "4":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/vanilla.png"))
            elif self.ui_window.spinBox2.text() == "5":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/bananas.png"))
            elif self.ui_window.spinBox2.text() == "0":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap(""))

        self.ui_window.spinBox2.valueChanged.connect(change)
        self.ui_window.spinBox1.valueChanged.connect(change)

    def openWindow3_5(self):
        global type_coffee
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/latte.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        if self.water_amount < 100 or self.coffee_amount < 20:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.syrup_type != '0' and self.syrup_amount[self.syrup_type] < 1:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif int(self.sugar_count) > self.sugar_amount:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.milk_amount < 200:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        else:
            self.ui_window.btn_make.clicked.connect(self.openWindow4)
            self.ui_window.btn_back.clicked.connect(self.openWindow2)

        type_coffee = "latte"

        def change():
            self.sugar_count = self.ui_window.spinBox1.text()  # Используйте value() для получения числа
            self.syrup_type = self.ui_window.spinBox2.text()

            if self.ui_window.spinBox2.text() == "1":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/caramel.png"))
            elif self.ui_window.spinBox2.text() == "2":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/chocolate.png"))
            elif self.ui_window.spinBox2.text() == "3":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/coconut.png"))
            elif self.ui_window.spinBox2.text() == "4":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/vanilla.png"))
            elif self.ui_window.spinBox2.text() == "5":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/bananas.png"))
            elif self.ui_window.spinBox2.text() == "0":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap(""))

        self.ui_window.spinBox2.valueChanged.connect(change)
        self.ui_window.spinBox1.valueChanged.connect(change)

    def openWindow3_6(self):
        global type_coffee
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/moccachino.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        if self.water_amount < 100 or self.coffee_amount < 20:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.syrup_type != '0' and self.syrup_amount[self.syrup_type] < 1:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif int(self.sugar_count) > self.sugar_amount:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.milk_amount < 200:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.hot_chocolate < 20:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        else:
            self.ui_window.btn_make.clicked.connect(self.openWindow4)
            self.ui_window.btn_back.clicked.connect(self.openWindow2)

        type_coffee = "moccachino"

        def change():
            self.sugar_count = self.ui_window.spinBox1.text()  # Используйте value() для получения числа
            self.syrup_type = self.ui_window.spinBox2.text()

            if self.ui_window.spinBox2.text() == "1":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/caramel.png"))
            elif self.ui_window.spinBox2.text() == "2":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/chocolate.png"))
            elif self.ui_window.spinBox2.text() == "3":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/coconut.png"))
            elif self.ui_window.spinBox2.text() == "4":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/vanilla.png"))
            elif self.ui_window.spinBox2.text() == "5":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/bananas.png"))
            elif self.ui_window.spinBox2.text() == "0":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap(""))

        self.ui_window.spinBox2.valueChanged.connect(change)
        self.ui_window.spinBox1.valueChanged.connect(change)

    def openWindow3_7(self):
        global type_coffee
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/raf.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        if self.water_amount < 50 or self.coffee_amount < 10:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.syrup_type != '0' and self.syrup_amount[self.syrup_type] < 1:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif int(self.sugar_count) > self.sugar_amount:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.milk_amount < 300:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        else:
            self.ui_window.btn_make.clicked.connect(self.openWindow4)
            self.ui_window.btn_back.clicked.connect(self.openWindow2)

        type_coffee = "raf"

        def change():
            self.sugar_count = self.ui_window.spinBox1.text()  # Используйте value() для получения числа
            self.syrup_type = self.ui_window.spinBox2.text()

            if self.ui_window.spinBox2.text() == "1":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/caramel.png"))
            elif self.ui_window.spinBox2.text() == "2":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/chocolate.png"))
            elif self.ui_window.spinBox2.text() == "3":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/coconut.png"))
            elif self.ui_window.spinBox2.text() == "4":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/vanilla.png"))
            elif self.ui_window.spinBox2.text() == "5":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/bananas.png"))
            elif self.ui_window.spinBox2.text() == "0":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap(""))

        self.ui_window.spinBox2.valueChanged.connect(change)
        self.ui_window.spinBox1.valueChanged.connect(change)

    def openWindow3_8(self):
        global type_coffee
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/cappuccino.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        if self.water_amount < 50 or self.coffee_amount < 10:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.syrup_type != '0' and self.syrup_amount[self.syrup_type] < 1:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif int(self.sugar_count) > self.sugar_amount:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.milk_amount < 150:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        else:
            self.ui_window.btn_make.clicked.connect(self.openWindow4)
            self.ui_window.btn_back.clicked.connect(self.openWindow2)

        type_coffee = "cappuccino"

        def change():
            self.sugar_count = self.ui_window.spinBox1.text()  # Используйте value() для получения числа
            self.syrup_type = self.ui_window.spinBox2.text()

            if self.ui_window.spinBox2.text() == "1":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/caramel.png"))
            elif self.ui_window.spinBox2.text() == "2":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/chocolate.png"))
            elif self.ui_window.spinBox2.text() == "3":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/coconut.png"))
            elif self.ui_window.spinBox2.text() == "4":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/vanilla.png"))
            elif self.ui_window.spinBox2.text() == "5":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/bananas.png"))
            elif self.ui_window.spinBox2.text() == "0":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap(""))

        self.ui_window.spinBox2.valueChanged.connect(change)
        self.ui_window.spinBox1.valueChanged.connect(change)

    def openWindow3_9(self):
        print("Данный вид кофе приготовить нельзя.")
        self.openWindow2()

    def openWindow3_10(self):
        global type_coffee
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/viennese_coffee.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        if self.water_amount < 200 or self.coffee_amount < 20:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.syrup_type != '0' and self.syrup_amount[self.syrup_type] < 1:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif int(self.sugar_count) > self.sugar_amount:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.milk_amount < 150:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        else:
            self.ui_window.btn_make.clicked.connect(self.openWindow4)
            self.ui_window.btn_back.clicked.connect(self.openWindow2)

        type_coffee = "viennese"

        def change():
            self.sugar_count = self.ui_window.spinBox1.text()  # Используйте value() для получения числа
            self.syrup_type = self.ui_window.spinBox2.text()

            if self.ui_window.spinBox2.text() == "1":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/caramel.png"))
            elif self.ui_window.spinBox2.text() == "2":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/chocolate.png"))
            elif self.ui_window.spinBox2.text() == "3":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/coconut.png"))
            elif self.ui_window.spinBox2.text() == "4":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/vanilla.png"))
            elif self.ui_window.spinBox2.text() == "5":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/bananas.png"))
            elif self.ui_window.spinBox2.text() == "0":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap(""))

        self.ui_window.spinBox2.valueChanged.connect(change)
        self.ui_window.spinBox1.valueChanged.connect(change)

    def openWindow3_11(self):
        global type_coffee
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/hot_chocolate.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        if self.syrup_type != '0' and self.syrup_amount[self.syrup_type] < 1:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif int(self.sugar_count) > self.sugar_amount:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.milk_amount < 150:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.hot_chocolate < 50:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        else:
            self.ui_window.btn_make.clicked.connect(self.openWindow4)
            self.ui_window.btn_back.clicked.connect(self.openWindow2)

        type_coffee = "hot_chocolate"

        def change():
            self.sugar_count = self.ui_window.spinBox1.text()  # Используйте value() для получения числа
            self.syrup_type = self.ui_window.spinBox2.text()

            if self.ui_window.spinBox2.text() == "1":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/caramel.png"))
            elif self.ui_window.spinBox2.text() == "2":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/chocolate.png"))
            elif self.ui_window.spinBox2.text() == "3":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/coconut.png"))
            elif self.ui_window.spinBox2.text() == "4":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/vanilla.png"))
            elif self.ui_window.spinBox2.text() == "5":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/bananas.png"))
            elif self.ui_window.spinBox2.text() == "0":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap(""))

        self.ui_window.spinBox2.valueChanged.connect(change)
        self.ui_window.spinBox1.valueChanged.connect(change)

    def openWindow3_12(self):
        global type_coffee
        self.new_window.close()
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog3()
        self.ui_window.Coffee_select = "icons/hot_chocolate.png"
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        if self.syrup_type != '0' and self.syrup_amount[self.syrup_type] < 1:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif int(self.sugar_count) > self.sugar_amount:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.milk_amount < 200:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        elif self.cocoa < 50:
            print("Недостаточно ингредиентов для приготовления кофе!")
            self.ui_window.btn_make.clicked.connect(self.openWindow2)
        else:
            self.ui_window.btn_make.clicked.connect(self.openWindow4)
            self.ui_window.btn_back.clicked.connect(self.openWindow2)

        type_coffee = "cocoa"

        def change():
            self.sugar_count = self.ui_window.spinBox1.text()  # Используйте value() для получения числа
            self.syrup_type = self.ui_window.spinBox2.text()

            if self.ui_window.spinBox2.text() == "1":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/caramel.png"))
            elif self.ui_window.spinBox2.text() == "2":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/chocolate.png"))
            elif self.ui_window.spinBox2.text() == "3":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/coconut.png"))
            elif self.ui_window.spinBox2.text() == "4":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/vanilla.png"))
            elif self.ui_window.spinBox2.text() == "5":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap("icons/bananas.png"))
            elif self.ui_window.spinBox2.text() == "0":
                self.ui_window.label_syrop.setPixmap(QtGui.QPixmap(""))

        self.ui_window.spinBox2.valueChanged.connect(change)
        self.ui_window.spinBox1.valueChanged.connect(change)

    def openWindow1(self):
        self.show()
        self.new_window.close()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Coffee()
    window.show()
    sys.exit(app.exec())

