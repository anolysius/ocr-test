import os
import sys

"""
Not used
# Open cv2 package
import cv2
import qrcode

from reportlab.graphics import renderPM
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter, A4
from pypdf import PdfReader, PdfWriter
from zxing import BarCodeReader
"""

import re
from typing import List, Tuple

# this not working for pdf merge
from pdf2image import convert_from_path, convert_from_bytes
# this working for pdf merge
import fitz
# extract text
import easyocr

from .GlobalState import GlobalState
from .Dto import Meta
from .utils import isCommonForm, isMailForm, extractNames, extractTotalAddress
from PIL import Image


# extract text by pytesseract
# import pytesseract

# pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

def convertImageToText(filePath: str):
    reader = easyocr.Reader(['en'], model_storage_directory=os.path.join(os.path.dirname(__file__), '../detector'))
    documents = fitz.open(filePath)
    next_items = []
    matrix = fitz.Matrix(2, 2)
    for pageNo, document in enumerate(documents):
        pixmap = document.get_pixmap(matrix=matrix)
        pixmap_bytes = pixmap.tobytes()
        extracted_Text = reader.readtext(pixmap_bytes, detail=0)

        if len(extracted_Text) > 2:
            if isCommonForm(extracted_Text):
                meta = {'page_no': pageNo}
                names = extractNames(extracted_Text)
                if names is not None:
                    meta['title'] = names.get('title')
                    meta['first_name'] = names.get('first_name')
                    meta['middle_name'] = names.get('middle_name')
                    meta['last_name'] = names.get('last_name')

                full_address = extractTotalAddress(extracted_Text)
                if full_address is not None:
                    meta['street_line'] = full_address.get('address')
                    meta['zip_code'] = full_address.get('zip')
                    meta['mail_code'] = full_address.get('mail_code')

                next_items.append(Meta(**meta))
            elif isMailForm(extracted_Text):

                shape = document.new_shape()
                x, y, height = document.rect.br[0] / 2, 0, document.rect.br[1] / 5
                shape.draw_rect(fitz.Rect(x, y, document.rect.br[0], height))
                shape.finish(color=(1, 1, 1), fill=(1, 1, 1))
                shape.commit()

                pixmap = document.get_pixmap(matrix=matrix)
                pixmap_bytes = pixmap.tobytes()
                extracted_Text = reader.readtext(pixmap_bytes, detail=0)
                print('-----------')
                print(extracted_Text)
                print('-----------')
                meta = Meta(**{'page_no': pageNo})
                next_items.append(meta)

        # print(extracted_Text)
        # -----------
        # image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
        # grayscale_image = image.convert("L")
        # extracted_Text = pytesseract.image_to_string(grayscale_image)
        # print(extracted_Text)
        # -----------
        # meta_date = extractMetaData(extracted_Text)
        # if meta_date is not None:
        #     meta_date['page_no'] = pageNo
        #     next_items.append(meta_date)
        # print(extractMetaData(extracted_Text))

    GlobalState.getInstance().state = next_items
    documents.close()
    # single_doc = documents[0]
    # pixmap = single_doc.get_pixmap()
    # pix_bytes = pixmap.tobytes()
    # extracted_Text = reader.readtext(pix_bytes, detail=0, paragraph=True)
    # pix.save(readTarget)  # store image as a PNG


class PdfManager:
    def __init__(self):
        pass

# variables
# testPng = 'MyQRCode1.png'
# without_img = './inputPdf/without.pdf'
# with_img = './inputPdf/with.pdf'
# readTarget = 'with_png.png'
# --handle QRCODE
# ------ make qr code
# qr = qr_manager.py.QRCode(
#     error_correction=qr_manager.py.constants.ERROR_CORRECT_Q,
#     border=1,
#     box_size=2
# )
# qr.add_data('firstName: MyungSoo, LastName: Park, ZipCode:22630')
# qr.make(fit=True)
# img = qr.make_image(fill_color="black", back_color="transparent")
# img.save(testPng)

# ------ convert svg to png
# drawing = svg2rlg('22.svg')

# ------ convert pdf to png
# documents = fitz.open(with_img)
# single_doc = documents[0]
# pix = single_doc.get_pixmap()  # render page to an image
# pix.save(readTarget)  # store image as a PNG


# ------ read qr code
# can read transparent
# reader = BarCodeReader()
# barcode = reader.decode(readTarget)
# print(barcode.parsed)

# can't read transparent
# img = cv2.imread(readTarget)
# qrDetector = cv2.QRCodeDetector()
# decodedText, points, _ = qrDetector.detectAndDecode(img)
# print(decodedText, points)
##

# --handle pdf
#
# packet = io.BytesIO()
# can = Canvas(packet, pagesize=A4)
#
# x = 500
# y = 20
#
# can.drawImage(testPng, x, y, mask='auto', preserveAspectRatio=True, anchor='c')
# can.showPage()
# can.save()
#
# # move to the beginning of the StringIO buffer
# packet.seek(0)
# temp_pdf = PdfReader(packet)
#
# without_Pdf = PdfReader(without_img)
# output_writer = PdfWriter()
#
# page = without_Pdf.pages[0]
# page.merge_page(temp_pdf.pages[0])

# output_writer.add_page(page)

# w = write, b = binary mode
# outputStream = open(with_img, "wb")
# output_writer.write(outputStream)
# outputStream.close()
