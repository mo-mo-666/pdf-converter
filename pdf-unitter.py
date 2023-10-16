from pypdf import PdfReader, PdfWriter

reader1 = PdfReader("pdf-unit/data/score.pdf")
reader2 = PdfReader("pdf-unit/data/sheet.pdf")
if len(reader1.pages) != len(reader2.pages):
    print('ページ数が異なります')
    quit()

# １ページずつ交互に新しいファイルに書き込む
writer = PdfWriter()
for i in range(len(reader1.pages)):
    writer.add_page(reader1.pages[i])
    writer.add_page(reader2.pages[i])
with open("pdf-unit/data/unit.pdf", 'wb') as f:
    writer.write(f)
