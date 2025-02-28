from flask import Flask

app = Flask(__name__)

fixed_response = """
\\documentclass[a4paper,10pt]{article}

\\usepackage{geometry}
\\geometry{margin=1in}

\\usepackage{graphicx}

\\begin{document}

\\title{\\textbf{John Doe's CV}}
\\author{}
\\date{}

\\maketitle

\\section*{Personal Information}
\\begin{tabular}{rl}
    Name: & John Doe \\\\
    Email: & john.doe@example.com \\\\
    Phone: & +1 234 567 8901 \\\\
\\end{tabular}

\section*{Education}
\\textbf{Master of Science in Computer Science}, University XYZ (2020 - 2022)

\\section*{Work Experience}
\\textbf{Software Engineer}, TechCorp (2022 - Present) \\\\
- Developed web applications using Python and JavaScript. \\\\
- Optimized database queries, reducing response time by 30\%.

\\section*{Skills}
- Programming: Python, C++, Java \\\\
- Databases: MySQL, PostgreSQL \\\\
- Tools: Git, Docker, Linux

\\end{document}

"""


# Handle any request with a fixed response
@app.route(
    "/",
    defaults={"path": ""},
    methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
)
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def return_fixed_response(path):
    return fixed_response


# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

