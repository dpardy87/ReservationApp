# use official python image
FROM python:3.11

# set working dir in container
WORKDIR /app

# copy current dir to /app
COPY . /app

# install deps
RUN pip install --no-cache-dir -r requirements.txt
