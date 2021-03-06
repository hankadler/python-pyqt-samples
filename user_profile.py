#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""A user profile GUI.

@author   Hank Adler
@version  0.1.0
@license  MIT
"""


import os
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QFont


class UserProfileWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(300, 375)
        self.setWindowTitle('User Profile')
        self.setStyleSheet('background-color: white;')
        self.displayImages()
        self.displayInfo()

        self.show()

    def displayImages(self):
        # Background
        try:
            with open(abspath('resources/marble.webp')) as img:
                bg_label = QLabel(self)
                bg_label.setPixmap(QPixmap(img.name))
        except FileNotFoundError:
            print(f'ERROR: $bg_label image not found!')
        bg_label.setGeometry(0, 0, 300, 150)

        # Foreground
        try:
            with open(abspath('resources/logo_v0.1.1.png')) as img:
                fg_label = QLabel(self)
                fg_label.setPixmap(QPixmap(img.name))
        except FileNotFoundError:
            print(f'ERROR: $fg_label image not found!')
        fg_label.setGeometry(100, 25, 100, 100)

    def displayInfo(self):
        h1_font = QFont('Roboto', 12)
        h1_font.setBold(True)
        b1_font = QFont('Roboto Mono', 10)

        # User
        usr_h1_label = QLabel(self)
        usr_h1_label.setFont(h1_font)
        usr_h1_label.setText('Hank Adler')
        usr_h1_label.move(100, 165)

        # Biography
        bio_h1_label = QLabel(self)
        bio_h1_label.setText('Biography')
        bio_h1_label.setFont(h1_font)
        bio_h1_label.move(10, 200)

        bio_b1_label = QLabel(self)
        bio_b1_label.setFont(b1_font)
        bio_b1_label.setText("A man's reach should extend beyond\nhis grasp!")
        bio_b1_label.move(20, 220)

        # Skills
        skills_h1_label = QLabel(self)
        skills_h1_label.setText('Skills')
        skills_h1_label.setFont(h1_font)
        skills_h1_label.move(10, 280)

        skills_b1_label = QLabel(self)
        skills_b1_label.setFont(b1_font)
        skills_b1_label.setText(
            "Boxing | Coding | Engineering\n"
            "Design | Investing | Music\n"
            "Philosophy | Writing | Lifting"
        )
        skills_b1_label.move(20, 300)


def abspath(path):
    """Converts resources path from relative to absolute."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, path)
    return os.path.join(os.path.abspath('.'), path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = UserProfileWindow()
    sys.exit(app.exec_())
