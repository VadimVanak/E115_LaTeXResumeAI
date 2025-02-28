from flask import Flask, request, send_file, jsonify
import os
import uuid
import docker
import logging
import json

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    filename='/var/log/flask_app.log',  # Change path if needed
    level=logging.DEBUG,  # Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Directories
TEX_DIR = "/var/lib/overleaf"

# Initialize Docker client
client = docker.from_env()
logging.info("client created")

def get_unique_filename():
    """Generate a unique filename that does not exist in /var/lib/overleaf"""
    while True:
        filename = f"{uuid.uuid4()}.tex"
        tex_path = os.path.join(TEX_DIR, filename)
        if not os.path.exists(tex_path):
            return filename, tex_path

@app.route('/pdf/', methods=['POST'])
def process_latex():
    try:
        # Get LaTeX content from POST request
        latex_inp = request.data.decode("utf-8")
        latex_content = json.loads(latex_inp)["latex"]
        logging.info(f"inp={latex_content}")
        if not latex_content.strip():
            return jsonify({"error": "Empty LaTeX content"}), 400

        # Get unique filename and save the .tex file
        tex_filename, tex_path = get_unique_filename()
        logging.info(f"tex_file = {tex_path}")
        with open(tex_path, "w") as tex_file:
            tex_file.write(latex_content)

        # Define output PDF file paths
        pdf_filename = tex_filename.replace(".tex", ".pdf")
        pdf_output_path = os.path.join(TEX_DIR, pdf_filename)
        logging.info(f"pdf_path={pdf_output_path}")

        container = client.containers.get("sharelatex")
        logging.info("got container")
        #cmd=f"pdflatex {tex_path} && cp {pdf_output_path} {TEX_DIR}"
        cmd=f"pdflatex {tex_path}"
        logging.info(cmd)
        container.exec_run(cmd)

        cmd=f"cp /overleaf/{pdf_filename} {TEX_DIR}"
        logging.info(cmd)
        container.exec_run(cmd)

        # Check if PDF was generated
        if not os.path.exists(pdf_output_path):
            return jsonify({"error": "PDF generation failed"}), 500

        # Return the generated PDF
        return send_file(pdf_output_path, as_attachment=True, mimetype="application/pdf")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    logging.info("logging started")
    app.run(host='0.0.0.0', port=4000, debug=True)

