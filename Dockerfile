FROM python:alpine
ENV TOKEN "Your Discord Token"

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY server.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./server.py" ]