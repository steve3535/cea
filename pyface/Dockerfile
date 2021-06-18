FROM jfloff/alpine-python
WORKDIR /
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY face.py .
CMD ["python3","face.py"]
