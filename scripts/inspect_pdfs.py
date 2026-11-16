import pymupdf
from src import config

def show_outline(path):
    with pymupdf.open(path) as doc:
        print(path.name, len(doc), " pages")
        toc = doc.get_toc()

        if not toc:
            print("No bookmarks")
            return

        print(len(toc), " entries:")
        for level, title, page in toc[:30]:
            print("  "*level, title, " p. ", page)

def show_fonts(path, page_number):
    """
    Inspect one page
    """
    with pymupdf.open(path) as doc:
        print(path.name, len(doc), " pages")

        data = doc[page_number - 1].get_text("dict", flags = 11)["blocks"]
        for b in data:
            for l in b["lines"]:
                for s in l["spans"]:
                    txt = s["text"].strip()
                    if not txt:
                        continue
                    if s["flags"] & 16:
                        bold = "bold"
                    else:
                        bold = "-"
                    size = round(s["size"], 1)
                    print(f"{size:>5}, {bold:<4}, {txt[:30]}")





if __name__ == "__main__":
    #for path in config.RAW_DIR.glob("*.pdf"):
    #   show_outline(path)
    #   print("-"*60)

    show_fonts(config.RAW_DIR/"student_handbook_2025_26.pdf", 13)