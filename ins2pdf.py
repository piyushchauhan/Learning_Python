import pdfkit, pyperclip, os

os.chdir('C:\\Users\\Piyush\\Downloads')
pdfkit.from_url(pyperclip.paste(), input('Enter the name of the pdf file') + '.pdf')
