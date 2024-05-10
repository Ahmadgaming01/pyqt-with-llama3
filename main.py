
import ollama
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qt_material import apply_stylesheet
from PyQt5.QtWidgets import QWidget 
from qt_material import list_themes


# sys library 

import sys 
import os
from os import path 



# loader for ui design 
from PyQt5.uic import loadUiType

FORM_CLASS,_ = loadUiType(os.path.join(path.dirname(__file__) , 'ollama.ui')) 
class Main (QMainWindow ,FORM_CLASS):
    def __init__(self, parent=None ):
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_button()
        self.clear_output()
        #self.handel_output_text()
        #self.handel_input_text()
        self.chat_generator()

    def chat_generator(self):
        
        input_text = self.plainTextEdit.toPlainText()
        stream = ollama.chat(
            model='llama3',
            messages=[{'role': 'user', 'content': input_text}],
            stream=True,
        )


        for chunk in stream:
            result = (chunk['message']['content'])
            
            self.textBrowser.insertPlainText(result + " ")
            QApplication.processEvents()
            self.plainTextEdit.setPlainText("")
            




    def clear_output(self):
        self.textBrowser.setText('')
    def handel_button(self):
        self.pushButton.clicked.connect(self.chat_generator)
        self.pushButton_2.clicked.connect(self.clear_output)




    # def handel_input_text(self):
    #     text_input = self.plainTextEdit.toPlainText()
        
        


    # def handel_output_text(self):
    #     pass
    #     #output = ChatGenerator

def main ():
    app = QApplication(sys.argv)
    window = Main()
    apply_stylesheet(app, theme='dark_purple.xml')

    window.show()
    app.exec_()


if __name__ == '__main__':
    main()


