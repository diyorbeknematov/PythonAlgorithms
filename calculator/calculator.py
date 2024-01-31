from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import Qt, QEvent
import math


class MyWindow(QWidget):
    def __init__(self, title) -> None:
        super().__init__()
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon("D:\\Python\python_darslar\\17-dars\\uyga vazifa\\calculator\images\\calculator.png"))
        self.setFixedSize(400, 480)
        self.initUI()
        self.show()
    
    def initUI(self):
        gridLayout = QGridLayout(self)

        # QLabel va QLineEdit uchun alohida QVBoxLayout
        topLayout = QVBoxLayout()
        topLayout.setSpacing(0)  # QLabel va QLineEdit orasidagi bo'shliq yo'q qilinadi
        # topLayout.setContentsMargins(0, 10, 0, 0)


        self.operationLabel = QLabel(self)
        self.edit = QLineEdit(self)
        self.styleLabel()
        self.styleLineEdit()
        self.edit.textChanged.connect(self.onEditChanged)

        topLayout.addWidget(self.operationLabel)
        topLayout.addWidget(self.edit)
        gridLayout.addLayout(topLayout, 0, 0, 1, 4)  # topLayout gridLayoutga qo'shiladi


        # Asosiy raqamli tugmalar
        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")
        self.btn4 = QPushButton("4")
        self.btn5 = QPushButton("5")
        self.btn6 = QPushButton("6")
        self.btn7 = QPushButton("7")
        self.btn8 = QPushButton("8")
        self.btn9 = QPushButton("9")
        self.btn0 = QPushButton("0")

        # Amallar
        self.btnQ = QPushButton("+")
        self.btnB = QPushButton("/")
        self.btnK = QPushButton("*")
        self.btnA = QPushButton("-")
        self.btnE = QPushButton("=")
        self.btnC = QPushButton("C")
        self.btnDot = QPushButton(".")
        self.btnAC = QPushButton("⌫")

        # Qo'shimcha funksiyalar
        self.btnXy = QPushButton("x^y")
        self.btnSqrt = QPushButton("√")
        self.btnLog = QPushButton("log")
        self.btnPercent = QPushButton("%")

        # Tugmalar joylashuvi
        gridLayout.addWidget(self.btnAC, 1, 3)
        gridLayout.addWidget(self.btnC, 1, 2)
        gridLayout.addWidget(self.btnXy, 2, 0)
        gridLayout.addWidget(self.btnSqrt, 2, 1)
        gridLayout.addWidget(self.btnLog, 2, 2)
        gridLayout.addWidget(self.btnQ, 2, 3)
        gridLayout.addWidget(self.btn7, 3, 0)
        gridLayout.addWidget(self.btn8, 3, 1)
        gridLayout.addWidget(self.btn9, 3, 2)
        gridLayout.addWidget(self.btnB, 3, 3)
        gridLayout.addWidget(self.btn4, 4, 0)
        gridLayout.addWidget(self.btn5, 4, 1)
        gridLayout.addWidget(self.btn6, 4, 2)
        gridLayout.addWidget(self.btnK, 4, 3)
        gridLayout.addWidget(self.btn1, 5, 0)
        gridLayout.addWidget(self.btn2, 5, 1)
        gridLayout.addWidget(self.btn3, 5, 2)
        gridLayout.addWidget(self.btnA, 5, 3)
        gridLayout.addWidget(self.btnPercent, 6, 0)
        gridLayout.addWidget(self.btn0, 6, 1)
        gridLayout.addWidget(self.btnDot, 6, 2)
        gridLayout.addWidget(self.btnE, 6, 3)

        self.btnE.clicked.connect(self.onEqualClicked)
        self.styleButtons()
        self.setLayout(gridLayout)
        self.styleLineEdit()
        self.styleLabel()


        self.btn1.clicked.connect(lambda: self.onNumberClicked("1"))
        self.btn2.clicked.connect(lambda: self.onNumberClicked("2"))
        self.btn3.clicked.connect(lambda: self.onNumberClicked("3"))
        self.btn4.clicked.connect(lambda: self.onNumberClicked("4"))
        self.btn5.clicked.connect(lambda: self.onNumberClicked("5"))
        self.btn6.clicked.connect(lambda: self.onNumberClicked("6"))
        self.btn7.clicked.connect(lambda: self.onNumberClicked("7"))
        self.btn8.clicked.connect(lambda: self.onNumberClicked("8"))
        self.btn9.clicked.connect(lambda: self.onNumberClicked("9"))
        self.btn0.clicked.connect(lambda: self.onNumberClicked("0"))


        self.btnDot.clicked.connect(self.onDotClicked)
        

        self.btnQ.clicked.connect(lambda: self.onOperationClicked("+"))
        self.btnB.clicked.connect(lambda: self.onOperationClicked("/"))
        self.btnK.clicked.connect(lambda: self.onOperationClicked("*"))
        self.btnA.clicked.connect(lambda: self.onOperationClicked("-"))

        self.btnLog.clicked.connect(self.onLogClicked)
        self.btnXy.clicked.connect(self.onPowerClicked)
        self.btnSqrt.clicked.connect(self.onSqrtClicked)
        self.btnPercent.clicked.connect(self.onPercentClicked)
        self.btnE.clicked.connect(self.onEqualClicked)
        self.btnC.clicked.connect(self.onClearClicked)
        self.btnAC.clicked.connect(self.onBackspaceClicked)

    def onEditChanged(self, text):
        self.operationLabel.setText(text)  # QLabel matnini yangilash


        #Raqamlar uchun
    def onNumberClicked(self, number):
        current_text = self.edit.text()
        new_text = current_text + number
        self.edit.setText(new_text)

        #"Nuqta uchun"
    def onDotClicked(self):
        current_text = self.edit.text()
        if not current_text or not current_text[-1].isdigit():
            # Oxirgi belgi raqam emas, nuqta qo'shilmaydi
            return

        # Oxirgi operandni tekshirish
        for i in range(len(current_text) - 1, -1, -1):
            if current_text[i] in '+-*/^%':
                break
            if current_text[i] == '.':
                return  # Allaqqachon nuqta bor

        self.edit.setText(current_text + ".")
    
        #Amallar uchun
    def onOperationClicked(self, operation):
        current_text = self.edit.text()
        if not current_text.endswith(('+', '-', '*', '/')):
            new_text = current_text + operation
            self.edit.setText(new_text)

        #Logarifm  uchun
    def onLogClicked(self):
        current_text = self.edit.text()
        try:
            result = math.log(float(current_text))
            self.edit.setText(str(result))
        except ValueError:
            self.edit.setText("Error")

        #Daraja uchun
    def onPowerClicked(self):
        current_text = self.edit.text()
        self.edit.setText(current_text + "^")

        #Ildiz uchun
    def onSqrtClicked(self):
        current_text = self.edit.text()
        try:
            result = math.sqrt(float(current_text))
            self.edit.setText(str(result))
        except ValueError:
            self.edit.setText("Error")

        #Foiz uchun
    def onPercentClicked(self):
        current_text = self.edit.text()
        self.edit.setText(current_text + "%")
    
        #Tenglik uchun
    def onEqualClicked(self):
        try:
            expression = self.operationLabel.text()
            if '^' in expression:
                base, exponent = expression.split('^')
                result = math.pow(float(base), float(exponent))
            elif '%' in expression:
                base, percent = expression.split('%')
                result = (float(base) * float(percent)) / 100
            else:
                result = eval(expression)
            self.edit.setText(str(result))
        except Exception as e:
            self.edit.setText("Error")


        #Backspace uchun
    def onBackspaceClicked(self):
        current_text = self.edit.text()
        new_text = current_text[:-1]  
        self.edit.setText(new_text)
    
        # C uchun ya'ni clear
    def onClearClicked(self):
        self.edit.clear()


    def styleButtons(self):
        buttonStyle = """
        QPushButton {
            background-color: #80c1ff;
            color: white;
            border-style: outset;
            border-width: 2px;
            border-radius: 15px;
            font: bold 14px;
            min-width: 40px;
            min-height: 40px;
            padding: 6px;
            cursor: pointer;
        }
        QPushButton:pressed {
            background-color: #559cd8;
            border-style: inset;
        }
        """

        for btn in [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6,
                    self.btn7, self.btn8, self.btn9, self.btn0, self.btnQ, self.btnB,
                    self.btnK, self.btnA, self.btnE, self.btnC, self.btnDot, self.btnXy,
                    self.btnSqrt, self.btnLog, self.btnPercent, self.btnAC]:
            btn.setStyleSheet(buttonStyle) 
            btn.setCursor(QCursor(Qt.PointingHandCursor))

    def styleLineEdit(self):
        lineEditStyle = """
        QLineEdit {
            border: 2px solid #80c1ff;
            border-radius: 10px;
            padding: 5px;
            background-color: #f0f0f0;
            font: bold 14px;
        }
        QLineEdit:focus {
            border: 2px solid #559cd8;
        }
        """
        self.edit.setStyleSheet(lineEditStyle)
        self.edit.setAlignment(Qt.AlignRight)
    
    def styleLabel(self):
        labelStyle = """
        QLabel {
            background-color: #f0f0f0;
            color: #333333;
            font: bold 12px;
            border: 1px solid #f0f0f0;
            padding: 2px;
            text-align: center;
        }
        """
        self.operationLabel.setStyleSheet(labelStyle)
        self.operationLabel.setAlignment(Qt.AlignRight)


app = QApplication([])
oyna = MyWindow("Calculator")

app.exec_()