
from pypdf import PdfReader, PdfWriter

data = [
	[1, '06-07-2023 10:30', 'name1', '100% geprüft'],
	[2, '06-07-2023 10:35', 'name2', '100% geprüft'],
	[3, '06-07-2023 10:40', 'name3', '100% geprüft'],
	[4, '06-07-2023 10:45', 'name4', '100% geprüft'],
]

reader = PdfReader("form.pdf")
writer = PdfWriter()

'''
def a3(reader, writer, Stueckzahl, Datum, Name, Bemerkung):

	writer.append_pages_from_reader(reader)

	writer.update_page_form_field_values(
	    writer.pages[0], {"Stueckzahl": Stueckzahl}
	)
	writer.update_page_form_field_values(
	    writer.pages[0], {"Datum": Datum}
	)
	writer.update_page_form_field_values(
	    writer.pages[0], {"Name": Name}
	)
	writer.update_page_form_field_values(
	    writer.pages[0], {"Bemerkung": Bemerkung}
	)

	# write "output" to PyPDF2-output.pdf
	with open("filled-out.pdf", "wb") as output_stream:
		writer.write(output_stream)
'''

for Stueckzahl, Datum, Name, Bemerkung in data[0:3]:
	print(Stueckzahl, Datum, Name, Bemerkung)
data = data[3:]
for Stueckzahl, Datum, Name, Bemerkung in data[0:3]:
	print(Stueckzahl, Datum, Name, Bemerkung)