FROM python:3.9 AS builder_python_sport

RUN uname -a
RUN apt update && apt install -y --no-install-recommends python-dev python-setuptools

WORKDIR /srv/project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

FROM builder_python_sport as builder

COPY src/ src/
COPY commands/ commands/
COPY ./Makefile Makefile

RUN chmod +rx -R commands

RUN useradd -ms /bin/bash admin
RUN chown -R admin:admin /srv/project
RUN chmod 755 /srv/project
USER admin

CMD bash -C "./commands/wsgi_dev.sh"

# CMD ["python", "./src/manage.py", "runserver", "0.0.0.0:8111"
# EXPOSE 8111
#docker run --rm -t -d -p 8001:8111
