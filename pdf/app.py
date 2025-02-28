from flask import Flask, request, send_file
from fpdf import FPDF
import os

app = Flask(__name__)

# Generate a fixed PDF file
def generate_pdf():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Hello, this is a fixed PDF!", ln=True, align="C")
    pdf.cell(200, 10, txt="This PDF is returned as a response to any POST request.", ln=True, align="C")
    
    pdf_path = "fixed_response.pdf"
    pdf.output(pdf_path)
    return pdf_path

@app.route('/pdf/', methods=['POST'])
def send_pdf():
    pdf_path = generate_pdf()
    return send_file(pdf_path, as_attachment=True, mimetype="application/pdf")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)

