# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5 import QtGui


class Button(QWidget):
    def __init__(self, text, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.button = QPushButton(text)
        self.button.setStyleSheet(open('mystylesheet.css').read())

        layout.addWidget(self.button)
        self.setLayout(layout)


class Label(QWidget):
    def __init__(self, text, *args, **kwargs):
        super(Label, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.label = QLabel(text)
        self.label.setStyleSheet(open('mystylesheet.css').read())

        layout.addWidget(self.label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])
    QtGui.QFontDatabase.addApplicationFont(
        "./resources/fonts/PoppinsRegular.ttf")
    app.setStyleSheet(open('mystylesheet.css').read())
    window = QWidget()
    layout = QVBoxLayout()
    button = Button("This is a button")
    layout.addWidget(button)
    layout.addWidget(Label("This si a llwbel"))
    window.setLayout(layout)
    window.show()
    app.exec()
