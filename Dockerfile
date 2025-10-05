# Use the official Python base image
FROM python 

# Set working directory inside the container
WORKDIR /myapp

# Copy your application file(s) into the container
COPY ./myapp.py .

# Command to run your app
CMD ["python", "myapp.py"]
