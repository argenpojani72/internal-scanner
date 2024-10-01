FROM kalilinux/kali-rolling

# Install necessary packages
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Set the working directory
WORKDIR /sandbox

# Copy the project files
COPY . .

# Create a virtual environment and install dependencies
RUN python3 -m venv venv && \
    /sandbox/venv/bin/pip install --upgrade pip && \
    /sandbox/venv/bin/pip install -r requirements.txt

# Set the command to run your project
CMD ["/sandbox/venv/bin/python", "run_sandbox_test.py"]
