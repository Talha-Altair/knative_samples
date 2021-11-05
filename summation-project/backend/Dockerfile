FROM python:3.9.7-alpine3.14

RUN pip install flask

ADD app.py /app/app.py

WORKDIR /app

CMD ["python","app.py"]