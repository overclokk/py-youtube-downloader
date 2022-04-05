FROM python:3.8.0-buster

WORKDIR /app

#COPY requirements.txt .
RUN pip install --upgrade pip
RUN #pip install -r requirements.txt

COPY /app .
RUN pip freeze > requirements.txt
RUN #pip install -r requirements.txt
RUN pip install pytube
RUN pip install moviepy

CMD ["python", "index.py"]