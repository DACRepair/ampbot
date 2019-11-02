FROM python:alpine
ENV TOKEN "Your Discord Token"
ENV MESSAGE "{name} sent an amp link. Please use real links dipshit.\n ||{url}||"

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY server.py .
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./server.py" ]