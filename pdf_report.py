from fpdf import FPDF
from Rejets_ligne_pdf import pareto_semaine,pareto_semaine_process



WIDTH = 210
HEIGHT = 297

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 25)
pdf.cell(0,0,f"Rejets ligne semaine 14",align='c')

pdf.image("C:\\Users\\Tomáš\\Pandas tutorial\\pdf_report\\graphS14.png",0,16,WIDTH/2,97)

pdf.image("C:\\Users\\Tomáš\\Pandas tutorial\\pdf_report\\\graph0.png",106,16,WIDTH/2,97)
pdf.image("C:\\Users\\Tomáš\\Pandas tutorial\\pdf_report\\graph1.png",0,108,WIDTH/2,97)
pdf.image("C:\\Users\\Tomáš\\Pandas tutorial\\pdf_report\\graph2.png",106,108,WIDTH/2,97)
pdf.image("C:\\Users\\Tomáš\\Pandas tutorial\\pdf_report\\graph3.png",0,200,WIDTH/2,97)
pdf.image("C:\\Users\\Tomáš\\Pandas tutorial\\pdf_report\\graph4.png",106,200,WIDTH/2,97)
pdf.output('tutorial1.pdf', 'F')