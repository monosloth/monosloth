FROM python:3

COPY ./ /app

RUN pip install monosloth pyyaml pymysql

WORKDIR /app

CMD ["python", "./main.py"]
