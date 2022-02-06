FROM python:3.9.10-alpine3.15

WORKDIR /app

RUN apk add tzdata && cp /usr/share/zoneinfo/America/Chicago /etc/localtime && echo "America/Chicago" >  /etc/timezone

ENV TZ America/Chicago

ADD requirements.txt /app/requirments.txt
RUN python -m pip install -r requirments.txt

ADD timeapi.py /app

CMD ["python", "-u", "/app/timeapi.py"]