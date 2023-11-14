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
        loadUi("gui/gui.ui", self)  # Make sure to use the correct path to custom_ui.ui

        # Find and connect the "Scan" button from your custom UI
        scan_button = self.findChild(
            QPushButton, "scan_button"
        )  # Replace "scanButton" with the actual name of your button
        if scan_button is not None:
            scan_button.clicked.connect(self.scan_button_clicked)

        # Find and connect the "Scan" button from your custom UI
        import_button = self.findChild(
            QPushButton, "import_button"
        )  # Replace "scanButton" with the actual name of your button
        if import_button is not None:
            import_button.clicked.connect(self.import_button_clicked)

    def scan_button_clicked(self):
        result = self.scan_function()  # Call the provided scan function
        print(result)

    def import_button_clicked(self):
        result = self.import_function()  # Call the provided scan function
        print(result)
