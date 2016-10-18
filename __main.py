

import UrlParserUi
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from urllib.parse import urlparse

class UrlParserApp(QMainWindow, UrlParserUi.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.parseUrl)

    def parseUrl(self):
        url = self.originalUrl.toPlainText()
        parsedurl = url.replace('&','\n')
        parsedurl = parsedurl.replace('?', '\n')


        # report parsed url
        self.parsedUrl.setPlainText(parsedurl)



if __name__ == "__main__":
    a = QApplication(sys.argv)
    app = UrlParserApp()
    app.show()

    exit(a.exec_())