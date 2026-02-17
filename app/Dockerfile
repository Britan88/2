FROM mcr.microsoft.com/playwright/python:v1.42.0-jammy
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt && playwright install
CMD ["python","main.py"]
