# Qt
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QVBoxLayout,
    QPushButton
)


def greet():
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText("Hi!")


app = QApplication([])

window = QWidget()
window.setWindowTitle("App with Button")
layout = QVBoxLayout()

button = QPushButton("Greet")
button.clicked.connect(greet)

layout.addWidget(button)
msgLabel = QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)

window.show()
sys.exit(app.exec())
