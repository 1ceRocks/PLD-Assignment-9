import os as access
from fpdf import FPDF

# I used the FPDF module (PDF File Library - PyPDF) imported on Python to generate my own Personal Resume.
"""
 I've also updated my Python Version from 3.10 to 3.10.1;
    and the PIP Install Package used for External Modules from 22.0.1 to 22.0.3;
        for full availability and compatibility of the program to run with less hassle and supplement unerrors.
"""

full_Nm = 'FRITZ CEDRICK V. VILLARIZA' # Nm = Name
fcvRSM = 'VILLARIZA_FRITZCEDRICK.pdf' # FCV = Fritz Cedrick Villariza, RSM = ReSuMe
subH_Chr = 'My Personal Resume' # H = Header, Chr = Character
jsonPD = "personalDetails.json" # PD = Personal Details

class PDF(FPDF):
    """
    PDF HEADER SETTINGS
    """
    def header(self):
        self.image('PLD_HEADER.png', 5, 10, 50, 0) # Located on the top-left corner on the PDF File Format
        self.image('2x2_PICTURE.png', 160, 10, 40, 0) # The frame image of myself (Top-right).
        self.set_font('times', 'B', 20) # The font present within a specified character string.
        self.cell(180, 35, full_Nm, ln = 1, align = 'C'); # Character String Format.
        self.cell(90, 20, subH_Chr) # Character String Format.
        self.ln(10) # Page break is set to 10 millimeters.

    """
    PDF FOOTER SETTINGS
    """
    def footer(self):
        self.set_y(-9) # Y-axis at negative 9 to implement a right amount of space below the width of an imported image. 
        self.image('PLD_FOOTER.png', 10, 340, 200, 0)

    """
    PDF JSON-SOURCE FILE SETTINGS
    """
    def json_body(self, name):
        with open(jsonPD) as obj: # obj = Object
            chr = obj.read() # chr = Character
        self.set_font("times", "B", 10) # Times New Roman, Bold Font
        self.multi_cell(0, 5, chr)

    """
    PDF PAGE SETTINGS
    """
    def chapterOpt(self, num, title, name): # Opt = Output
        self.add_page()
        self.json_body(name)

"""
Generate a formal PDF File using Python.
"""
villapdf = PDF('P', 'mm', 'Legal') # villa = Villariza, a short abbreviation of my last name followed by PDF on the global variable.
villapdf.set_auto_page_break(margin = 0.5, auto = True) # Sets a page break + margin between the character string for the PDF File.
villapdf.chapterOpt(1, "", jsonPD)

# Saves the PDF aligned with the program code to execute and connect between the PDF File.
villapdf.output(fcvRSM)

# Opens the file with a preset browser settled as default on the Microsoft properties.
