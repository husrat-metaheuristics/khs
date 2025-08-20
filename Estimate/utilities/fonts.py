from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont('MainFont', 'static\_fonts\BOD_R.TTF')
)