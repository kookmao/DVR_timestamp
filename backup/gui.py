# gui.py
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.uic import loadUi

class MyGUI(QMainWindow):
    def __init__(self, scan_function):
        super().__init__()
        self.scan_function = scan_function
        self.initUI()

    def initUI(self):
        # Load your custom .ui file as the main window
        loadUi("gui/.ui", self)  # Make sure to use the correct path to custom_ui.ui

        # Find and connect the "Scan" button from your custom UI
        scan_button = self.findChild(QPushButton, "scanButton")  # Replace "scanButton" with the actual name of your button
        if scan_button is not None:
            scan_button.clicked.connect(self.scan_button_clicked)

    def scan_button_clicked(self):
        result = self.scan_function()  # Call the provided scan function
        print(result)
