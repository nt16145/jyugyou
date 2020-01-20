FROM python:3.6

RUN mkdir /jyugyou/

ADD ./jyugyou/requirements.txt /jyugyou/

WORKDIR /jyugyou/

RUN pip install -r requirements.txt

EXPOSE 80
