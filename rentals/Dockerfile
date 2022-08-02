FROM python:3.11.0b1-slim-buster

WORKDIR /api

COPY rentals/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./rentals .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]