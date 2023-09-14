FROM ubuntu:22.04

WORKDIR /app

VOLUME [ "/var/lib/mysql" ]

RUN apt-get update && apt-get install -y python3 \
    python3-pip \
    libmysqlclient-dev \
    pkg-config

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "bash", "entrypoint.sh" ]
