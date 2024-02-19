from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout, QComboBox, QHBoxLayout, QMessageBox

from SotibOlish import SotibOlishWindow
from mySQL import MySQL

class MyComboBox(QComboBox):
    def __init__(self, placeholder):
        super().__init__()
        self.flag = True
        self.placeholder = placeholder
        self.addItem(self.placeholder)
        self.model().item(0).setEnabled(False)

    def showPopup(self):
        if self.flag:
            self.removeItem(0)
            self.flag = False
            self.setCurrentIndex(-1)
        super().showPopup()


    def hidePopup(self):
        if self.currentIndex() == -1:
            self.insertItem(0, self.placeholder)
            self.setCurrentIndex(0)
            self.model().item(0).setEnabled(False)
            self.flag = True     
        super().hidePopup()

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        

        self.h_combo_lay = QHBoxLayout()
        self.v_main_lay = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()

        self.genre_cm = MyComboBox("Search by genre")

        self.author_cm = MyComboBox("Search by author")

        self.lbl = QLabel("Book search")

        self.book_edit = QLineEdit()
        self.book_edit.setPlaceholderText("Search by book title")

        self.search_btn = QPushButton("SEARCH")
        self.search_btn.clicked.connect(self.Search)

        
        self.h_combo_lay.addWidget(self.genre_cm)
        self.h_combo_lay.addWidget(self.author_cm)

        self.h_btn_lay.addStretch()
        self.h_btn_lay.addWidget(self.search_btn)

        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addLayout(self.h_combo_lay)
        self.v_main_lay.addWidget(self.book_edit)
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

    def Search(self):
        db = MySQL()

        book_name = self.book_edit.text()
        genre = self.genre_cm.currentText()
        author = self.author_cm.currentText()

        book_data = []

        try:
            if book_name and genre == "Search by genre" and author == "Search by author":
                book_data = db.SearcheBookN(book_name)

            elif not book_name and genre != "Search by genre" and author == "Search by author":
                book_data = db.SearcheBookG(genre)

            elif not book_name and genre == "Search by genre" and author != "Search by author":
                book_data = db.SearcheBookA(author)

            elif book_name and genre != "Search by genre" and author == "Search by author":
                book_data = db.SearcheBookGN(book_name, genre)

            elif not book_name and genre != "Search by genre" and author != "Search by author":
                book_data = db.SearcheBookAG(author, genre)

            elif book_name and genre == "Search by genre" and author != "Search by author":
                book_data = db.SearcheBookAN(author, book_name)

            elif book_name and genre != "Search by genre" and author != "Search by author":
                book_data = db.SearcheBookAGN(book_name, author, genre)
            
            else:
                QMessageBox.critical(self, "Tanlov yo'q", "Iltimos, hech bo'lmaganda bir tanlovni amalga oshiring")
                return

            if book_data:
                self.new_window = SotibOlishWindow(book_data)
                self.new_window.show()
            else:
                QMessageBox.information(self, "Natija yo'q", "Bunday malumot asosida hech qanday kitob topilmadi")
        except Exception as e:
            QMessageBox.critical(self, "Xatolik", f"Xatolik yuz berdi: {e}")