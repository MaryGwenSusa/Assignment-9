import os as access; from fpdf import FPDF; import json

# import OS to interact with the Microsoft Windows default settings
# fpdf module to generate pdf


data = open("resume.json")
data = json.load(data) # read the json file
susaPDF = FPDF('P', 'mm', 'Legal') # orientation, measure, size of page; set up the pdf
susaPDF.add_page()