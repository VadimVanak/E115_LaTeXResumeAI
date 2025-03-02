from fastapi.responses import PlainTextResponse
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import uuid
import os
from fastapi.responses import FileResponse

app = FastAPI()

fixed_response = r"""
\documentclass[a4paper,10pt]{article}

\usepackage{geometry}
\geometry{margin=1in}

\usepackage{graphicx}

\begin{document}

\title{\textbf{John Doe's CV}}
\author{}
\date{}

\maketitle

\section*{Personal Information}
\begin{tabular}{rl}
    Name: & John Doe \\
    Email: & john.doe@example.com \\
    Phone: & +1 234 567 8901 \\
\end{tabular}

\section*{Education}
\textbf{Master of Science in Computer Science}, University XYZ (2020 - 2022)

\section*{Work Experience}
\textbf{Software Engineer}, TechCorp (2022 - Present) \\
- Developed web applications using Python and JavaScript. \\
- Optimized database queries, reducing response time by 30\%.

\section*{Skills}
- Programming: Python, C++, Java \\
- Databases: MySQL, PostgreSQL \\
- Tools: Git, Docker, Linux

\end{document}
"""

class BuildRequest(BaseModel):
    input_text: str
    latex_code: str


class EditRequest(BaseModel):
    command: str
    latex_code: str

@app.post("/ai/build")
async def return_fixed_response(request: BuildRequest):
    return PlainTextResponse(fixed_response, media_type="text/plain")

@app.post("/ai/command")
async def return_fixed_response(request: EditRequest):
    return PlainTextResponse(fixed_response, media_type="text/plain")
