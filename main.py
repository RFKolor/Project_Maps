from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Яндекс карты")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_widget = Widget()
    my_widget.show()
    sys.exit(app.exec())
