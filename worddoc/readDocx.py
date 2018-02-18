#! python3

import docx, os

os.chdir('C:\\MyPythonScripts\\worddoc')


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


print(getText('multipleParagraphs.docx'))
