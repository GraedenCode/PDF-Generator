from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')

topics = []
pages = []

for i, row in df.iterrows():
    topics.append(row['Topic'])
    pages.append(row['Pages'])

pdf = FPDF(orientation="portrait", format='A4', unit='mm')

pdf.set_font(family="Times", style='B', size=12)

y = 20
# page width is 210 height is 297

for i, topic in enumerate(topics):
    y = 20
    page_count = pages[i]
    print(page_count)
    pdf.add_page()

    # Writes Title of topics and Line
    pdf.cell(txt=topic.title(), w=0, h=12, align='L', ln=69, border=2)
    pdf.set_line_width(1)
    pdf.line(10,20,200,20)

    # Prints Footer
    pdf.set_font(family="Times", style='B', size=12)
    pdf.set_text_color(100,100,100)
    pdf.text(180, 280, topic)

    # Resets Font
    pdf.set_font(family="Times", style='B', size=12)
    pdf.set_text_color(0,0,0)

    # prints lines
    for x in range(25):
        y = y + 10
        pdf.set_line_width(.3)
        pdf.line(10, y, 200, y)

    # prints additional pages
    y = 5
    if page_count > 1:
        for x in range(page_count - 1):
            pdf.add_page()
            for x in range(27):
                y = y + 10
                pdf.set_line_width(.3)
                pdf.line(10, y, 200, y)
        pdf.text(190, 290, topic)

pdf.output('output.pdf')
