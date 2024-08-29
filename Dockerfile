FROM python:3.11.9
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 app:app --bind 0.0.0.0:$PORT app:app