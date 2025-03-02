from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import uuid
import os
from fastapi.responses import FileResponse

app = FastAPI()

# Directory to store LaTeX files temporarily
OUTPUT_DIR = "/workdir/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

class LatexRequest(BaseModel):
    latex_code: str

@app.post("/api/")
def compile_latex(request: LatexRequest):
    # Generate unique filename
    file_id = str(uuid.uuid4())
    tex_file = f"{OUTPUT_DIR}/{file_id}.tex"
    pdf_file = f"{OUTPUT_DIR}/{file_id}.pdf"

    # Write LaTeX content to a file
    with open(tex_file, "w") as f:
        f.write(request.latex_code)

    # Run pdflatex inside the container
    try:
        subprocess.run(["pdflatex", "-output-directory", OUTPUT_DIR, tex_file], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail="LaTeX compilation failed: " + e.stderr.decode())

    # Return the generated PDF
    if os.path.exists(pdf_file):
        return FileResponse(pdf_file, media_type="application/pdf", filename="output.pdf")
    else:
        raise HTTPException(status_code=500, detail="PDF generation failed.")

