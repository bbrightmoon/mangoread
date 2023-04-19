FROM python:3.10

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . app
WORKDIR /app

EXPOSE 8000
ENV DEBUG=false

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

