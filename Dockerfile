FROM python:3.12-slim-bullseye

WORKDIR /app

COPY confugurator /app/
COPY req.txt /app/
CMD [ "pip","install","-r" "req.txt" ] 
CMD [ "python","manage.py","runserver" ] 