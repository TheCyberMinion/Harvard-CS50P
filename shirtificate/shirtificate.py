from fpdf import FPDF

class MakeHeader(FPDF):
    def header(self):
        self.image('shirtificate.png', 25, 80, 160)
        self.set_font("helvetica", style="B", size=40)
        self.cell(0, 57, "CS50 Shirtificate", border=0, align="C")
        self.ln(20)

def main():
    name = getName().strip()
    makeShirt(name)

def getName():
    return input('Name -> ')

def makeShirt(name):
    shirt = MakeHeader(orientation="P", unit="mm", format="A4")
    shirt.add_page()
    shirt.set_font("Helvetica", size=24)
    shirt.set_text_color(255,255,255)
    shirt.set_y(140)
    shirt.cell(0, 10, f'{name} took CS50', align="C")
    shirt.output('shirtificate.pdf')

if __name__ == "__main__":
    main()
