from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout

from mySQL import MySQL
from Search import SearchWindow
from adminPanelWindow import AdminPanel

class SignUP(QWidget):
    def __init__(self, data):
        super().__init__()

        self.data = data

        self.check_btn_lampochka = True

        self.h1_lay = QHBoxLayout()
        self.h2_lay = QHBoxLayout()
        self.v_main_lay = QVBoxLayout()

        self.name_edit = QLineEdit()
        self.parol_edit = QLineEdit()
        self.parol_edit.setEchoMode(QLineEdit.Password)

        self.name_lbl = QLabel("Login:  ")
        self.parol_lbl = QLabel("Parol: ")
        self.natija_lbl = QLabel("")

        self.submit_btn = QPushButton("OK")
        self.submit_btn.clicked.connect(self.OK)

        self.check_btn = QPushButton("CHECK")
        self.check_btn.clicked.connect(self.CHECK)

        self.h1_lay.addWidget(self.name_lbl)
        self.h1_lay.addWidget(self.name_edit)

        self.h2_lay.addWidget(self.parol_lbl)
        self.h2_lay.addWidget(self.parol_edit)
        self.h2_lay.addWidget(self.check_btn)

        self.v_main_lay.addLayout(self.h1_lay)
        self.v_main_lay.addLayout(self.h2_lay)
        self.v_main_lay.addWidget(self.natija_lbl)
        self.v_main_lay.addWidget(self.submit_btn)

        self.setLayout(self.v_main_lay)
    
    def OK(self):
        db = MySQL()
        if self.data == "user":
            natija = db.CheckUserQuery(self.name_edit.text())
            if natija is not None:
                if natija[0] == self.parol_edit.text():
                    self.new_window = SearchWindow()

                    self.new_window.genre_cm.addItems([i[0] for i in db.allGenreQuery()])
                    self.new_window.author_cm.addItems([i[0] for i in db.allAuthorQuery()])

                    self.hide()
                    self.new_window.show()
                else:
                    self.natija_lbl.setText("Parolingiz hato")
            else:
                self.natija_lbl.setText("SIZ RO'YXATDAN O'TMAGANSIZ")
        elif self.data == "admin":
            natija = db.CheckAdminQuery(self.name_edit.text())
            if natija is not None:
                if natija[0] == self.parol_edit.text():
                    self.new_window = AdminPanel()
                    self.hide()
                    self.new_window.show()
                else:
                    self.natija_lbl.setText("Parolingiz hato")
            else:
                exit()
        self.natija_lbl.adjustSize()

    def CHECK(self):
        if self.check_btn_lampochka:
            self.parol_edit.setEchoMode(QLineEdit.Normal)
            self.check_btn_lampochka = False
        else:
            self.check_btn_lampochka = True
            self.parol_edit.setEchoMode(QLineEdit.Password)
