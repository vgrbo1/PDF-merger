from PyPDF2 import PdfMerger
import sys
import datetime

merged = PdfMerger()

ok = True
for pdf in sys.argv[1:]:
    try:
        merged.append(pdf)
    except Exception:
        print("You have specified non-existent pdf: ", pdf)
        ok = False
        merged.close()

if(ok):
    merged.write("Merged-"+datetime.date.today().strftime("%d-%m-%Y")+".pdf")
    merged.close()
    print("Done")