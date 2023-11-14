from PyQt5 import uic,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel
from PyQt5.QtCore import Qt
import os
from logic.logic import *

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("gui/gui.ui", self)
        self.show()

        self.import_button.clicked.connect(self.import_clicked)

        # Create a QStringListModel
        self.list_model = QStringListModel()
        self.imported_files.setModel(self.list_model)

        # Connect the item clicked signal to a function
        self.imported_files.clicked.connect(self.item_clicked)

    def import_clicked(self):
        print("import button pressed")
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        options |= QFileDialog.DontUseNativeDialog

        # Allow selecting multiple files
        file_paths, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "", "All Files (*);;Text Files (*.txt)", options=options)

        # file_paths is a list containing the selected file paths
        print("Selected files:")
        file_names = [os.path.basename(file_path) for file_path in file_paths]

        # Update the QStringListModel with the file names
        self.list_model.setStringList(file_paths)

    def item_clicked(self, index):
        # Get the selected item text
        selected_item = self.list_model.data(index, Qt.DisplayRole)

        # Call your function with the selected item
        self.show_preview(selected_item)

    def show_preview(self, selected_item):
        # Replace this with your actual function logic
        print(f"Item clicked: {selected_item}")
        scan_video_for_timestamp(selected_item)
        self.label.setPixmap(QtGui.QPixmap(".\\exported_frame.jpg"))
        
