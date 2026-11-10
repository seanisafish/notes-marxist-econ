import sys, os
import pypdfium2 as pdfium

PDF = r"C:\Users\HUAWEI\.minimax\v2\assets\2026\11\01\20-15-21-199-asset_20261101-201521-199_78e33c28a14b_c743272d-马克思主义政治经济学概论(第二版) (《马克思主义政治经济学概论》编写组编) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
OUT = r"C:\Users\HUAWEI\.minimax-agent-cn\projects\marxist-econ\pages"
os.makedirs(OUT, exist_ok=True)

start = int(sys.argv[1]); end = int(sys.argv[2])
scale = float(sys.argv[3]) if len(sys.argv) > 3 else 2.0

doc = pdfium.PdfDocument(PDF)
print("total pages:", len(doc))
for i in range(start - 1, min(end, len(doc))):
    page = doc[i]
    bmp = page.render(scale=scale)
    img = bmp.to_pil()
    p = os.path.join(OUT, f"p{i+1:04d}.png")
    img.save(p)
    print(p, img.size)
