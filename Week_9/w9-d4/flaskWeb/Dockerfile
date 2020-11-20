FROM alpine:latest

LABEL Docker y u like dis

# Install System dependencies
RUN apk update \
    apk add --no-cache zlib-dev python-dev build-base


# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

# Install Python dependencies
RUN pip install -Ur requirements.txt
COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]