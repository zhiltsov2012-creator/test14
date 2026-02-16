FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /tmp/fonts && \
    apt-get update && apt-get install -y wget && \
    wget -O /tmp/fonts/DejaVuSans.ttf https://github.com/dejavu-fonts/dejavu-fonts/raw/refs/heads/master/ttf/DejaVuSans.ttf

COPY . .

CMD ["python", "main.py"]