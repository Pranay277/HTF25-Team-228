# Use an official Python runtime
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file and install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy your entire 'app' folder into the container
COPY ./app /code/app

# Tell the container what command to run
# Note: We use 0.0.0.0 to listen on all network interfaces
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]