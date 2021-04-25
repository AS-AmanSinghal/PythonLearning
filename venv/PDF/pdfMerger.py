import PyPDF2

inputs = ['dummy.pdf','tilt.pdf','twopage.pdf']

def pdfMerger(pdfList):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdfList:
        print(pdf)
        merger.append(pdf)
    merger.write('merged.pdf')

pdfMerger(inputs)