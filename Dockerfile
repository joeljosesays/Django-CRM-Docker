FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /django

COPY requirements.txt .
RUN pip install  -r requirements.txt

# Copy other necessary files first to avoid copying unnecessary files causing timeouts
COPY . .

EXPOSE 8000
ENTRYPOINT ["/django/django.sh"]
