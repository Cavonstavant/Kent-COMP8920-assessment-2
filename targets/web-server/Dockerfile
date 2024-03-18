
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8080

CMD ["flask", "--app", "app.py", "run", "--host", "0.0.0.0", "--port", "8080"]