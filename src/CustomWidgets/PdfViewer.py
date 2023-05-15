from PySide6.QtCore import Slot, QPoint
from PySide6.QtPdf import QPdfDocument, QPdfLink
from PySide6.QtPdfWidgets import QPdfView

from src.Modules import PdfState, GlobalState


class PdfViewer(QPdfView):
    def __init__(self):
        super(PdfViewer, self).__init__()
        self.pdf_document = QPdfDocument()

        self.setPageMode(QPdfView.PageMode.MultiPage)
        self.setDocument(self.pdf_document)

        PdfState.getInstance().selected_file_signal.connect(self.bindDocument)
        GlobalState.getInstance().move_signal.connect(self.moveDocument)

    @Slot(str)
    def bindDocument(self, message):
        if PdfState.getInstance().source is not None:
            self.pdf_document.load(PdfState.getInstance().source)

    @Slot(str)
    def moveDocument(self):
        selectItem = GlobalState.getInstance().selectedState

        if selectItem is not None:
            nav = self.pageNavigator()
            nav.jump(selectItem.pageNo, QPoint(), nav.currentZoom())
