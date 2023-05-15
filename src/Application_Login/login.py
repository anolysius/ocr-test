import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from src.Application_Login.UI.login_window import Ui_w_LoginForm

class LoginForm(qtw.QWidget, Ui_w_LoginForm):
    login_success = qtc.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # button connection
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.process_login)

    @qtc.Slot()
    def process_login(self):
        if self.ie_userId.text() == 'Jason' and self.ie_Password.text() == 'Password':
            self.login_success.emit()
            self.close()
        else:

            self.label_3.setText("Login Fail")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = LoginForm()
    window.show()

    sys.exit(app.exec())
