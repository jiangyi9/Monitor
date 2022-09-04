FROM python:3.10

WORKDIR ./Desktop/Monitor

ADD . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python3", "src/main_linux.py"]
