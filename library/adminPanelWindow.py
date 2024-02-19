from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

from mySQL import MySQL

class AdminPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()

        self.lbl = QLabel("KITOB QO'SHISH")
        self.bookName_edit = QLineEdit()
        self.bookName_edit.setPlaceholderText("Name of the book...")
        self.authorName_edit = QLineEdit()
        self.authorName_edit.setPlaceholderText("Author name...")
        self.genre_edit = QLineEdit()
        self.genre_edit.setPlaceholderText('Book genre...')
        self.price_edit = QLineEdit()
        self.price_edit.setPlaceholderText('Book price...')
        self.count_edit = QLineEdit()
        self.count_edit.setPlaceholderText("Book quantity...")

        self.insert_btn = QPushButton("Insert")
        self.insert_btn.clicked.connect(self.Insert)

        self.h_btn_lay.addStretch()
        self.h_btn_lay.addWidget(self.insert_btn)

        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addWidget(self.bookName_edit)
        self.v_main_lay.addWidget(self.authorName_edit)
        self.v_main_lay.addWidget(self.genre_edit)
        self.v_main_lay.addWidget(self.price_edit)
        self.v_main_lay.addWidget(self.count_edit)
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)
    
    def Insert(self):
        db = MySQL()
        author_name = self.authorName_edit.text()
        genre_name = self.genre_edit.text()
        book_name = self.bookName_edit.text()
        price = int(self.price_edit.text())
        count = int(self.count_edit.text())

        if author_name and genre_name and book_name and price and count:

            try:
                authorId = db.takeAuthorIdQuery(author_name)[0]
                if authorId is None:
                    authorId = db.InsertAuthorQuery(author_name)[0]
            
                genreId = db.takeGenreIdQuery(genre_name)[0]
                if genreId is None:
                    genreId = db.InsertGenreQuery(genre_name)[0]
                
                db.InsertBookQuery(book_name, price, count, genreId, authorId)
                # Muvaffaqiyatli xabar
                QMessageBox.information(self, "Muvaffaqiyat", "Kitob muvaffaqiyatli qo'shildi.")

                self.authorName_edit.clear()
                self.genre_edit.clear()
                self.bookName_edit.clear()
                self.price_edit.clear()
                self.count_edit.clear()
            except Exception as e:
                # Xato xabari
                QMessageBox.critical(self, "Xatolik", f"Xatolik yuz berdi: {e}")