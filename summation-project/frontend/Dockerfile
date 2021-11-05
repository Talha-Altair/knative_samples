FROM python:3.9.7-alpine3.14

RUN pip install flask requests python-dotenv

ADD app.py /app/app.py

ADD templates/ /app/templates

WORKDIR /app

CMD ["python","app.py"]