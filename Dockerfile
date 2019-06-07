FROM python:3.7

COPY . /app
WORKDIR /app
ENV FLASK_APP=hello.py

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
