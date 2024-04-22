from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QSystemTrayIcon, \
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp
from PyQt5.QtCore import QSize
from ui import Ui_MainWindow
from registr import Ui_Form
from test import LoginWindow
from hotkey import Ui_Dialog
import keyboard
import sys
import logic
import time
print('111')
print('11111')
class Login(LoginWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_MessageBoxInformation))
        self.pushButton.clicked.connect(self.apply)

        self.pushButton_2.clicked.connect(self.login)
        self.radioButton.toggled.connect(self.radio_toggle)

        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        tr = logic.Translator()
        keyboard.add_hotkey("ctrl+c+t", tr.translate)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
            "Tray Program",
            "Application was minimized to Tray",
            QSystemTrayIcon.Information,
            2000
        )

    def radio_toggle(self):
        if not self.radioButton.isChecked():
            self.comboBox_2.setEnabled(True)
        else:
            self.comboBox_2.setEnabled(False)

    def autodetect(self):
        return self.radioButton.isChecked()

    def target_lang(self):
        return self.comboBox.currentIndex()

    def source_lang(self):
        return self.comboBox_2.currentIndex()

    def hotkey(self):
        return self.keySequenceEdit.keySequence()

    def apply(self):
        tr = logic.Translator(autodetect=self.autodetect(), target_lang=self.target_lang())
        keyboard.unhook_all_hotkeys()
        keyboard.add_hotkey("ctrl+c+" + self.lineEdit.text(), tr.translate)



    def login(self):
        self.lw = LoginWindow()
        self.lw.show()


app = QApplication(sys.argv)
mw = MainWindow()

mw.show()

sys.exit(app.exec())
