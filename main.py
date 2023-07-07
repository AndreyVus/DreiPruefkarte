
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
vorlage = """<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="UTF-8">
	<title>Title</title>
	<style>
		body {
			font-size: 14pt;
		}

		div {
			position: absolute;
		}

		#a1 {
			top: 255px;
			left: 185px;
		}

		#a2 {
			top: 255px;
			left: 390px;
		}

		#a3 {
			top: 253px;
			left: 620px;
		}

		#a4 {
			top: 300px;
			left: 250px;
		}

		#b1 {
			top: 645px;
			left: 185px;
		}

		#b2 {
			top: 650px;
			left: 390px;
		}

		#b3 {
			top: 650px;
			left: 620px;
		}

		#b4 {
			top: 690px;
			left: 250px;
		}

		#c1 {
			top: 1035px;
			left: 185px;
		}

		#c2 {
			top: 1040px;
			left: 390px;
		}

		#c3 {
			top: 1045px;
			left: 620px;
		}

		#c4 {
			top: 1080px;
			left: 250px;
		}
		img {
			width: 826px; /*21cm;*/
			height: 1169px; /*29.7cm;*/
		}
	</style>
</head>
<body>
	<div id="a1">a1</div>
	<div id="a2">a2</div>
	<div id="a3">a3</div>
	<div id="a4">a4</div>
	<div id="b1">b1</div>
	<div id="b2">b2</div>
	<div id="b3">b3</div>
	<div id="b4">b4</div>
	<div id="c1">c1</div>
	<div id="c2">c2</div>
	<div id="c3">c3</div>
	<div id="c4">c4</div>
	<img alt="" src="form.png">
</body>
</html>"""

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