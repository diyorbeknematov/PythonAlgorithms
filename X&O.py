from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QStyle, QWidget, QPushButton, QLabel, QCheckBox
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QMessageBox

class MyWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("X&O")
        self.initUI()
        self.applyStyles()

    def initUI(self):
        self.grid_lay = QGridLayout()
        self.h_btn_lay = QHBoxLayout()
        self.v_main_lay = QVBoxLayout()
        self.h_rbtn_lay = QHBoxLayout()

        self.lbl = QLabel("X & O O'yini")
        self.lbl.setAlignment(Qt.AlignCenter)

        self.chkX = QCheckBox("X", clicked=lambda: self.checkExclusive(self.chkX))
        self.chkO = QCheckBox("O", clicked=lambda: self.checkExclusive(self.chkO))

        self.btn1 = QPushButton(clicked = lambda : self.processPlayerMove(self.btn1))
        self.btn2 = QPushButton(clicked = lambda : self.processPlayerMove(self.btn2))
        self.btn3 = QPushButton(clicked = lambda : self.processPlayerMove(self.btn3))
        self.btn4 = QPushButton(clicked = lambda : self.processPlayerMove(self.btn4))
        self.btn5 = QPushButton(clicked = lambda : self.processPlayerMove(self.btn5))
        self.btn6 = QPushButton(clicked = lambda : self.processPlayerMove(self.btn6))
        self.btn7 = QPushButton(clicked = lambda : self.processPlayerMove(self.btn7))
        self.btn8 = QPushButton(clicked = lambda : self.processPlayerMove(self.btn8))
        self.btn9 = QPushButton(clicked = lambda : self.processPlayerMove(self.btn9))

        self.start = QPushButton("START", clicked=self.START)
        self.restart = QPushButton("RESTART", clicked=self.RESTART)
        self.restart.hide()
        self.exit = QPushButton("EXIT", clicked=exit)

        self.buttons = [self.btn1, self.btn2, self.btn3,
                        self.btn4, self.btn5, self.btn6,
                        self.btn7, self.btn8, self.btn9]

        index = 0
        for i in range(3):
            for j in range(3):
                self.grid_lay.addWidget(self.buttons[index], i, j)
                self.buttons[index].hide()
                self.buttons[index].setMinimumSize(50, 50)
                index += 1
        self.grid_lay.setSpacing(0)  # Buttonlar orasidagi bo'shliqni yo'q qilish


        self.h_btn_lay.addWidget(self.start)
        self.h_btn_lay.addWidget(self.restart)
        self.h_btn_lay.addWidget(self.exit)

        self.h_rbtn_lay.addWidget(self.chkX)
        self.h_rbtn_lay.addWidget(self.chkO)

        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addStretch()
        self.v_main_lay.addLayout(self.h_rbtn_lay)
        self.v_main_lay.addStretch()
        self.v_main_lay.addLayout(self.grid_lay)
        self.v_main_lay.addStretch()
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)


    def checkExclusive(self, checkBox):
        if self.chkO == checkBox:
            self.chkX.setChecked(False)
        if self.chkX == checkBox:
            self.chkO.setChecked(False)


    def START(self):
        if self.chkO.isChecked() or self.chkX.isChecked():
            self.setFixedSize(250, 250)
            self.restart.show()
            self.chkO.hide()
            self.chkX.hide()
            self.start.hide()
            self.lbl.show()

            self.navbat = False if self.chkX.isChecked() else True
            if self.navbat:
                self.lbl.setText("Navbat: 🟢")
            else:
                self.lbl.setText("Navbat: ❌")
            for i in self.buttons:
                i.show()


    def processPlayerMove(self, btn):
        if self.navbat:
            btn.setText("🟢")
            btn.setEnabled(False)

            self.lbl.setText("Navbat: ❌")

            self.navbat = False
        else:
            btn.setText("❌")
            btn.setEnabled(False)

            self.lbl.setText("Navbat: 🟢")

            self.navbat = True
        
        if self.checkWinner():
            return 
        
        if self.checkForDraw():
            return 


    def RESTART(self):
        #Qayta boshlash
        self.setFixedSize(200, 150)
        self.lbl.setText("X & O o'yini")
        self.start.show()
        self.restart.hide()

        self.chkO.setChecked(False)
        self.chkX.setChecked(False)
        self.chkX.show()
        self.chkO.show()

        for i in self.buttons:
            i.setText("")
            i.setEnabled(True)
            i.setStyleSheet("background-color: #ADD8E6;")
            i.hide()


    def checkWinner(self):
        if self.btn1.text() == self.btn2.text() == self.btn3.text() and self.btn1.text() != "":
            self.win(self.btn1, self.btn2, self.btn3)
        elif self.btn4.text() == self.btn5.text() == self.btn6.text() and self.btn4.text() != "":
            self.win(self.btn4, self.btn5, self.btn6)
        elif self.btn7.text() == self.btn8.text() == self.btn9.text() and self.btn7.text() != "":
            self.win(self.btn7, self.btn8, self.btn9)
        elif self.btn1.text() == self.btn4.text() == self.btn7.text() and self.btn1.text() != "":
            self.win(self.btn1, self.btn4, self.btn7)
        elif self.btn2.text() == self.btn5.text() == self.btn8.text() and self.btn2.text() != "":
            self.win(self.btn2, self.btn5, self.btn8)
        elif self.btn3.text() == self.btn6.text() == self.btn9.text() and self.btn3.text() != "":
            self.win(self.btn3, self.btn6, self.btn9)
        elif self.btn1.text() == self.btn5.text() == self.btn9.text() and self.btn1.text() != "":
            self.win(self.btn1, self.btn5, self.btn9)
        elif self.btn3.text() == self.btn5.text() == self.btn7.text() and self.btn3.text() != "":
            self.win(self.btn3, self.btn5, self.btn7)
        else:
            return False
        return True

    
    def win(self, btn1, btn2, btn3):
        btn1.setStyleSheet("Background-color: green")
        btn2.setStyleSheet("Background-color: green")
        btn3.setStyleSheet("Background-color: green")

        for i in self.buttons:
            i.setEnabled(False)

        winner = btn1.text()
        msg = QMessageBox()
        msg.setWindowTitle("O'yin Yakuni")
        msg.setText(f"Tabriklaymiz! '{winner}' yutdi!")
        msg.setInformativeText("Yana o'ynash uchun 'RESTART' tugmasini bosing.")
        msg.setStyleSheet("""
                    QMessageBox {
                        background-color: #f0f0f0;
                        font: 12pt "Arial";
                    }
                    QMessageBox QLabel {
                        color: blue;
                    }
                """)

        msg.exec_()


    def checkForDraw(self):
        for i in self.buttons:
            if i.text() == "":
                return False
        msg = QMessageBox()
        msg.setWindowTitle("O'yin Yakuni")
        msg.setText(f"Durrang bo'ldi!")
        msg.setInformativeText("Yana o'ynash uchun 'RESTART' tugmasini bosing.")
        msg.setStyleSheet("""
                    QMessageBox {
                        background-color: #f0f0f0;
                        font: 12pt "Arial";
                    }
                    QMessageBox QLabel {
                        color: blue;
                    }
                """)
        msg.exec_()
        return True
    
    def applyStyles(self):
        # Umumiy uslubni barcha elementlarga qo'llash
        self.setStyleSheet("""
            QWidget {
                background-color: #ecf0f1;
            }
            QPushButton {
                background-color: #ADD8E6;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QCheckBox {
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }               
            QPushButton:hover {
                background-color: #87CEEB;
            }
            QCheckBox:hover {
                background-color: #d6dbdf;
            }
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: green;
            }
        """)



app = QApplication([])
oyna = MyWindow()
oyna.show()
app.exec_()