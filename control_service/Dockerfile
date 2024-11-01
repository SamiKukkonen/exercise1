# control_service/Dockerfile
# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install Flask
RUN pip install flask

# Expose the port the app runs on
EXPOSE 3000

# Run the application
CMD ["python", "app.py"]
