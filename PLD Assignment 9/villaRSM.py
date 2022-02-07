from fpdf import FPDF

# I used the FPDF module (PDF File Library - PyPDF) imported on Python to generate my own Personal Resume.
"""
 I've also updated my Python Version from 3.10 to 3.10.1;
    and the PIP Install Package used for External Modules from 22.0.1 to 22.0.3;
        for full availability and compatibility of the program to run with less hassle and supplement unerrors.
"""

full_Nm = 'FRITZ CEDRICK V. VILLARIZA' # Nm = Name
fcvRSM = 'VILLARIZA_FRITZCEDRICK.pdf' # FCV = Fritz Cedrick Villariza, RSM = ReSuMe
subH_Chr = "My Personal Resume" # H = Header, Chr = Character

class PDF(FPDF):
    """
    PDF HEADER SETTINGS
    """
    def header(self):
        self.image('PLD_HEADER.png', 5, 10, 50, 0) # Located on the top-left corner on the PDF File Format
        self.image('2x2 FCV.png', 160, 10, 40, 0) # The frame image of myself (Top-right).
        self.set_font('times', 'B', 20) # The font present within a specified character string.
        self.cell(180, 25, full_Nm, ln = 1, align = 'C'); # Character String Format.
        self.cell(90, 40, subH_Chr) # Character String Format.
        self.ln(10) # Page break is set to 10 millimeters.

    """
    PDF FOOTER SETTINGS
    """
    def footer(self):
        self.set_y(-9) # Y-axis at negative 9 to implement a right amount of space below the width of an imported image. 
        self.image('PLD_FOOTER.png', 10, 260, 200, 0)

"""
Generate a formal PDF File using Python.
"""
villapdf = PDF('P', 'mm', 'Letter') # villa = Villariza, a short abbreviation of my last name followed by PDF on the global variable.
villapdf.set_fill_color(250, 250, 250) # Defines the color used for all filling operations. Can be expressed through a dynamic chart of RGB components.
villapdf.set_auto_page_break(margin = 12.7, auto = True) # Sets a page break + margin between the character string for the PDF File.

# Saves the PDF aligned with the program code to execute and connect between the PDF File.
villapdf.output(fcvRSM)
