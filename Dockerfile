FROM public.ecr.aws/lambda/python:3.9

WORKDIR /var/task

COPY app app
COPY lambda_handler.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["lambda_handler.lambda_handler"]
