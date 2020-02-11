FROM python:3.8.1-alpine3.11
WORKDIR /app
COPY test.py /app/test.py
ENV PYTHONUNBUFFERED=1 
# RUN apk add gcc
# RUN pip3 install scrapy
CMD python3 test.py