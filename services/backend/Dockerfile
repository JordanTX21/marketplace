FROM python:3.11-buster

RUN mkdir -p /app/dist
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/ .
# COPY --from=marketplace-frontend-builder /dist /app/dist