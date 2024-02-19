from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QPushButton, QHBoxLayout, QVBoxLayout

from SignIn import SignIN
from SignUp import SignUP

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.h_radio_lay = QHBoxLayout()
        self.v_main_lay = QVBoxLayout()

        self.admin_radio_btn = QRadioButton("ADMIN")
        self.user_radio_btn = QRadioButton("USER")

        self.singIn_btn = QPushButton("SIGN IN")
        self.singIn_btn.clicked.connect(self.SIGNIN)
        self.singUp_btn = QPushButton("SIGN UP")
        self.singUp_btn.clicked.connect(self.SIGNUP)

        self.h_radio_lay.addWidget(self.admin_radio_btn)
        self.h_radio_lay.addWidget(self.user_radio_btn)

        self.v_main_lay.addLayout(self.h_radio_lay)
        self.v_main_lay.addWidget(self.singIn_btn)
        self.v_main_lay.addWidget(self.singUp_btn)

        self.setLayout(self.v_main_lay)

    def SIGNIN(self):
        if self.user_radio_btn.isChecked():
            self.oynacha = SignIN()
            self.oynacha.show()

    def SIGNUP(self):
        if self.user_radio_btn.isChecked():
            self.user_window = SignUP("user")
            self.user_window.show()
        elif self.admin_radio_btn.isChecked():
            self.user_window = SignUP("admin")
            self.user_window.show()

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()