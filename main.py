import os
import sys

import PySide6.QtWidgets as qtw
import PySide6.QtGui as qgi

from src.CustomWidgets import ItemList, FormLayout, PdfViewer
from src.Modules import convertImageToText, PdfState

"""
 Layout 
  * w/o add widget layout does not do anything, now appearing in its parent 
"""


def openFileDialog(parent: qtw.QMainWindow):
    file_dialog = qtw.QFileDialog()
    file_dialog.setWindowTitle("Select Pdf File")
    file_dialog.setFileMode(qtw.QFileDialog.FileMode.ExistingFile)
    file_dialog.setNameFilter('*.pdf')
    if file_dialog.exec() == 1:
        # 파일 경로 state 에 저장
        convertImageToText(file_dialog.selectedFiles()[0])
        PdfState.getInstance().source = file_dialog.selectedFiles()[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    os.environ["QT_MAC_WANTS_LAYER"] = "1"

    # image to text
    # convertImageToText()

    app = qtw.QApplication(sys.argv)

    window = qtw.QMainWindow()
    window.setWindowTitle("LOVELY SUE")
    window.resize(1280, 720)

    main_v_layout = qtw.QGridLayout()

    items_list_widget = ItemList()
    top_h_layout = qtw.QHBoxLayout()
    top_h_layout.addWidget(items_list_widget, 2)

    form_layout = FormLayout()
    top_h_layout.addLayout(form_layout, 4)

    pdf_widget = PdfViewer()
    top_h_layout.addWidget(pdf_widget, 6)

    add_btn = qtw.QPushButton("Manual Add")
    delete_btn = qtw.QPushButton("Delete")
    bottom_h_layout = qtw.QHBoxLayout()
    bottom_h_layout.addWidget(add_btn)
    bottom_h_layout.addWidget(delete_btn)

    main_v_layout.setRowStretch(0, 11)
    main_v_layout.setRowStretch(1, 1)
    main_v_layout.addLayout(top_h_layout, 0, 0)
    main_v_layout.addLayout(bottom_h_layout, 1, 0)

    widget = qtw.QWidget()
    widget.setLayout(main_v_layout)
    window.setCentralWidget(widget)

    window.setCentralWidget(widget)

    # Add StatusBar
    window.setStatusBar(qtw.QStatusBar(window))

    button_action = qgi.QAction("&Select File", window)
    button_action.setStatusTip("Select pdf File")
    button_action.triggered.connect(openFileDialog)

    # Add Toolbar
    toolbar = qtw.QToolBar("Main Toolbar")
    toolbar.addAction(button_action)
    toolbar.setMovable(False)
    window.addToolBar(toolbar)

    # Add Menu Bar
    # menu = window.menuBar()
    # file_menu = menu.addMenu("&File")
    """
    w/o addAction button does not appear on menu
    """
    # file_menu.addAction(button_action)

    window.show()
    app.exec()
