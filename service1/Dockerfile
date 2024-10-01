# Use official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install necessary system utilities
RUN apt-get update && apt-get install -y procps

# Install the requests library
RUN pip install requests

# Copy the current directory contents into the container
COPY . .

# Install the Flask library
RUN pip install flask

# Make port 8199 available
EXPOSE 8199

# Run app.py when the container launches
CMD ["python", "app.py"]

