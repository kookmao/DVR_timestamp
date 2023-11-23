# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\noahs\DVR_timestamp\gui\gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1088, 655)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\noahs\\DVR_timestamp\\gui\\icon-icx-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.imported_files = QtWidgets.QListView(self.centralwidget)
        self.imported_files.setEnabled(True)
        self.imported_files.setGeometry(QtCore.QRect(15, 15, 205, 571))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imported_files.sizePolicy().hasHeightForWidth())
        self.imported_files.setSizePolicy(sizePolicy)
        self.imported_files.setMinimumSize(QtCore.QSize(100, 205))
        self.imported_files.setMaximumSize(QtCore.QSize(1600, 1600))
        self.imported_files.setAcceptDrops(True)
        self.imported_files.setFrameShape(QtWidgets.QFrame.Box)
        self.imported_files.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.imported_files.setDragEnabled(True)
        self.imported_files.setObjectName("imported_files")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setEnabled(False)
        self.start_button.setGeometry(QtCore.QRect(120, 600, 100, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        self.start_button.setMinimumSize(QtCore.QSize(100, 30))
        self.start_button.setMaximumSize(QtCore.QSize(100, 30))
        self.start_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_button.setObjectName("start_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(226, 15, 854, 480))
        self.label.setMinimumSize(QtCore.QSize(640, 360))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label.setAutoFillBackground(True)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("c:\\Users\\noahs\\DVR_timestamp\\gui\\default.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.undo_button = QtWidgets.QPushButton(self.centralwidget)
        self.undo_button.setGeometry(QtCore.QRect(840, 540, 50, 22))
        self.undo_button.setDefault(False)
        self.undo_button.setFlat(False)
        self.undo_button.setObjectName("undo_button")
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setEnabled(True)
        self.progress_bar.setGeometry(QtCore.QRect(225, 495, 854, 4))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress_bar.sizePolicy().hasHeightForWidth())
        self.progress_bar.setSizePolicy(sizePolicy)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setOrientation(QtCore.Qt.Horizontal)
        self.progress_bar.setInvertedAppearance(False)
        self.progress_bar.setObjectName("progress_bar")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(480, 510, 286, 91))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.scan_button = QtWidgets.QPushButton(self.widget)
        self.scan_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scan_button.sizePolicy().hasHeightForWidth())
        self.scan_button.setSizePolicy(sizePolicy)
        self.scan_button.setMinimumSize(QtCore.QSize(50, 22))
        self.scan_button.setMaximumSize(QtCore.QSize(50, 22))
        self.scan_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scan_button.setAutoDefault(True)
        self.scan_button.setDefault(False)
        self.scan_button.setObjectName("scan_button")
        self.gridLayout.addWidget(self.scan_button, 0, 0, 1, 1)
        self.system_date = QtWidgets.QDateEdit(self.widget)
        self.system_date.setEnabled(True)
        self.system_date.setMaximumSize(QtCore.QSize(80, 20))
        self.system_date.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.system_date.setCalendarPopup(True)
        self.system_date.setObjectName("system_date")
        self.gridLayout.addWidget(self.system_date, 0, 1, 1, 1)
        self.system_time = QtWidgets.QTimeEdit(self.widget)
        self.system_time.setEnabled(True)
        self.system_time.setMaximumSize(QtCore.QSize(80, 20))
        self.system_time.setObjectName("system_time")
        self.gridLayout.addWidget(self.system_time, 0, 2, 1, 1)
        self.actual_date = QtWidgets.QDateEdit(self.widget)
        self.actual_date.setEnabled(False)
        self.actual_date.setMaximumSize(QtCore.QSize(80, 20))
        self.actual_date.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.actual_date.setCalendarPopup(True)
        self.actual_date.setObjectName("actual_date")
        self.gridLayout.addWidget(self.actual_date, 1, 1, 1, 1)
        self.actual_time = QtWidgets.QTimeEdit(self.widget)
        self.actual_time.setEnabled(False)
        self.actual_time.setMaximumSize(QtCore.QSize(80, 20))
        self.actual_time.setObjectName("actual_time")
        self.gridLayout.addWidget(self.actual_time, 1, 2, 1, 1)
        self.apply_button = QtWidgets.QPushButton(self.widget)
        self.apply_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apply_button.sizePolicy().hasHeightForWidth())
        self.apply_button.setSizePolicy(sizePolicy)
        self.apply_button.setMinimumSize(QtCore.QSize(50, 22))
        self.apply_button.setMaximumSize(QtCore.QSize(50, 22))
        self.apply_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.apply_button.setObjectName("apply_button")
        self.gridLayout.addWidget(self.apply_button, 1, 0, 1, 1)
        self.import_button = QtWidgets.QPushButton(self.centralwidget)
        self.import_button.setGeometry(QtCore.QRect(15, 600, 100, 30))
        self.import_button.setMinimumSize(QtCore.QSize(100, 30))
        self.import_button.setMaximumSize(QtCore.QSize(100, 30))
        self.import_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.import_button.setDefault(True)
        self.import_button.setObjectName("import_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DVR timestamp"))
        self.start_button.setStatusTip(_translate("MainWindow", "start processing"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.undo_button.setText(_translate("MainWindow", "Reset"))
        self.scan_button.setStatusTip(_translate("MainWindow", "scan date & time"))
        self.scan_button.setText(_translate("MainWindow", "Scan"))
        self.system_date.setStatusTip(_translate("MainWindow", "system date"))
        self.system_date.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.system_time.setStatusTip(_translate("MainWindow", "system time"))
        self.system_time.setDisplayFormat(_translate("MainWindow", "hh:mm:ss"))
        self.actual_date.setStatusTip(_translate("MainWindow", "actual date"))
        self.actual_date.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.actual_time.setStatusTip(_translate("MainWindow", "actual time"))
        self.actual_time.setDisplayFormat(_translate("MainWindow", "hh:mm:ss"))
        self.apply_button.setStatusTip(_translate("MainWindow", "apply actual time"))
        self.apply_button.setText(_translate("MainWindow", "Apply"))
        self.import_button.setStatusTip(_translate("MainWindow", "import videos"))
        self.import_button.setText(_translate("MainWindow", "Import"))
