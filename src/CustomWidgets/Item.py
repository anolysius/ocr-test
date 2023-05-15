from PySide6.QtCore import Slot
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QCheckBox

from src.Modules import GlobalState


class Item(QListWidgetItem):
    def __init__(self, page_no):
        super(Item, self).__init__()
        self.page_no = page_no
