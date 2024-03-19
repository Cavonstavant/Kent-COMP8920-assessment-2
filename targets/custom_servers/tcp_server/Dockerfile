FROM python:3.9-slim

LABEL org.opencontainers.image.source=https://github.com/Cavonstavant/Kent-COMP8920-assessment-2

WORKDIR /app

COPY tcp_server.py .

EXPOSE 9999

CMD ["python", "tcp_server.py", "0.0.0.0", "9999"]