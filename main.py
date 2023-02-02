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
        self.image = QLabel(self)
        self.x_coords = QLabel(self)
        self.y_coords = QLabel(self)
        self.x_coords.setText("x")
        self.y_coords.setText("y")
        self.x_coords.resize(50, 50)
        self.y_coords.resize(50, 50)
        self.x_coords.move(105, 400)
        self.y_coords.move(105, 450)
        self.x_line.move(0, 400)
        self.y_line.move(0, 450)
        self.x_line.setText("45")
        self.y_line.setText("55")
        self.choose_btn.resize(100, 50)
        self.choose_btn.move(200, 425)
        self.do_image()
        self.choose_btn.clicked.connect(self.do_image)

    def initUI(self):
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Яндекс карты")

    def do_image(self):
        try:
            toponym_coodrinates = f"{self.x_line.text()} {self.y_line.text()}"
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
            #мой код,а не его
            self.pixmap = QPixmap('res.png')
            self.image.move(0, 0)
            self.image.resize(500, 400)
            self.image.setPixmap(self.pixmap)
        except Exception:
            print("Не надо ломать программу")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_widget = Widget()
    my_widget.show()
    sys.exit(app.exec())