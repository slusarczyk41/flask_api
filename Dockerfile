FROM python:3

RUN mkdir /code
WORKDIR /code
COPY ./content_api/* /code/
RUN mkdir /code/data

RUN pip install -r requirements.txt
