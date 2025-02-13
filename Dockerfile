FROM python:3.9
WORKDIR /connect4
COPY requirements.txt .
RUN pip install -r ./requirements.txt
COPY connect4_backend.py .
COPY .env .
ENV PYTHONUNBUFFERED=1
CMD [ "python", "./connect4_backend.py" ]
