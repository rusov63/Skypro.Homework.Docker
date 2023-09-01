FROM python:3.11-slim-buster
#Debian GNU/Linux 10, python без компилятора

WORKDIR /Skypro.Homework.DRF
#рабочая директория, название проекта

COPY ./requirements.txt /Skypro.Homework.DRF/

RUN pip install -r requirements.txt

COPY . .

#CMD ["python", "manage.py", "runserver"]