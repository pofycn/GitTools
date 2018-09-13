# -*- coding: utf-8 -*-

__author__ = 'Jerry Chan'

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont

# def main():
#     app = QApplication(sys.argv)
#     w = QWidget()
#     w.resize(600, 400)
#     # w.move(300, 300)
#     w.setWindowTitle('CMFT-GitTools')
#     w.show()
#     sys.exit(app.exec_())


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(20, 20)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
