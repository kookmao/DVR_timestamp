from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel, Qt, QRect
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog, QRubberBand
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QRect, QSize, QDate, QTime


import os
from logic.logic import extract_timestamp, export_frame_from_video


class MyGUI(QMainWindow):
    # initilize the selected region
    time_format = "hh:mm:ss ap"
    date_format = "MM-dd-yyyy"

    interval_ss = 1
    time_cap_ss = 50

    selected_rect = None
    imagesize = None
    file_paths = None
    selected_item = None
    box_selected = None
    i = 0

    def __init__(self):
        super(MyGUI, self).__init__()

        self.rubber_band = None
        self.start_pos = None

        uic.loadUi("gui/gui.ui", self)
        self.show()

        self.import_button.clicked.connect(self.import_clicked)
        self.undo_button.clicked.connect(self.undo_clicked)

        # create a QStringListModel
        self.list_model = QStringListModel()
        self.imported_files.setModel(self.list_model)

        # connect clicked signal to a function
        self.imported_files.clicked.connect(self.item_clicked)

        self.scan_button.clicked.connect(self.scan_date)
        self.scan_button.setEnabled(False)

        self.label.mousePressEvent = self.mouse_press_event
        self.label.mouseMoveEvent = self.mouse_move_event
        self.label.mouseReleaseEvent = self.mouse_release_event
        self.progress_bar.hide()

    def scan_date(self):
        print("scan button clicked")

        self.i = 0
        formatted_date = None
        skipped_seconds = 0
        self.progress_bar.setMaximum(self.time_cap_ss)
        self.progress_bar.show()

        while formatted_date is None and self.i < self.time_cap_ss:
            self.show_preview(self.selected_item)
            self.i += self.interval_ss
            skipped_seconds = +self.i
            formatted_date = extract_timestamp(
                ".\\exported_frame.jpg",
                self.box_selected,
                self.imagesize.width(),
                self.imagesize.height(),
            )
            

            # Update progress bar
            progress_value = min(
                self.i, self.time_cap_ss
            )  # Ensure progress value doesn't exceed the maximum
            self.progress_bar.setValue(progress_value)
            QApplication.processEvents()

        if formatted_date is not None:
            print("Found date!")
            self.system_date.setEnabled(True)
            self.system_time.setEnabled(True)
            self.actual_date.setEnabled(True)
            self.actual_time.setEnabled(True)
            self.apply_button.setEnabled(True)
            
            # TODO fix this with drop menu with 'MM-dd-yyyy' and 'dd-MM-yyyy' options
            date = QDate.fromString(formatted_date[0], self.date_format)
            time = QTime.fromString(formatted_date[1], self.time_format)
            
            if not date.isValid() and not time.isValid():
                QMessageBox.information(self, 'Information', 'couldnt extract time and date, please enter manually.')
                self.scan_button.setEnabled(False)
                return

            if date.isValid():
                self.system_date.setDate(date)
            else:
                #app = QApplication([])
                QMessageBox.information(self, 'Information', 'couldnt extract time, please enter manually.')
                print(f"date is not valid({formatted_date[0]})")
            if time.isValid():
                self.system_time.setTime(time)
            else:
               # app = QApplication([])
                QMessageBox.information(self, 'Information', 'couldnt extract time, please enter manually.')
                print(f"time is not valid! ({formatted_date[1]})")
            
           
        else:
            print("Couldn't find date!")
            QMessageBox.information(self, 'Information', "Couldn't extract, please enter manually")
            self.i = 0
            self.show_preview(self.selected_item)
            self.scan_button.setEnabled(True)

        # Reset progress bar after the task is complete
        self.progress_bar.hide()
        self.progress_bar.setValue(0)

    def import_clicked(self):
        print("import button pressed")
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        options |= QFileDialog.DontUseNativeDialog

        # selecting multiple files
        self.file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "QFileDialog.getOpenFileNames()",
            "",
            "All Files (*);;Text Files (*.txt)",
            options=options,
        )

        # file_paths is a list containing the selected file paths
        print("Selected files:")
        file_names = [os.path.basename(file_path) for file_path in self.file_paths]

        # Update the QStringListModel with the file names
        self.list_model.setStringList(self.file_paths)

    def item_clicked(self, index):
        self.selected_item = self.list_model.data(index, Qt.DisplayRole)
        self.show_preview(self.selected_item)

    def show_preview(self, selected_item):
        #print(f"Item clicked: {selected_item}")
        # selected item first frame, show it on screen
        if export_frame_from_video(selected_item, self.i):
            original_pixmap = QPixmap(".\\exported_frame.jpg")
            # Resize the image to the displayed size
            resized_pixmap = original_pixmap.scaled(
                self.label.size(), Qt.KeepAspectRatio
            )

            self.label.setPixmap(resized_pixmap)
            #self.scan_button.setEnabled(True)

            # Store the size of the displayed image
            self.imagesize = resized_pixmap.size()

    def mouse_press_event(self, event):
        ## if the image has been loaded
        if self.label.pixmap() is not None:
            if self.rubber_band is not None:
                self.rubber_band.hide()
            self.start_pos = event.pos()
            self.rubber_band = QRubberBand(QRubberBand.Rectangle, self.label)
            self.rubber_band.setGeometry(QRect(self.start_pos, QSize()))
            self.rubber_band.show()

    def mouse_move_event(self, event):
        if self.rubber_band is not None:
            self.rubber_band.setGeometry(
                QRect(self.start_pos, event.pos()).normalized()
            )

    def mouse_release_event(self, event):
        if self.rubber_band is not None:
            #  self.rubber_band.hide()
            self.box_selected = (
                self.rubber_band.geometry().left(),
                self.rubber_band.geometry().top(),
                self.rubber_band.geometry().right(),
                self.rubber_band.geometry().bottom(),
            )

            self.selected_rect = self.rubber_band.geometry()
            # Do something with the selected rectangle, e.g., crop the image
            print("Selected Rectangle:", self.selected_rect)
            self.scan_button.setEnabled(True)

    def undo_clicked(self, event):
        if self.selected_rect is not None:
            
            self.i = self.time_cap_ss
            self.rubber_band.hide()
            self.selected_rect = None
            self.scan_button.setEnabled(True)
            self.system_date.setDate(QDate.fromString("01-01-2000", self.date_format))
            self.system_time.setTime(QTime.fromString("00:00:00 AM", self.time_format))
