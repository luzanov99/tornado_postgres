FROM python:3.10

WORKDIR /project1

COPY requirements.txt /project1/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /project1

CMD ["python", "main.py"]