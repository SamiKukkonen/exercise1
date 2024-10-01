# Use the official Node.js 16 image as the base image
FROM node:16-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install necessary system utilities
RUN apt-get update && apt-get install -y procps

# Copy the package.json
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Expose port 3000
EXPOSE 3000

# Command to run the application
CMD ["node", "app.js"]

