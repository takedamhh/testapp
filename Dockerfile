FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install flask boto3
ENTRYPOINT ["python"]
CMD ["app.py"]


