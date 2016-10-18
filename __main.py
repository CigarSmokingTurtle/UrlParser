

import UrlParserUi
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from urllib.parse import urlparse
from urllib.request import url2pathname

class UrlParserApp(QMainWindow, UrlParserUi.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.parseUrl)

    def parseUrl(self):
        url = self.originalUrl.toPlainText()
        parsedurl = str(urlparse(url))
        parsedurl = parsedurl.replace(',', '\n')
        parsedurl = parsedurl.replace('&', '\n')
        parsedurl = str(url2pathname(parsedurl))
        parsedurl = parsedurl.replace('query=\'', 'query=\n')


        # report parsed url
        self.parsedUrl.setPlainText(parsedurl)



if __name__ == "__main__":
    a = QApplication(sys.argv)
    app = UrlParserApp()
    app.show()

    exit(a.exec_())