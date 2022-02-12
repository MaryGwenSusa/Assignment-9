import os as access; from fpdf import FPDF; import json
# import OS to interact with the Microsoft Windows default settings
# fpdf module to generate pdf

data = open("resume.json")
data = json.load(data) # read the json file
susaPDF = FPDF('P', 'mm', 'Legal') # orientation, measure, size of page; set up the pdf
susaPDF.add_page()

def layout():
    susaPDF.image('2by2.jpg', 165, 10, 40, 0)  #space and dimensions   

def jsonPart(): 
    susaPDF.set_font("times", "B", 30) #font type, size, etc.
    susaPDF.cell(100, 20, str(data["mainInfo"][0]["name"]), ln = 1, align = 'L')

    susaPDF.set_font("helvetica", "B", 12)
    susaPDF.cell(200, 6, str(data["mainInfo"][0]["address"]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["mainInfo"][0]["email"]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["mainInfo"][0]["phone"]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["mainInfo"][0]["website"]), ln = 1, align = 'L')

    susaPDF.set_text_color(16, 78, 139)
    susaPDF.cell(200, 6, str(data["mainInfo"][0]["network"]), ln = 1, align = 'L')

    susaPDF.set_text_color(5, 5, 5)
    susaPDF.cell(200, 6, str(data["mainInfo"][0]["username"]), ln = 1, align = 'L')
    susaPDF.ln(5)

    susaPDF.set_text_color(240, 255, 240)
    susaPDF.set_fill_color(139, 58, 98)
    susaPDF.cell(200, 6, "Skills", ln = 1, align = 'L', fill = 1)
    
    susaPDF.set_font("helvetica", "", 12)
    susaPDF.set_text_color(5, 5, 5)
    susaPDF.cell(200, 6, str(data["skills"][0]["keywords"]), ln = 1, align = 'L')
    susaPDF.ln(7)

    susaPDF.set_font("helvetica", "B", 12)
    susaPDF.set_text_color(240, 255, 240)
    susaPDF.set_fill_color(139, 58, 98)
    susaPDF.cell(200, 6, "Experience", ln = 1, align = 'L', fill = 1)
    
    susaPDF.set_text_color(5, 5, 5)
    susaPDF.set_font("courier", "B", 16)
    susaPDF.cell(200, 6, str(data["work"][0]["company"]), ln = 1, align = 'L')

    susaPDF.set_font("courier", "I", 16)
    susaPDF.cell(200, 6, str(data["work"][0]["position"]), ln = 1, align = 'L')

    susaPDF.set_font("helvetica", "", 12)
    susaPDF.cell(200, 6, str(data["work"][0]["startDate"]) + '-' + str(data["work"][0]["endDate"]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work"][0]["highlights"][0]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work"][0]["highlights"][1]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work"][0]["highlights"][2]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work"][0]["highlights"][3]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work"][0]["highlights"][4]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work"][0]["highlights"][5]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work"][0]["highlights"][6]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work"][0]["highlights"][7]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work"][0]["highlights"][8]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work"][0]["highlights"][9]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work"][0]["highlights"][10]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work"][0]["highlights"][11]), ln = 1, align = 'L')
    susaPDF.ln(10)

    susaPDF.set_font("courier", "B", 16)
    susaPDF.cell(200, 6, str(data["work2"][0]["company"]), ln = 1, align = 'L')

    susaPDF.set_font("helvetica", "", 12)
    susaPDF.cell(200, 6, str(data["work2"][0]["highlights"][0]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work2"][0]["highlights"][1]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work2"][0]["highlights"][2]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work2"][0]["highlights"][3]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work2"][0]["highlights"][4]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work2"][0]["highlights"][5]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work2"][0]["highlights"][6]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work2"][0]["highlights"][7]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work2"][0]["highlights"][8]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work2"][0]["highlights"][9]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work2"][0]["highlights"][10]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work2"][0]["highlights"][11]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["work2"][0]["highlights"][12]), ln = 1, align = 'L')
    susaPDF.ln(7)
    
    susaPDF.set_font("helvetica", "B", 12)
    susaPDF.set_text_color(240, 255, 240)
    susaPDF.set_fill_color(139, 58, 98)
    susaPDF.cell(200, 6, "Objective", ln = 1, align = 'L', fill = 1)
    
    susaPDF.set_text_color(5, 5, 5)
    susaPDF.set_font("helvetica", "", 12)
    susaPDF.cell(200, 6, str(data["summary"][0]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["summary"][1]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["summary"][2]), ln = 1, align = 'L')
    susaPDF.cell(200, 6, str(data["summary"][3]), ln = 1, align = 'L')


layout() 
jsonPart()
# saves the coded pdf with the help of the module
susaPDF.output('SUSA_MARY GWEN.pdf')
# opens the file with a preset browser settled as default on the Microsoft properties
access.startfile('SUSA_MARY GWEN.pdf')