FROM python:3.11.0b1-slim-buster

WORKDIR /api

COPY trending/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./trending .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]