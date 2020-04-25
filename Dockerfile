FROM python:3.6.5

RUN apt-get update -qq && \
    apt-get install vim -qq > /dev/null

RUN mkdir -p /app
ADD . /app
WORKDIR /app

RUN pip install --upgrade pip > /dev/null && \
    pip install -r requirements.txt  > /dev/null

EXPOSE 5000

SHELL ["/bin/bash", "-c"]
CMD ["python", "main.py"]

