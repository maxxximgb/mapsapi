import io
import sys

import requests
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
import geocoder

api_key = '7ab4d70e-469b-4d33-a528-0d04c7f43a9c'


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.pixmap = QPixmap()
        self.maplabel = QLabel()
        self.lout = QVBoxLayout()
        self.lout.addWidget(self.maplabel)
        self.setLayout(self.lout)
        self.request_map('Владикавказ')
        self.show()

    def request_map(self, coords=None, span=None, address=None):

        if coords and span:
            ls = coords, span
        else:
            ls = geocoder.get_ll_span(address)

        map_params = {
            "ll": ls[0],
            "spn": ls[1],
            "apikey": api_key
        }
        response = requests.get("https://static-maps.yandex.ru/v1", params=map_params)
        if response.status_code == 403:
            self.lout.addWidget(QLabel(text='Статус 403'))
        else:
            self.pixmap.loadFromData(response.content)
            self.maplabel.setPixmap(self.pixmap)


app = QApplication(sys.argv)
mainclass = App()
app.exec()
