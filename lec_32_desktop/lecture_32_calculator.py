import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QMainWindow,
    QLineEdit,
    QGridLayout
)
from PyQt6.QtCore import Qt
from functools import partial

WINDOW_SIZE = 255
DISPLAY_HEIGHT = 40
BUTTON_SIZE = 40
ERROR = "ERROR"


class PyCalc(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(self.generalLayout)
        self.setCentralWidget(central_widget)
        self._create_display()
        self._create_buttons()

    def _create_display(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _create_buttons(self):
        self.button_map = {}
        buttons_layout = QGridLayout()
        key_board = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]

        for row, keys in enumerate(key_board):
            for col, key in enumerate(keys):
                self.button_map[key] = QPushButton(key)
                self.button_map[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttons_layout.addWidget(self.button_map[key], row, col)

        self.generalLayout.addLayout(buttons_layout)

    def set_display_text(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def display_text(self):
        return self.display.text()

    def clear_display(self):
        self.set_display_text("")


def evaluate_expr(expr):
    try:
        res = str(eval(expr, {}, {}))
    except Exception:
        res = ERROR
    return res


class Controller:

    def __init__(self, model, view: PyCalc):
        self._evaluate = model
        self._view = view
        self._connect_all()

    def _calculate_result(self):
        res = self._evaluate(expr=self._view.display_text())
        self._view.set_display_text(res)

    def _build_expr(self, sub_expr):
        if self._view.display_text() == ERROR:
            self._view.clear_display()
        expr = self._view.display_text() + sub_expr
        self._view.set_display_text(expr)

    def _connect_all(self):
        for key_symbol, button in self._view.button_map.items():
            if key_symbol not in {'=', 'C'}:
                button.clicked.connect(
                    partial(self._build_expr, key_symbol)
                )
        self._view.button_map['='].clicked.connect(self._calculate_result)
        self._view.display.returnPressed.connect(self._calculate_result)
        self._view.button_map['C'].clicked.connect(self._view.clear_display)


if __name__ == "__main__":
    app = QApplication([])
    py_calc_window = PyCalc()
    py_calc_window.show()
    Controller(model=evaluate_expr, view=py_calc_window)
    sys.exit(app.exec())
