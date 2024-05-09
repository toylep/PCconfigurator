FROM python:3.12-slim-bullseye

WORKDIR /app

COPY req.txt /app/
RUN pip install -r req.txt
# CMD ["pip","install","-r","req.txt"]