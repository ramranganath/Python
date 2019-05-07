from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table

import os.path
import xlrd

wb = xlrd.open_workbook(os.path.join('C:\\Users\\Ramesh\\Desktop', 'testProj.xlsx'))
wb.sheet_names()
sh = wb.sheet_by_index(2)
i = 2
x=4
h1 = sh.cell(0,4).value
h2 = sh.cell(1,4).value
h3 = sh.cell(1,5).value
h4 = sh.cell(1,6).value

DB3= str(h2)+ "    "+str(h3)+"     "+str(h4)
#x += 1


while sh.cell(i,1).value != 0:
   Load = sh.cell(i,3).value
   D1 = sh.cell(i,1).value
   D2 = sh.cell(i,2).value
   D3 = sh.cell(i,0).value
   D4 = sh.cell(i,4).value
   D5 = sh.cell(i,5).value
   D6 = sh.cell(i,6).value

   Da2 =str(D3)+"_"+str(D1)
   
   DB1 ="To :"+ str(Load) + "  " 
   DBa = str(D3) + "  " + str(D1)
   DB2= " bearing measurement of " + str(D2)+ " Sqft, made payment"
   DB2a=" as below for Year "+str(h1)
   
   DB4= str(D4)+"  "+str(D5)+ "  "+str(D6)

   c = canvas.Canvas("receipt" +Da2+ ".pdf")
   c.drawImage('logo.png', 15, 740)
   c.setFontSize(40)
   c.drawString(30, 700, "Supreme Appartment Owners Welfare Assocoation")
   c.setFontSize(20)
   c.drawString(80, 680, "Kengeri, Bangalore-60")
 #  c.createParagraph(DB1, 20, voffset+35)
 #  p = Paragraph(ptext, self.styles["Normal"])
 #  p.wrapOn(self.c, self.width-70, self.height)
 #  p.drawOn(self.c, *self.coord(20, voffset+48, mm))
   c.drawString(20, 640, " "+DB1)
   c.drawString(25, 620, " "+DBa)
   c.drawString(20, 600, " "+DB2)
   c.drawString(20, 600, " "+DB2a)
   c.setFontSize(20)
   c.drawString(40, 580, " "+DB3)
   c.setFontSize(16)
   c.drawString(40, 560, " "+DB4)
#    t = Table(DB3)
#       table.column_headers(DB3)
#       	table.append_row(DB4)
#       	c.drawString(20, 550, " " +table)




    
   
   i = i + 1
   c.save()
