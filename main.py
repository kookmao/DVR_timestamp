# main.py
from PyQt5.QtWidgets import QApplication
from gui.gui import MyGUI
from logic.logic import *

if __name__ == "__main__":
    app = QApplication([])
    windows = MyGUI()
    app.exec_()