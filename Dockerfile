FROM --platform=linux/amd64 3.7-alpine

WORKDIR /usr/src/app

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . .

RUN touch replied_comments.txt

CMD ["python", "./bot.py"]
