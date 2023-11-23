from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel, Qt, QRect
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog, QRubberBand
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QRect, QSize


import os
from logic.logic import extract_timestamp, export_frame_from_video

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        
        self.rubber_band = None  # Variable to hold the rubber band instance
        self.start_pos = None  # Variable to hold the starting position of the rubber band

        uic.loadUi("gui/gui.ui", self)
        self.show()

        self.import_button.clicked.connect(self.import_clicked)

        # Create a QStringListModel
        self.list_model = QStringListModel()
        self.imported_files.setModel(self.list_model)

        # Connect the item clicked signal to a function
        self.imported_files.clicked.connect(self.item_clicked)

        self.scan_button.clicked.connect(self.scan_date)

        self.label.mousePressEvent = self.mouse_press_event
        self.label.mouseMoveEvent = self.mouse_move_event
        self.label.mouseReleaseEvent = self.mouse_release_event

    def scan_date(self):
        print("scan button clicked")
        # Use the selected region for further processing
        if self.current_rect.isValid():
            selected_region = self.label.pixmap().copy(self.current_rect)
            # You can perform further processing with the selected region here
            # ...
            print("Processing selected region.")
            self.scan_button.setEnabled(False)

    def import_clicked(self):
        print("import button pressed")
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        options |= QFileDialog.DontUseNativeDialog

        # Allow selecting multiple files
        file_paths, _ = QFileDialog.getOpenFileNames(
            self, "QFileDialog.getOpenFileNames()", "", "All Files (*);;Text Files (*.txt)", options=options
        )

        # file_paths is a list containing the selected file paths
        print("Selected files:")
        file_names = [os.path.basename(file_path) for file_path in file_paths]

        # Update the QStringListModel with the file names
        self.list_model.setStringList(file_paths)

    def item_clicked(self, index):
        selected_item = self.list_model.data(index, Qt.DisplayRole)
        self.show_preview(selected_item)

    def show_preview(self, selected_item):
        print(f"Item clicked: {selected_item}")
        if export_frame_from_video(selected_item, 0):
            pixmap = QPixmap(".\\exported_frame.jpg")
            self.label.setPixmap(pixmap)
            self.scan_button.setEnabled(True)

    def mouse_press_event(self, event):
        if self.label.pixmap() is not None:
            self.start_pos = event.pos()
            self.rubber_band = QRubberBand(QRubberBand.Rectangle, self.label)
            self.rubber_band.setGeometry(QRect(self.start_pos, QSize()))
            self.rubber_band.show()

    def mouse_move_event(self, event):
        if self.rubber_band is not None:
            self.rubber_band.setGeometry(QRect(self.start_pos, event.pos()).normalized())

    def mouse_release_event(self, event):
        if self.rubber_band is not None:
            self.rubber_band.hide()
            selected_rect = self.rubber_band.geometry()
            # Do something with the selected rectangle, e.g., crop the image
            print("Selected Rectangle:", selected_rect)
   