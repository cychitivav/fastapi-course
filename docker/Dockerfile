FROM python:3.10

RUN pip install fastapi && \
    pip install uvicorn

WORKDIR /home/fastapi

ENTRYPOINT ["uvicorn", "--reload", "--port", "5000", "--host", "0.0.0.0"]
CMD ["main:app"]