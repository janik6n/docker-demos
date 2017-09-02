FROM python:3.6.2-stretch
# Using the official Python image https://hub.docker.com/_/python/

LABEL maintainer="janikarh@gmail.com"

# Install Voikko packages 
RUN DEBIAN_FRONTEND=noninteractive \
	&& apt-get update \
	&& apt-get install -y voikko-fi python-libvoikko

WORKDIR /usr/src/app

# Copy libvoikko.py to app directory from install dir to make it available for the app.
RUN cp /lib/python3/dist-packages/libvoikko.py /usr/src/app/libvoikko.py

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./

ENTRYPOINT ["python", "./app.py"]
CMD ["./app.py"]
