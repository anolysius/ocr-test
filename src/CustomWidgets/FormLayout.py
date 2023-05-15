from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QFormLayout, QLabel, QLineEdit

from src.Modules import GlobalState


class FormLayout(QFormLayout):
    def __init__(self):
        super(FormLayout, self).__init__()
        # Qt.AlignLeft | Qt.AlignTop
        # Set the form layout alignment to stretch the labels and fields
        self.setFormAlignment(Qt.AlignmentFlag.AlignLeft)
        # Set the growth policy for the fields to expand horizontally
        self.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        page = QLabel("Page No:")
        page_edit = QLineEdit()
        page_edit.setDisabled(True)
        page_edit.setText('1')
        self.addRow(page, page_edit)

        self.title = QLabel("Title:")
        self.title_edit = QLineEdit()
        self.addRow(self.title, self.title_edit)

        self.first = QLabel("First Name:")
        self.first_edit = QLineEdit()
        self.addRow(self.first, self.first_edit)

        self.middle = QLabel("Middle Name:")
        self.middle_edit = QLineEdit()
        self.addRow(self.middle, self.middle_edit)

        self.last = QLabel("Last Name:")
        self.last_edit = QLineEdit()
        self.addRow(self.last, self.last_edit)

        self.suffix = QLabel("Suffix:")
        self.suffix_edit = QLineEdit()
        self.addRow(self.suffix, self.suffix_edit)

        # Usually None
        self.title_line = QLabel("Title Line:")
        self.title_line_edit = QLineEdit()
        self.addRow(self.title_line, self.title_line_edit)

        # Rarely Used
        self.extra_addr = QLabel("Extra Addr Line:")
        self.extra_addr_edit = QLineEdit()
        self.addRow(self.extra_addr, self.extra_addr_edit)

        self.street_line = QLabel("Street Line:")
        self.street_line_edit = QLineEdit()
        self.addRow(self.street_line, self.street_line_edit)

        # Apt number
        self.number_line = QLabel("Number:")
        self.number_line_edit = QLineEdit()
        self.addRow(self.number_line, self.number_line_edit)

        self.zip_line = QLabel("ZIP Code:")
        self.zip_line_edit = QLineEdit()
        self.addRow(self.zip_line, self.zip_line_edit)

        # Donation type
        self.code_line = QLabel("CODE LINE:")
        self.code_line_edit = QLineEdit()
        self.addRow(self.code_line, self.code_line_edit)

        self.comm_line = QLabel("COMM1:")
        self.comm_line_edit = QLineEdit()
        self.addRow(self.comm_line, self.comm_line_edit)

        self.mail_code_line = QLabel("MAIL CODE:")
        self.mail_code_line_edit = QLineEdit()
        self.addRow(self.mail_code_line, self.mail_code_line_edit)

        GlobalState.getInstance().select_signal.connect(self.updateEdit)

    @Slot(str)
    def updateEdit(self):
        selectItem = GlobalState.getInstance().selectedState
        if selectItem is not None:
            self.title_edit.setText(selectItem.title if selectItem.title else '')
            self.first_edit.setText(selectItem.firstName if selectItem.firstName else '')
            self.middle_edit.setText(selectItem.middleName if selectItem.middleName else '')
            self.last_edit.setText(selectItem.lastName if selectItem.lastName else '')
            self.street_line_edit.setText(selectItem.streetLine if selectItem.streetLine else '')
            self.zip_line_edit.setText(selectItem.zipCode if selectItem.zipCode else '')
            self.mail_code_line_edit.setText(selectItem.mailCode if selectItem.mailCode else '')
