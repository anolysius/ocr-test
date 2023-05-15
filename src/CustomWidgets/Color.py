from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        # Next we get the current palette (which is the global desktop palette by default)
        palette = self.palette()
        # change the current QPalette.Window color to a new QColor described by the value color we passed in
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
