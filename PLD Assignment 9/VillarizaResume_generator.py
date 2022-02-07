from fpdf import FPDF

header = 'FRITZ CEDRICK V. VILLARIZA'
header.center(50, ' ')

# I used the FPDF module (PDF File Library) imported on Python to generate my own Personal Resume.
"""
 I've also updated my Python Version from 3.10 to 3.10.1;
    and the PIP Install Package used for External Modules from 22.0.1 to 22.0.3;
        for full availability and compatibility of the program to run with less hassle and supplement unerrors.
"""

villaPDF = FPDF('P', 'mm', 'Letter'); # villa = Villariza, a short abbreviation of my last name followed by PDF on the global variable.

villaPDF.add_page() # Increment a blank page on the PDF File I will execute.

villaPDF.set_font('times', 'B', 24) # Sets the text font used to print character strings.

villaPDF.cell(70, 10, header) # Arranges the layout of my character string on a certain position on the PDF File.

villaPDF.output('VILLARIZA_FRITZCEDRICK.pdf') # Saves the PDF aligned with the program code to execute and connect between the PDF File.