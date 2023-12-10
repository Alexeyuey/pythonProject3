import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush


class Square1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(50, 50, 800, 900)
        self.setWindowTitle('Square-Lens — 1')

        self.label1 = QLabel('Size of the side of the square (pixels):')
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setText('300')

        self.label2 = QLabel('Scaling factor (<1):')
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setText('0.9')

        self.label3 = QLabel('Number of squares:')
        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setText('10')

        self.btn = QPushButton('Draw Squares', self)
        self.btn.clicked.connect(self.drawSquares)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.label2)
        layout.addWidget(self.lineEdit_2)
        layout.addWidget(self.label3)
        layout.addWidget(self.lineEdit_3)
        layout.addWidget(self.btn)

        self.view = QGraphicsView(self)
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)
        layout.addWidget(self.view)

        self.setLayout(layout)
        self.show()

    def drawSquares(self):
        a = int(self.lineEdit.text())
        k = float(self.lineEdit_2.text())
        n = int(self.lineEdit_3.text())

        self.scene.clear()

        pen = QPen(Qt.black)
        brush = QBrush(self.color)

        side_length = a
        x, y = 400 - side_length / 2, 400 - side_length / 2

        for _ in range(n):
            rect = QRectF(x, y, side_length, side_length)
            self.scene.addRect(rect, pen, brush)
            side_length *= k
            x, y = x + (a - side_length) / 2, y + (a - side_length) / 2

    @property
    def color(self):
        return QColor(255, 0, 0)  # You can change the color here


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Square1()
    sys.exit(app.exec_())
