FROM python:3.7-alpine3.10

WORKDIR /app

RUN apk add tzdata
RUN cp /usr/share/zoneinfo/America/Chicago /etc/localtime
RUN echo "America/Chicago" >  /etc/timezone

ENV TZ America/Chicago

ADD requirements.txt /app/requirments.txt
RUN python -m pip install -r requirments.txt

ADD timeapi.py /app

CMD ["python", "-u", "/app/timeapi.py"]