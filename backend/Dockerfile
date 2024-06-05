FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app

ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
