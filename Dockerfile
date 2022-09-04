FROM python:3.10

WORKDIR /home/jelly/Desktop/Monitor

ADD . .

RUN pip install --upgrade pip

RUN apt-get install -y kmod kbd

RUN pip install -r requirements.txt

CMD ["python3", "src/main_linux.py"]
