from PySide6.QtCore import Slot
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QCheckBox

from src.CustomWidgets.Item import Item
from src.Modules import GlobalState


class ItemList(QListWidget):
    def __init__(self):
        super(ItemList, self).__init__()
        GlobalState.getInstance().signal.connect(self.updateListItem)
        self.itemClicked.connect(self.handleItemClick)

    @Slot(str)
    def updateListItem(self, message):
        print(message)
        self.clear()
        metas = GlobalState.getInstance().state
        for index, item in enumerate(metas):
            item_widget = Item(item.pageNo)
            checkbox = QCheckBox(str(item.pageNo) + ':' + item.firstName if item.firstName else 'no name')
            checkbox.setProperty('id', item.pageNo)
            item_widget.setSizeHint(checkbox.sizeHint())
            self.addItem(item_widget)
            self.setItemWidget(item_widget, checkbox)

    @Slot()
    def handleItemClick(self):
        print(self.currentItem())
        states = GlobalState.getInstance().state
        found_meta = [m for m in states if m.pageNo == self.currentItem().page_no]
        if found_meta is not None:
            GlobalState.getInstance().selectedState = found_meta[0]
