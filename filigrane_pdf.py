# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:20:58 2024

@author: cnco
"""

from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO

# Étape 1 : Créer une page PDF avec plusieurs filigranes en diagonale
def create_repeating_watermark(watermark_text):
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)
    c.setFont("Helvetica", 15)
    c.setFillColorRGB(0.4, 0.4, 0.4, 0.8)  # Gris clair avec transparence

    width, height = A4
    # Positionner les filigranes en diagonale sur toute la page
    for x in range(50, int(width), 200):
        for y in range(0, int(height), 100):
            c.saveState()
            c.translate(x, y)
            c.rotate(30)  # Rotation en diagonale
            c.drawCentredString(0, 0, watermark_text)  # Dessiner le texte centré
            c.restoreState()
    c.save()

    packet.seek(0)
    return PdfReader(packet)

# Étape 2 : Appliquer le filigrane sur chaque page du PDF
def add_watermark_to_pdf(input_pdf, output_pdf, watermark_text):
    watermark = create_repeating_watermark(watermark_text)
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        page.merge_page(watermark.pages[0])  # Appliquer la filigrane sur la page
        writer.add_page(page)

    # Sauvegarder le nouveau fichier PDF avec la filigrane
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

# Exemple d'utilisation
filename="12-24"
input_pdf = rf"C:\Users\cnco\Downloads\Dossier Loc\Dossier Loc\{filename}.pdf"
output_pdf = rf"C:\Users\cnco\Downloads\Dossier Loc\Dossier Loc\{filename}_cc.pdf"
output2_pdf = rf"C:\Users\cnco\Downloads\Dossier Loc\Dossier Loc\{filename}_cc_mp.pdf"
watermark_text = "Document exclusivement destiné à la location immobilière"

add_watermark_to_pdf(input_pdf, output_pdf, watermark_text)

###############################################################################
#                                SAVE PDF AS PNG                              #
###############################################################################

import fitz  # PyMuPDF

# Path to the PDF file
pdf_path = output_pdf

# Open the PDF
pdf_document = fitz.open(pdf_path)

# Set the zoom factor for resolution (1.0 = 72 DPI, 2.0 = 144 DPI, etc.)
zoom = 2.0  # Increase for higher resolution
matrix = fitz.Matrix(zoom, zoom)  # Scale horizontally and vertically


# Iterate over PDF pages
for page_number in range(len(pdf_document)):
    # Get the page
    page = pdf_document.load_page(page_number)

    # Render page to a pixmap (image)
    pix = page.get_pixmap(matrix=matrix)

    # Save the image as PNG
    pix.save(rf"C:\Users\cnco\Downloads\Dossier Loc\Dossier Loc\{filename}_{page_number + 1}.png")

###############################################################################
#                                SAVE PNG AS PDF                              #
###############################################################################

input('Faire modif sur png')

from PIL import Image

# List of PNG images to convert
image_paths = [rf"C:\Users\cnco\Downloads\Dossier Loc\Dossier Loc\{filename}_1.png"]

# Open the first image and convert it to RGB (required for PDF)
images = [Image.open(img).convert("RGB") for img in image_paths]

# Save the first image as a PDF and append the rest
images[0].save(rf"C:\Users\cnco\Downloads\Dossier Loc\Dossier Loc\{filename}_Loc_mp.pdf", save_all=True, append_images=images[1:])

