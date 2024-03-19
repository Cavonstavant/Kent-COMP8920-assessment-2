FROM python:3.9-slim

LABEL org.opencontainers.image.source=https://github.com/Cavonstavant/Kent-COMP8920-assessment-2

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8080

CMD ["flask", "--app", "app.py", "run", "--host", "0.0.0.0", "--port", "8080"]