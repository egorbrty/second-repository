import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from random import randint

import traceback


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Oбнаружена ошибка !:", tb)
#    QtWidgets.QApplication.quit()             # !!! если вы хотите, чтобы событие завершилось


sys.excepthook = excepthook


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.paint)

        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setPen(QPen(QColor(255, 255, 0)))
        x = randint(10, 200)
        qp.drawEllipse(150, 100, x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())