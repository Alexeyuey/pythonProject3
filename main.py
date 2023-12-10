import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PyQt5.QtCore import Qt, QObject, pyqtSignal


class DotGame(QMainWindow):
    dotClicked = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Dots Game')

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        self.board_size = 8  # You can change the size of the board here
        self.cell_size = 25

        self.initBoard()

    def initBoard(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                x = col * self.cell_size
                y = row * self.cell_size
                dot = DotItem(x, y, self.cell_size, self.dotClicked)
                self.scene.addItem(dot)


class DotItem(QGraphicsEllipseItem):
    def __init__(self, x, y, size, signal_handler):
        super().__init__(x, y, size, size)

        self.setBrush(Qt.white)
        self.setPen(Qt.black)

        self.row = y // size
        self.col = x // size

        self.signal_handler = signal_handler

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setBrush(Qt.blue)  # Change the color to the current player's color
            self.signal_handler.emit(self.row, self.col)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DotGame()
    window.show()
    sys.exit(app.exec_())
