import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QWidget, QLabel, QLCDNumber


class MiniCalculate(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle("Миникалькулятор")

        self.inpFirst = QLineEdit(self)
        self.inpFirst.setGeometry(20, 25, 70, 15)

        self.inpSecond = QLineEdit(self)
        self.inpSecond.setGeometry(20, 90, 70, 15)

        self.onInpFirst = QLabel(self)
        self.onInpFirst.move(20, 10)
        self.onInpFirst.setText("Первое число (целое):")

        self.onInpSecond = QLabel(self)
        self.onInpSecond.move(20, 75)
        self.onInpSecond.setText("Второе число(целое):")

        self.btn = QPushButton("->", self)
        self.btn.setGeometry(100, 45, 65, 25)
        self.btn.clicked.connect(self.result)

        self.sumDisp = QLCDNumber(self)
        self.sumDisp.setGeometry(300, 10, 70, 25)

        self.differenceDisp = QLCDNumber(self)
        self.differenceDisp.setGeometry(300, 35, 70, 25)

        self.multiplicationDisp = QLCDNumber(self)
        self.multiplicationDisp.setGeometry(300, 60, 70, 25)

        self.divisionDisp = QLCDNumber(self)
        self.divisionDisp.setGeometry(300, 85, 70, 25)

        self.labelSumDisp = QLabel(self)
        self.labelSumDisp.move(250, 20)
        self.labelSumDisp.setText("Сумма:")

        self.labelDifferenceDisp = QLabel(self)
        self.labelDifferenceDisp.move(235, 45)
        self.labelDifferenceDisp.setText("Разность:")

        self.labelMultiplicationDisp = QLabel(self)
        self.labelMultiplicationDisp.move(223, 70)
        self.labelMultiplicationDisp.setText("Произведение:")

        self.labelDivisionDisp = QLabel(self)
        self.labelDivisionDisp.move(240, 95)
        self.labelDivisionDisp.setText("Частное:")

    def result(self):
        self.sumDisp.display(int(self.inpFirst.text()) + int(self.inpSecond.text()))
        self.differenceDisp.display(int(self.inpFirst.text()) - int(self.inpSecond.text()))
        self.multiplicationDisp.display(int(self.inpFirst.text()) * int(self.inpSecond.text()))

        if self.inpSecond.text() == "0":
            self.divisionDisp.display("Error")

        else:
            self.divisionDisp.display(round(int(self.inpFirst.text()) / int(self.inpSecond.text()), 3))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MiniCalculate()
    ex.show()
    sys.exit(app.exec())