FROM python:3.8

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    # build-essential \
    # libssl-dev \
    # libffi-dev \
    # python3-dev \
    # build-essential \
    # libjpeg-dev \
    # zlib1g-dev \
    # libpq-dev \
    # gcc \
    # libc-dev \
    # bash \
    # git \
    # postgresql-server-dev-all \
    # musl-dev \
    # libmagic1 \
    && pip3 install --upgrade pip

# set environment variables
# ENV LIBRARY_PATH=/lib:/usr/lib
# ENV PYTHONUNBUFFERED=1
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /ai_chatapp

COPY requirements.txt /ai_chatapp/

# RUN pip install gunicorn

# install all the requirements
RUN pip install -r requirements.txt

#copy the contents
COPY . /ai_chatapp/

# for docker demo-server environment uncomment the following line for development comment it out
ENTRYPOINT ["python", "ai_chatapp/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
