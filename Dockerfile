FROM python:3.9

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ../../AOS-develop/AOS-develop/requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ../../AOS-develop/AOS-develop /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "OpenApi"]