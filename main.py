import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui')
        self.do_paint = False
        self.btn_run.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        qp.setPen(QColor(255, 0, 0))
        qp.drawRect(0, 0, 120, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Circles()
    wnd.show()
    sys.exit(app.exec())