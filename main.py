
#from pypdf import PdfReader, PdfWriter
#from fillpdf import fillpdfs

data = [
	[1, '06-07-2023 10:30', 'name1', '100% geprüft'],
	[2, '06-07-2023 10:35', 'name2', '100% geprüft'],
	[3, '06-07-2023 10:40', 'name3', '100% geprüft'],
	[4, '06-07-2023 10:45', 'name4', '100% geprüft'],
]

# teilen data in 3er Gruppe
data123 = [data[i:i+3] for i in range(0, len(data), 3)]
# vorlage
#reader = PdfReader("form.pdf")
# ergebnis
#writer = PdfWriter()
# aktuelle Seitennummer
pageNum = 0
# füllen 3 Karten auf Seite aus
for card123 in data123:
	# add page
	#writer.append(reader)
	# card = dict(text1='', text2='', text3='', text4='',
	#             text5='', text6='', text7='', text8='',
	#             text9='', text10='', text11='', text12='')
	# Stueckzahl, Datum, Name, Bemerkung   * 3
	card = {}
	count = 1
	for row in card123:
		for item in row:
			key = f'text{count}'
			card[key] = item
			count += 1
	print(card)
	#writer.update_page_form_field_values(
	#	writer.pages[pageNum], card
	#)
	#fillpdfs.write_fillable_pdf('form.pdf', f'new{pageNum}.pdf', card)
	# next page
	pageNum += 1

# write "output" to pypdf-output.pdf
#with open("filled-out.pdf", "wb") as output_stream:
#    writer.write(output_stream)