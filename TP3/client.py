import socket
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys




class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)
        self.label1 = QLabel("Enter your host IP:", self)
        self.label1.move(11, 5)
        self.text = QLineEdit(self)
        self.text.move(10, 30)
        self.label2 = QLabel("Enter your API Key:", self)
        self.label2.move(11, 65)
        self.text2 = QLineEdit(self)
        self.text2.move(10, 90)
        self.label3 = QLabel("Enter the hostname:", self)
        self.label3.move(11, 125)
        self.text3 = QLineEdit(self)
        self.text3.move(10, 150)
        self.label4 = QLabel("Answer:", self)
        self.label4.move(10, 180)
        self.button = QPushButton("Send", self)
        self.button.move(10, 200)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()



    def on_click(self):
        host_IP=self.text.text()
        API_key=self.text2.text()
        hostname = self.text3.text()


        if hostname == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res= self.__query(host_IP,API_key,hostname)

    def __query(self,host_IP,API_key, hostname):
        url = "http://%s" % (hostname) + "/ip/%s?" % (host_IP) + "key=%s" % (API_key)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()

    
#test