FROM python:3.12.3
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/.
CMD ["python", "osc-to-pixelblaze-forward.py"]