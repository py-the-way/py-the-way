FROM python:3.7-slim

WORKDIR /backend

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "start.py"]