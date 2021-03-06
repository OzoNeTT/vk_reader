FROM python:3.7-slim-buster

COPY requirements.txt /tmp/requirements.txt

ENV PACKAGES="gcc \
              build-essential \
              python3-dev"

RUN set -ex && \
    apt-get update -y && \
    apt-get install -y $PACKAGES && \
    pip install -r /tmp/requirements.txt && \
    apt-get remove -y $PACKAGES

WORKDIR /opt/builder

COPY . /opt/builder

CMD ["python", "reader/reader.py"]
