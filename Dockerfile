FROM python:3.9.7-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip 
#RUN pip install Django==3.2.10
#RUN pip install djangoresetframework==3.13.1

RUN pip install djangorestframework
# RUN pip install markdown
# RUN ip install django-filter

# copy project
COPY . /usr/src/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]