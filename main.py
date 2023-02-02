from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
import sys
import requests


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

    def initUI(self):
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Яндекс карты")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_widget = Widget()
    my_widget.show()
    sys.exit(app.exec())
