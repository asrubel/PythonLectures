# Qt
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
)

app = QApplication([])

window = QWidget()
window.setWindowTitle("My PyQt App")
window.setGeometry(300, 300, 400, 100)
helloMsg = QLabel("<h1>My PyQt App!!!!</h1>", parent=window)
helloMsg.move(100, 50)

window.show()

sys.exit(app.exec())
