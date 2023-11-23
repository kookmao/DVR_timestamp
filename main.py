# main.py
from PyQt5.QtWidgets import QApplication
from gui.gui import MyGUI
from logic.logic import *
from pathlib import Path

if __name__ == "__main__":
    app = QApplication([])
    windows = MyGUI()
    app.setStyleSheet(Path('style.qss').read_text())
    app.exec_()