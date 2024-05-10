import sys
from PyQt5.QtWidgets import QApplication, QTextBrowser, QVBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the window
        self.setWindowTitle('QTextBrowser Example')
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout(self)

        # Create the QTextBrowser
        text_browser = QTextBrowser()
        text_browser.setHtml("<h1>Hello World!</h1><p>This is an example of <b>QTextBrowser</b>.</p>")
        
        # Add the QTextBrowser to the layout
        layout.addWidget(text_browser)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()