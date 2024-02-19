from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout

from mySQL import MySQL

class SignIN(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("NICK NAME...")
        self.age_edit = QLineEdit()
        self.age_edit.setPlaceholderText("AGE...")
        self.parol_edit = QLineEdit()
        self.parol_edit.setPlaceholderText("PASSWORD...")
        self.parol_edit.setEchoMode(QLineEdit.Password)

        self.lbl = QLabel("")

        self.submit_btn = QPushButton("SUBMIT")
        self.submit_btn.clicked.connect(self.SUBMIT)

        self.v_main_lay.addWidget(self.name_edit)
        self.v_main_lay.addWidget(self.age_edit)
        self.v_main_lay.addWidget(self.parol_edit)
        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addWidget(self.submit_btn)

        self.setLayout(self.v_main_lay)
    
    def SUBMIT(self):
        if self.name_edit.text() and self.age_edit.text() and self.parol_edit.text():
            try:
                self.db = MySQL()
                self.db.SignInUserQuery(self.name_edit.text(), int(self.age_edit.text()), self.parol_edit.text())
                self.lbl.setText("User was created succesfully")
                self.lbl.setStyleSheet("color:Green")
            except ValueError:
                self.lbl.setText("Please enter your age in a correct numeric format.")
                self.lbl.setStyleSheet("color:Red")   
            except:
                self.lbl.setText("User is already exists")
                self.lbl.setStyleSheet("color:Red")

            self.lbl.adjustSize()