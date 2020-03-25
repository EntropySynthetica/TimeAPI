FROM python:3.7-alpine3.10

WORKDIR /app

ADD requirements.txt /app/requirments.txt
RUN python -m pip install -r requirments.txt

ADD timeapi.py /app

CMD ["python", "-u", "/app/timeapi.py"]