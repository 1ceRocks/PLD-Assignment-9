from fpdf import FPDF

header = 'FRITZ CEDRICK V. VILLARIZA'
sub_header = "My Personal Resume"

# I used the FPDF module (PDF File Library - PyPDF) imported on Python to generate my own Personal Resume.
"""
 I've also updated my Python Version from 3.10 to 3.10.1;
    and the PIP Install Package used for External Modules from 22.0.1 to 22.0.3;
        for full availability and compatibility of the program to run with less hassle and supplement unerrors.
"""

"""
Generate a formal PDF File using Python.
"""
villaPDF = FPDF('P', 'mm', 'Letter'); # villa = Villariza, a short abbreviation of my last name followed by PDF on the global variable.

"""
PDF INSERT SETTINGS
"""
villaPDF.add_page() # Increment a blank page on the PDF File I will execute.

"""
PDF LAYOUT SETTINGS
"""
villaPDF.set_font('times', 'B', 24) # Sets the text font used to print character strings.
villaPDF.set_margins(12.7, 12.7, 12.7) # Sets the whole margin for the PDF File.
villaPDF.set_fill_color(250, 250, 250) # Defines the color used for all filling operations. Can be expressed through a dynamic chart of RGB components.

"""
PDF Character (TEXT) String Settings
"""
 
villaPDF.cell(180, 10, header, border= True, ln=1);
villaPDF.cell(90, 40, sub_header)

# Saves the PDF aligned with the program code to execute and connect between the PDF File.
villaPDF.output('VILLARIZA_FRITZCEDRICK.pdf')