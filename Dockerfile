FROM python:3.7-alpine3.10

WORKDIR /app

ADD requirements.txt /app/requirments.txt
RUN python -m pip install -r requirements.txt

ADD app.py /app

CMD ["python", "-u", "/app/app.py"]