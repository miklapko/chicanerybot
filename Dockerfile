FROM --platform=linux/amd64 python:3.7-alpine

WORKDIR /usr/src/app

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . .

RUN touch replied_comments.txt

RUN touch test.lol

CMD ["python", "./bot.py"]
