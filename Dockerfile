FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "src.wsgi:application", "--bind", "0.0.0.0:8000", "--timeout", "120"]
# CMD ["gunicorn", "src.wsgi:application", "--bind", "0.0.0.0:8000", "--timeout", "120"]

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]