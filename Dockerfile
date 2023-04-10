# Base image for the Docker container.
FROM python:3.10-slim-buster

# Set the working directory for the container.
WORKDIR /app

#Copy the "requirements.txt" file from the Flask project into the container.
COPY requirements.txt /app

# Install the dependencies listed in the "requirements.txt" file.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Flask project into the container.
COPY . /app

# Expose the port that the Flask application is running on.
EXPOSE 5000

# Start the Flask application.
CMD ["flask", "--debug", "run", "--host=0.0.0.0"]
