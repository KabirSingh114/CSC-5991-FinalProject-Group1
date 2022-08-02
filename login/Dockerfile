FROM python:3.11.0b1-slim-buster

WORKDIR /api

COPY login/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./login .

CMD ["python3", "app.py"]