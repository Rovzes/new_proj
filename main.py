import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QDialog, QApplication


class Example(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)

        self.do_paint = False

        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ell(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_ell(self, qp):
        x = random.randint(0, self.size().width())
        y = random.randint(0, self.size().height())
        s = random.randint(0, self.size().height() // 2)

        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, s, s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
