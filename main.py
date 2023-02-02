from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
import sys
import requests
from PyQt5.QtGui import QPixmap
from io import BytesIO
import requests
from PIL import Image


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.x_line = QLineEdit(self)
        self.y_line = QLineEdit(self)
        self.choose_btn = QPushButton(self)
        self.choose_btn.setText("Поиск")
        self.x_line.resize(100, 50)
        self.y_line.resize(100, 50)
        self.x_line.move(0, 400)
        self.y_line.move(0, 450)
        self.choose_btn.resize(100, 50)
        self.choose_btn.move(200, 425)
        toponym_coodrinates = '72.582114 61.113427'
        print(toponym_coodrinates)
        toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

        delta = "0.005"

        map_params = {
            "ll": ",".join([toponym_longitude, toponym_lattitude]),
            "spn": ",".join([delta, delta]),
            "l": "map"
        }

        map_api_server = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(map_api_server, params=map_params)

        im = Image.open(BytesIO(
            response.content))
        im.save('res.png')
        self.pixmap = QPixmap('res.png')
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(500, 400)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)

    def initUI(self):
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Яндекс карты")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_widget = Widget()
    my_widget.show()
    sys.exit(app.exec())
