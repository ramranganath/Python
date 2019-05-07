from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table
import os.path
import xlrd

wb = xlrd.open_workbook(os.path.join('C:\\Users\\Ramesh\\Desktop', 'testProj.xlsx'))
wb.sheet_names()
sh = wb.sheet_by_index(1)
i = 2

#nam = sh.cell(i,1).value

while sh.cell(i,1).value != 0:
   Load = sh.cell(i,3).value
   D1 = sh.cell(i,1).value
   D2 = sh.cell(i,2).value
   D3 = sh.cell(i,0).value
   D4 = sh.cell(i,4).value
   D5 = sh.cell(i,5).value
   D6 = sh.cell(i,6).value

   DB2 =str(D3)+"_"+str(D1)+"_"+str(D5)
   
   DB1 ="To :"+ str(Load) + " \n " + str(D3) + "  " + str(D1) + " \n bearing measurement of " + str(D2)+ " Sqft, made payment of Rs.  " + str(D4)+ " For the Month of  " + str(D5)+ " Year  " + str(D6)

   c = canvas.Canvas("receipt" +DB2+ ".pdf")
   c.drawString(10, 100, "Supreme Owners W Assocoation")
   c.drawString(15, 150, "Kengeri, Bangalore-60")
 #  c.createParagraph(DB1, 20, voffset+35)
 #  p = Paragraph(ptext, self.styles["Normal"])
 #  p.wrapOn(self.c, self.width-70, self.height)
 #  p.drawOn(self.c, *self.coord(20, voffset+48, mm))
   c.drawString(20, 200, " "+DB1)
   i = i + 1
   c.save()
