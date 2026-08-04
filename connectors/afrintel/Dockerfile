FROM python:3.12-slim
ENV CONNECTOR_TYPE=EXTERNAL_IMPORT PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /opt/opencti-connector-afrintel
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY src ./src
RUN useradd --create-home --uid 10001 connector && chown -R connector:connector /opt/opencti-connector-afrintel
WORKDIR /opt/opencti-connector-afrintel/src
USER connector
ENTRYPOINT ["python3", "main.py"]
