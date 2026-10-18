
FROM python:3.12-slim

WORKDIR /app

COPY app/ /app/

RUN python -m compileall -q /app

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
