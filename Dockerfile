FROM alpine:3.5
RUN apk add --update python py-pip
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD python -m pytest tests