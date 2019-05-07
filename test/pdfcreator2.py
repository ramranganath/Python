class fcMaker(object):
""""""
def __init__(self, response):
    self.PAGE_SIZE = (2.75*inch, 3.75*inch)
    self.c = canvas.Canvas(response, pagesize=self.PAGE_SIZE)
    self.styles = style
    self.width, self.height = self.PAGE_SIZE

def createDocument(self):
    """"""
    # Title Page
    title = """Title goes here"""
    p = Paragraph(title, styleH)

    logo = Image("my_cool_logo.jpg")
    logo.drawHeight = 99
    logo.drawWidth = 99

    data = [[logo], [p]]
    table = Table(data, colWidths=2.25*inch)
    table.setStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("TOPPADDING", (0, 0), (-1, -1), 20)])
    table.wrapOn(self.c, self.width, self.height)
    table.drawOn(self.c, *self.coord(.25, 2.75, inch))

    self.c.showPage()

    #Page Two
    side1_text = """Text goes here"""
    p = Paragraph(side1_text, styleF)

    side1_image = Image("first_image.jpg")
    side1_image.drawHeight = 99
    side1_image.drawWidth = 99

    data = [[side1_image], [p]]
    table = Table(data, colWidths=2.25*inch)
    table.setStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("TOPPADDING", (0, 0), (-1, -1), 3)])
    table.wrapOn(self.c, self.width, self.height)
    table.drawOn(self.c, *self.coord(.25, 2.75, inch))

    self.c.showPage()

    #Page Three
    side2_text = """<font size = '14'>This is where and how the main text will appear on the rear of this card.
    </font>"""
    p_side2 = Paragraph(side2_text, styleH)
    data = [[p_side2]]
    table_side2 = Table(data, colWidths=2.25*inch, rowHeights=2.55*inch)
    table_side2.setStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("TOPPADDING", (0, 0), (-1, -1), 3),
                    ("BOX", (0, 0), (-1,-1), 0.25, colors.red)])
    front_page = []
    front_page.append(table_side2)

    f = Frame(inch*.25, inch*.5, self.width-.5*inch, self.height-1*inch, showBoundary=1)
    f.addFromList(front_page, self.c)

def coord(self, x, y, unit=1):
    """
    Helper class to help position flowables in Canvas objects
    """
    x, y = x * unit, self.height -  y * unit
    return x, y

def savePDF(self):
    """"""
    self.c.save()

def fc_maker_view(request):
response = HttpResponse(content_type='application/pdf')
response['Content-Disposition'] = 'attachment; filename="pdf1.pdf"'
doc = fcMaker(response)
doc.createDocument()
doc.savePDF()
return response