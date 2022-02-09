# Assignment 9

# PDF Resume Creator
# 	- Create a python program that will create your personal resume in PDF format
# 	- All personal details are stored in a JSON file
# 	- Your program should read the JSON file and write the details in the PDF
# 	- The output file should be: LASTNAME_FIRSTNAME.pdf

# Note:
# 	- Search for available PDF library that you can use
# 	- Search how data is structured using JSON format
# 	- Search how to read JSON file
# 	- You will create the JSON file manually
# 	- Your code should be in github before Feb12

import os as access; from fpdf import FPDF; import json

# Import OS as to interact with the Microsoft Windows default settings.
# I used the FPDF module (PDF File Library - PyPDF) imported on Python to generate my own Personal Resume.
# Import JSON Source File to supplement the data needed inside the dictionary language.
"""
 I've also updated my Python Version from 3.10 to 3.10.1;
    and the PIP Install Package used for External Modules from 22.0.1 to 22.0.3;
        for full availability and compatibility of the program to run with less hassle and supplement unerrors.
"""

"""
IMPORTANT VARIABLES TO BE USED FOR PDF LAYOUT EXECUTION
"""
full_hDr = 'MY PERSONAL RESUME' # hDr = HeaDer
YrandSec = 'BSCOE 1-6' # Yr = Year, Sec = Section
fcvRSM = 'VILLARIZA_FRITZCEDRICK.pdf' # FCV = Fritz Cedrick Villariza, RSM = ReSuMe

# H = Header, Chr = Character
subH_Chr = 'Personal Information'
subH_Chr2 = 'Contact Information'
subH_Chr3 = 'Academic Background'
subH_Chr4 = 'Honorable Achievements'
subH_Chr5 = 'Skills and Experience'
subH_Chr6 = 'Identity Reference'

jsonPD = "personalDetails.json" # PD = Personal Details

"""
INITIATE THE PDF FILE AND OPEN THE JSON-SOURCE PROGRAM
"""
villapdf = FPDF('P', 'mm', 'Legal') # villa = Villariza, a short abbreviation of my last name followed by PDF on the global variable.
with open(jsonPD, "r") as obj: # obj = Object
    charac = json.loads(obj.read()) # charac = Character
villapdf.add_page() # Adds a new page within the PDF File.

"""
PDF HEADER SETTINGS
"""
def layout_design(villapdf):
    villapdf.image('PLD_HEADER.png', 5, 10, 50, 0) # Located on the top-left corner on the PDF File Format
    villapdf.image('2x2_PICTURE.png', 165, 10, 40, 0) # The frame image of myvillapdf (Top-right).
    villapdf.image('PROGRESS_BAR.png', 112, 248, 64.5, 0)
    villapdf.set_font('helvetica', 'B', 27) # The font present within a specified character string.
    villapdf.set_text_color(0, 0, 200) # RGB =  Blue Shade.
    villapdf.cell(180, 35, full_hDr, ln = 1, align = 'C'); # Character String Format.
    villapdf.set_font('arial', 'B', 27)
    villapdf.set_text_color(255, 165, 0) # RGB = Yellow SHade.
    villapdf.cell(180, -10, YrandSec, ln = 0, align = 'C');
    villapdf.set_text_color(0, 0, 0) # Sets the text color by default = Black Shade.

"""
PDF JSON-SOURCE FILE SETTINGS
"""
def json_1stbody(villapdf): # PERSONAL INFORMATION
    villapdf.ln(10) # Line break is set to 10 millimeters.
    villapdf.cell(90, 10, subH_Chr) # Character String Format.
    villapdf.ln(10) # Line break is set to 10 millimeters.
    villapdf.set_font("times", "B", 11) # Times New Roman, Bold Font
    villapdf.cell(40, 6, "Full Name          :  " + str(charac["primaryElements"][0]["Full Name"]), ln = 10)
    villapdf.cell(40, 6, "Sex / Gender      :  " + str(charac["primaryElements"][0]["Sex / Gender"]), ln = 10)
    villapdf.cell(40, 6, "Age                     :  " + str(charac["primaryElements"][0]["Age"]), ln = 10)
    villapdf.cell(40, 6, "Home Address   :  " + str(charac["primaryElements"][0]["Home Address"]), ln = 10)
    villapdf.cell(40, 6, "Height                :  " + str(charac["primaryElements"][0]["Height"]), ln = 10)
    villapdf.cell(40, 6, "Weight               :  " + str(charac["primaryElements"][0]["Weight"]), ln = 10)
    villapdf.ln(15) # Line break is set to 15 millimeters.

def json_2ndbody(villapdf): # CONTACT INFORMATION
    villapdf.set_font("helvetica", "B", 20) # The font present within a specified character string.
    villapdf.cell(90, 0, subH_Chr2) # Character String Format.
    villapdf.ln(5) # Line break is set to 5 millimeters.
    villapdf.set_font("times", "B", 11) # The font present within a specified character string.
    villapdf.cell(40, 6, "Electronic Mail           :  " + str(charac["contactInformation"][0]["Electronic Mail"]), ln = 10)
    villapdf.cell(40, 6, "Smartphone Number :  " + str(charac["contactInformation"][0]["Smartphone Number"]), ln = 10)
    villapdf.cell(40, 6, "Landline Number       :  " + str(charac["contactInformation"][0]["Landline Number"]), ln = 10)
    villapdf.ln(15) # Line break is set to 15 millimeters.

def json_3rdbody(villapdf): # ACADEMIC BACKGROUND
    villapdf.set_font("helvetica", "B", 20) # The font present within a specified character string.
    villapdf.cell(90, 0, subH_Chr3) # Character String Format.
    villapdf.ln(5) # Line break is set to 5 millimeters.
    villapdf.set_font("times", "B", 11) # The font present within a specified character string.
    villapdf.cell(40, 6, "Elementary (1st to 6th Grade)                   :  " + str(charac["academicBackground"][0]["Elementary"]), ln = 10)
    villapdf.cell(40, 6, "Middle School (1st to 4th Year)                 :  " + str(charac["academicBackground"][0]["Middle School"]), ln = 10)
    villapdf.cell(40, 6, "Senior High School (11th to 12th Grade)  :  " + str(charac["academicBackground"][0]["Senior High School"]), ln = 10)
    villapdf.cell(40, 6, "University or College (RECENT)              :  " + str(charac["academicBackground"][0]["College"]), ln = 10)
    villapdf.ln(15) # Line break is set to 15 millimeters.

def json_4thbody(villapdf): # HONORABLE ACHIEVEMENTS
    villapdf.set_font("helvetica", "B", 20) # The font present within a specified character string.
    villapdf.cell(90, 0, subH_Chr4) # Character String Format.
    villapdf.ln(5) # Line break is set to 5 millimeters.
    villapdf.set_font("times", "B", 11) # The font present within a specified character string.
    villapdf.cell(40, 6, "A.  " + str(charac["honorableAchievement/s"][0]), align = '')
    villapdf.cell(120, 6, "B.  " + str(charac["honorableAchievement/s"][1]), ln = 10, align = 'C')
    villapdf.ln(0) # Line break is set to 0 millimeters.
    villapdf.cell(40, 6, "C.  " + str(charac["honorableAchievement/s"][2]), align = '')
    villapdf.cell(150, 6, "D.  " + str(charac["honorableAchievement/s"][3]), ln = 10, align = 'C')
    villapdf.ln(0) # Line break is set to 0 millimeters.
    villapdf.cell(40, 6, "E.  " + str(charac["honorableAchievement/s"][4]), align = '')
    villapdf.cell(147, 6, "F.  " + str(charac["honorableAchievement/s"][5]), ln = 10, align = 'C')
    villapdf.ln(0) # Line break is set to 0 millimeters.
    villapdf.cell(40, 6, "G.  " + str(charac["honorableAchievement/s"][6]), align = '')
    villapdf.cell(143, 6, "H.  " + str(charac["honorableAchievement/s"][7]), ln = 10, align = 'C')
    villapdf.ln(15) # Line break is set to 15 millimeters.

def json_5thbody(villapdf): # SKILLS AND EXPERIENCES
    villapdf.set_font("helvetica", "B", 20) # The font present within a specified character string.
    villapdf.cell(90, 0, subH_Chr5) # Character String Format.
    villapdf.ln(5) # Line break is set to 5 millimeters.
    villapdf.set_font("times", "B", 11) # The font present within a specified character string.
    villapdf.cell(40, 6, "1. Microsoft Office              :  " + str(charac["personalExperience"][0]["Microsoft Office"]), ln = 10)
    villapdf.cell(40, 6, "2. Organizing System Unit :  " + str(charac["personalExperience"][0]["Organizing System Unit"]), ln = 10)
    villapdf.cell(40, 6, "3. Music                                :  " + str(charac["personalExperience"][0]["Music"]), ln = 10)
    villapdf.cell(40, 6, "4. E-Sports                           :  " + str(charac["personalExperience"][0]["E-Sports"]), ln = 10)
    villapdf.ln(15) # Line break is set to 15 millimeters.

def json_6thbody(villapdf): # IDENTITY REFERENCE
    villapdf.set_font("helvetica", "B", 20) # The font present within a specified character string.
    villapdf.cell(90, 0, subH_Chr6) # Character String Format.
    villapdf.ln(5) # Line break is set to 5 millimeters.
    villapdf.set_font("times", "B", 11) # The font present within a specified character string.
    villapdf.cell(40, 6, "" + str(charac["identityReference"][0]), ln = 10)
    villapdf.cell(40, 6, "" + str(charac["identityReference"][1]), ln = 10)
    villapdf.cell(40, 6, "" + str(charac["identityReference"][2]), ln = 10)
    villapdf.cell(40, 6, "" + str(charac["identityReference"][3]), ln = 10)
    villapdf.cell(40, 6, "" + str(charac["identityReference"][4]), ln = 10)
    villapdf.ln(15) # Line break is set to 15 millimeters.

"""
PDF FOOTER SETTINGS
"""
def footer(villapdf):
    villapdf.set_y(-9) # Y-axis at negative 9 to implement a right amount of space below the width of an imported image. 
    villapdf.image('PLD_FOOTER.png', 10, 340, 200, 0) # Import the Footer PNG located right below the PDF File.

"""
PDF LAYOUT EXECUTION SETTINGS
"""
def generatePDF():
    layout_design(villapdf) # 1ST LAYOUT
    json_1stbody(villapdf) # 2ND LAYOUT
    json_2ndbody(villapdf) # 3RD LAYOUT
    json_3rdbody(villapdf) # 4TH LAYOUT
    json_4thbody(villapdf) # 5TH LAYOUT
    json_5thbody(villapdf) # 6TH LAYOUT
    json_6thbody(villapdf) # 7TH LAYOUT
    footer(villapdf) # 8TH LAYOUT
    
#Run the PDF Generator
generatePDF()

# Sets a page break + margin between the character string for the PDF File.
villapdf.set_auto_page_break(margin = 0.5, auto = True) 

# Saves the PDF aligned with the program code to execute and connect between the PDF File.
villapdf.output(fcvRSM)

# Opens the file with a preset browser settled as default on the Microsoft properties.
access.startfile(fcvRSM)