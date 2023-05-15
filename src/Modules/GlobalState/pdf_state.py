from PySide6 import QtCore
from PySide6.QtCore import QObject, Signal
from typing import List, Dict


class PdfState(QObject):
    instance = None
    selected_file = "selected_file"
    selected_file_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self._source: str | None = None

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value: str):
        self._source = value
        self.selected_file_signal.emit(self.selected_file)

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = PdfState()
        return cls.instance
