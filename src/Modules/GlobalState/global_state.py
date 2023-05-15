from PySide6 import QtCore
from PySide6.QtCore import QObject, Signal
from typing import List, Dict

from src.Modules import Meta


class GlobalState(QObject):
    instance = None
    state_update = 'state_update'
    move_page = 'move_page'
    selected_state = 'selected_state'

    signal = Signal(str)
    move_signal = Signal(str)
    select_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self._state: List[Meta] = []
        self._selected_state: Meta | None = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value: List[Dict[str, str]]):
        self._state = value
        self.signal.emit(self.state_update)

    @property
    def selectedState(self):
        return self._selected_state

    @selectedState.setter
    def selectedState(self, value: Dict[str, str]):
        self._selected_state = value
        self.select_signal.emit(self.selected_state)
        self.move_signal.emit(self.move_page)

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = GlobalState()
        return cls.instance
