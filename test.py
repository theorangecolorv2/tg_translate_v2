from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QSystemTrayIcon, \
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp
from PyQt5.QtCore import QSize
import sys
from registr import Ui_Form
from reg_ok import RegOk_Dialog
from reg_err import RegErr_Dialog
from auth_ok import AuthOk_Dialog
from auth_err import AuthErr_Dialog
import sqlite3


class RegErr(QMainWindow, RegErr_Dialog):
    def __init__(self):
        super(RegErr, self).__init__()
        self.setupUi(self)


class RegOk(QMainWindow, RegOk_Dialog):
    def __init__(self):
        super(RegOk, self).__init__()
        self.setupUi(self)


class AuthErr(QMainWindow, AuthErr_Dialog):
    def __init__(self):
        super(AuthErr, self).__init__()
        self.setupUi(self)


class AuthOk(QMainWindow, AuthOk_Dialog):
    def __init__(self):
        super(AuthOk, self).__init__()
        self.setupUi(self)


class LoginWindow(QMainWindow, Ui_Form):

    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.lineEdit.setPlaceholderText("Эл. почта")
        self.pushButton_2.clicked.connect(self.auth)
        self.pushButton.clicked.connect(self.reg)



    def auth_err(self):
        self.auth_err_w = AuthErr()
        self.auth_err_w.show()

    def auth_ok(self):
        self.auth_ok_w = AuthOk()
        self.auth_ok_w.show()

    def reg_err(self):
        self.reg_err_w = RegErr()
        self.reg_err_w.show()

    def reg_ok(self):
        self.reg_ok_w= RegOk()
        self.reg_ok_w.show()

    def auth(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        con = sqlite3.connect("films_db.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM Films
                WHERE  username = ? AND password = ?""", (username, password)).fetchall()
        print(result)
        if result:
            self.auth_ok()
        else:
            self.auth_err()

    def reg(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        con = sqlite3.connect("films_db.sqlite")
        cur = con.cursor()

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        result = cur.execute("""SELECT * FROM Films
                        WHERE  username = ? AND password = ?""", (username, password)).fetchall()

        print(result)

        if not result:
            print("regok")
            cur.execute("""INSERT INTO Films(username, password) VALUES (?,?)""", (username, password))
            con.commit()
            self.reg_ok()
        else:
            print("regerr")
            self.reg_err()


# app = QApplication(sys.argv)
# mw = LoginWindow()
#
# mw.show()
#
# sys.exit(app.exec())
