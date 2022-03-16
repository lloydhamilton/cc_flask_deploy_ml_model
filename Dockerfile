FROM python:3.9-slim

# Install dependencies, exclude dev dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY app /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["flask_model.py"]