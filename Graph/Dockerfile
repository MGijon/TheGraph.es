FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt
RUN python Graph/manage.py migrate && python Graph/manage.py makemigrations
RUN . /code/
