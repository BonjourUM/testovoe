FROM python:3.11-slim
EXPOSE 8000
WORKDIR /usr/src/
COPY requirements.txt .
RUN pip install gunicorn --no-cache-dir --disable-pip-version-check \
    && pip install -r requirements.txt --no-cache-dir --disable-pip-version-check
COPY ./testovoe .
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "udp.wsgi:application"]
