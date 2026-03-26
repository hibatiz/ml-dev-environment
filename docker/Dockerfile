FROM python:3.11-slim

WORKDIR /app

COPY docker/requirements-docker.txt .

RUN pip install --no-cache-dir -r requirements-docker.txt

COPY src/ ./src/

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
