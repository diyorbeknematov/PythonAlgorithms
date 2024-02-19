from typing import Any
import mysql.connector

class MySQL:
    def __init__(self):
        self.ConnectDB()

    def ConnectDB(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="03212164",
            database="Library"
        )
        self.cursor = self.db.cursor()
    
    def SignInUserQuery(self, user_name, age, parol):
        self.cursor.execute(f"""INSERT INTO User(name,age,password)
                                VALUES(\"{user_name}\",{age},\"{parol}\");
                            """)
        self.db.commit()

    def CheckUserQuery(self, user_name):
        self.cursor.execute(f"""SELECT password FROM User 
                            WHERE name = \"{user_name}\";""")
        return self.cursor.fetchone()
    
    def CheckAdminQuery(self, user_name):
        self.cursor.execute(f"""SELECT password FROM admin 
                            WHERE name = \"{user_name}\';""")
        return self.cursor.fetchone()

    def takeAuthorIdQuery(self, author_name):
        self.cursor.execute(f"SELECT id FROM Author WHERE avtorlar = \"{author_name}\";")
        return self.cursor.fetchone()
    
    def InsertAuthorQuery(self, author_name):
        self.cursor.execute(f"INSERT INTO Author(avtorlar) VALUES(\"{author_name}\");")
        self.db.commit()

        self.cursor.execute(f"SELECT id from Author WHERE avtorlar = \"{author_name}\";")
        return self.cursor.fetchone()

    def takeGenreIdQuery(self, genre_name):
        self.cursor.execute(f"SELECT id FROM Genre WHERE janr = \"{genre_name}\";")
        return self.cursor.fetchone()

    def InsertGenreQuery(self, genre):
        self.cursor.execute(f"INSERT INTO Genre(janr) VALUES(\"{genre}\");")
        self.db.commit()

        self.cursor.execute(f"SELECT id from Genre WHERE janr = \"{genre}\";")
        return self.cursor.fetchone()

    def InsertBookQuery(self, book_name, price, count, idJ, idA):
        self.cursor.execute(f"""INSERT INTO Book(name, price, count, janr_id, author_id) VALUES
                            (\"{book_name}\", {price}, {count}, {int(idJ)}, {int(idA)});""")
        self.db.commit()

    def allGenreQuery(self):
        self.cursor.execute("SELECT janr FROM GENRE;")
        return self.cursor.fetchall()

    def allAuthorQuery(self):
        self.cursor.execute("SELECT avtorlar FROM Author;")
        return self.cursor.fetchall()
    

    
    def SearcheBookG(self, genre):
        self.cursor.execute(f"""SELECT b.id, b.name, a.avtorlar, g.janr, b.count, b.price FROM Book as b
                            INNER JOIN Author as a ON b.author_id = a.id
                            INNER JOIN Genre as g ON b.janr_id = g.id
                            WHERE g.janr = \"{genre}\"""")
        return self.cursor.fetchall()
    
    def SearcheBookA(self, author):
        self.cursor.execute(f"""SELECT b.id, b.name, a.avtorlar, g.janr, b.count, b.price FROM Book as b
                            INNER JOIN Author as a ON b.author_id = a.id
                            INNER JOIN Genre as g ON b.janr_id = g.id
                            WHERE a.avtorlar = \"{author}\"""")
        return self.cursor.fetchall()
    
    def SearcheBookN(self, book_name):
        self.cursor.execute(f"""SELECT b.id, b.name, a.avtorlar, g.janr, b.count, b.price FROM Book as b
                            INNER JOIN Author as a ON b.author_id = a.id
                            INNER JOIN Genre as g ON b.janr_id = g.id
                            WHERE b.name = \"{book_name}\"""")
        return self.cursor.fetchall()
    
    def SearcheBookAG(self, author, genre):
        self.cursor.execute(f"""SELECT b.id, b.name, a.avtorlar, g.janr, b.count, b.price FROM Book as b
                            INNER JOIN Author as a ON b.author_id = a.id
                            INNER JOIN Genre as g ON b.janr_id = g.id
                            WHERE a.avtorlar = \"{author}\" and g.janr = \"{genre}\";""")
        return self.cursor.fetchall()
    
    def SearcheBookAN(self, author, book_name):
        self.cursor.execute(f"""SELECT b.id, b.name, a.avtorlar, g.janr, b.count, b.price FROM Book as b
                            INNER JOIN Author as a ON b.author_id = a.id
                            INNER JOIN Genre as g ON b.janr_id = g.id
                            WHERE a.avtorlar = \"{author}\" and b.name = \"{book_name}\";
                            """)
        return self.cursor.fetchall()
        
    def SearcheBookGN(self, book_name, genre):
        self.cursor.execute(f"""SELECT b.id, b.name, a.avtorlar, g.janr, b.count, b.price FROM Book as b
                            INNER JOIN Author as a ON b.author_id = a.id
                            INNER JOIN Genre as g ON b.janr_id = g.id
                            WHERE g.janr = \"{genre}\" and b.name = \"{book_name}\";
                            """)
        return self.cursor.fetchall()
        
    def SearcheBookAGN(self, book_name, author, genre):
        self.cursor.execute(f"""SELECT b.id, b.name, a.avtorlar, g.janr, b.count, b.price FROM Book as b
                            INNER JOIN Author as a ON b.author_id = a.id
                            INNER JOIN Genre as g ON b.janr_id = g.id
                            WHERE a.avtorlar = \"{author}\" and b.name = \"{book_name}\" and g.janr = \"{genre}\";
                            """)
        return self.cursor.fetchall()
    
    def SearcheBookId(self, id):
        self.cursor.execute(f"SELECT count FROM Book WHERE id = {id};")
        return self.cursor.fetchone()

    def UpdateBookCount(self, count, id):
        self.cursor.execute(f"UPDATE Book SET count = {count} WHERE id = {id};")
        self.db.commit()