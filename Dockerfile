FROM python:3.12.0-slim

# Install OS dependencies
RUN apt-get update && apt-get install -qq -y \
    git gcc build-essential libpq-dev --fix-missing --no-install-recommends \ 
    && apt-get clean

# Make sure we are using latest pip
RUN pip install --upgrade pip

# Set the working directory in the container to /app
WORKDIR /user/app

# Create directory for dbt config
RUN mkdir -p /root/.kaggle

# Add the current directory contents into the container at /app
COPY ./requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Keep the container running
CMD ["tail", "-f", "/dev/null"]
