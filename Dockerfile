FROM ubuntu:18.04
RUN apt-get update -y \
    && apt-get install -y \
        git \
        build-essential \
        python3-pip \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
ADD ./ /app
RUN apt-get update -y \
    && apt-get install -y \
    locales && locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
CMD ["python3", "app.py"]