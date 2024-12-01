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
    c.setFillColorRGB(0.5, 0.5, 0.5, 0.3)  # Gris clair avec transparence

    width, height = A4
    # Positionner les filigranes en diagonale sur toute la page
    for x in range(0, int(width), 200):
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
filename="Bulletin_10_2024"
input_pdf = rf"C:\\Users\\cnco\\Documents Local\\Perso\\Dossier Loc\\{filename}.pdf"
output_pdf = rf"C:\\Users\\cnco\\Documents Local\\Perso\\Dossier Loc\\{filename}_cc.pdf"
watermark_text = "Document exclusivement destiné à la location immobilière"

add_watermark_to_pdf(input_pdf, output_pdf, watermark_text)
