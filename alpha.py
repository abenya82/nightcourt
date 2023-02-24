from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QPushButton,QMessageBox
from PyQt5.QtGui import QFont

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100,100,200,300)
    window.setWindowTitle("My Simple GUI")


    layout = QVBoxLayout()

    label = QLabel("Press Button")
    button = QPushButton("Press Me")

    button.clicked.connect(on_clicked)


    layout.addWidget(label)
    layout.addWidget(button)

    window.setLayout(layout)

    window.show()
    app.exec_()


def on_clicked():
    message = QMessageBox()
    message.setText("Hello World")
    message.exec_()


if __name__ == '__main__':
    main()