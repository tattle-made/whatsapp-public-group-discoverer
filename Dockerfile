FROM python:3.8.1-alpine3.11
WORKDIR /app
COPY test.py /app/test.py
# RUN apk add gcc
# RUN pip3 install scrapy
ENTRYPOINT [ "python3", "test.py" ]