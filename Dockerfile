FROM python:3.14-slim
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY app.py settings.py urls.py ./
EXPOSE 8000
CMD ["python", "-u", "app.py"]
