FROM texlive/texlive

# Install necessary dependencies
RUN apt-get update && apt-get install -y python3 python3-venv python3-pip

# Create a virtual environment
RUN python3 -m venv /venv

# Activate the virtual environment and install dependencies
RUN /venv/bin/pip install --no-cache-dir fastapi uvicorn pydantic

# Set the virtual environment as default
ENV PATH="/venv/bin:$PATH"

# Set working directory
WORKDIR /workdir

# Copy API files
COPY ./app.py ./requirements.txt /workdir/
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port
EXPOSE 4001

# Run FastAPI server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "4001", "--log-level", "debug"]

