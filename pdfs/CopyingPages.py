import PyPDF2
pdf1File=open('meetingminutes.pdf', 'rb')
pdf2File=open('meetingminutes.pdf', 'rb')
pdf1Reader=PyPDF2.PdfFileReader(pdf1File)
pdf2Reader=PyPDF2.PdfFileReader(pdf2File)
pdfWriter=PyPDF2.PdfFileWriter()
print(pdf1Reader.numPages, ' is pdf1Reader.numPages')
print(pdf2Reader.numPages, ' is pdf2Reader.numPages')
for pageNum in range(pdf1Reader.numPages):
    pageObj=pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj=pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
pdfOutputFile=open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()