from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QCheckBox, QVBoxLayout, QScrollArea, QSizePolicy, QMessageBox

from mySQL import MySQL

class SotibOlishWindow(QWidget):
    def __init__(self, book_data):
        super().__init__()
        self.setWindowTitle("Mavjud Kitoblar")
        self.initUI(book_data)

    def initUI(self, book_data):
        self.v_main_lay = QVBoxLayout()

        # QScrollArea yaratish
        scrollArea = QScrollArea(self)
        scrollArea.setWidgetResizable(True)

        # ScrollArea uchun ichki widget yaratish
        contentWidget = QWidget()
        scrollArea.setWidget(contentWidget)
        self.gridLayout = QGridLayout(contentWidget)
        self.gridLayout.setSpacing(0)

        headers = ['ID', "Kitob nomi", "Muallif", "Janr", "Miqdori", "Narxi", "Tanlash"]
        for i, header in enumerate(headers):
            label = QLabel(header)
            label.setStyleSheet("border: 1px solid black; font-weight: bold; font-size: 14px")
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            self.gridLayout.addWidget(label, 0, i)


        self.checkboxes = {}
        current_index = 1
        for row, book in enumerate(book_data, start=1):
            if (book[4]) == 0:
                continue

            for col, data in enumerate(book):
                label = QLabel(str(data))
                label.setStyleSheet("border: 0.5px solid black; height: 20px;")
                self.gridLayout.addWidget(label, current_index, col)
            current_index += 1

            chkBox = QCheckBox("Tanlash")
            chkBox.setStyleSheet("border: 0.5px solid black; height: 20px;")
            chkBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


            self.gridLayout.addWidget(chkBox, row, len(headers)-1)
            self.checkboxes[chkBox] = [int(book[0]), book[1]]

        self.sellButton = QPushButton("Tanlanganlarni sotib olish")
        self.sellButton.clicked.connect(self.sellSelectedBooks)

        self.v_main_lay.addWidget(scrollArea)
        self.v_main_lay.addWidget(self.sellButton)
        self.setLayout(self.v_main_lay)

    def sellSelectedBooks(self):
        db = MySQL()
        self.close()
        selected_books = [book_name for chkBox, book_name in self.checkboxes.items() if chkBox.isChecked()]

        for selected_book in selected_books:
            try:
                count = int(db.SearcheBookId(selected_book[0])[0])

                if count > 0:
                    db.UpdateBookCount(count - 1, selected_book[0])
                
                QMessageBox.information(self, "Tabriklaymiz", "Xarididingiz uchun tashakkur")
            except Exception as e:
                QMessageBox.critical(self, "Xatolik", f"Xatolik yuz berdi: {e}")
        