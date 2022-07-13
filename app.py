from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from addbook_dialog import Ui_Dialog as Ui_Addbook
from delete_dialog import Ui_Dialog as Ui_Delete_Dialog
from edit_dialog import Ui_Dialog as UI_Edit_Dialog
from main_win import Ui_MainWindow 
import my_functions as lib

class Addbook_Window(QDialog):
    def __init__(self,parent = None):
        super(Addbook_Window,self).__init__(parent)
        self.ui = Ui_Addbook()
        self.ui.setupUi(self)
        self.ui.edit_buttonbox.accepted.connect(self.accept)
        self.ui.edit_buttonbox.rejected.connect(self.reject)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.new_book.pressed.connect(self.show_addBook)
        print(lib.load_books()[0].to_dict())
    
    def show_addBook(self):
        input = Addbook_Window()
        input.ui.edit_buttonbox.accepted.connect(
            lambda: self.sadve_book(input.ui))
        input.exec()    
    
    def to_dict(self,ui):
        new_book = {
            "id" : int(ui.id_addB.text()),
            "name": ui.name_addB.text(),
            "description": ui.desc_addB.text(),
            "isbn": int(ui.isbn_addB.text()),
            "page_count": int(ui.page_addB.text()),
            "issued": ui.Yes.isChecked(),
            "author": ui.author_addB.text(),
            "year": int(ui.year_addB.text())
        }

        for attr in new_book:
            if new_book[attr] == None or str(new_book[attr]) == "":
               return False 
        print(new_book)

        
app = QApplication([])
window = MainWindow()
window.show()
app.exec()