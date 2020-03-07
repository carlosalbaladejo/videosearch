FROM python:3.8-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        curl  \
    && rm -rf /var/lib/apt/lists/*

###########################################################################
# User Aliases
###########################################################################
USER root
# Add a non-root user to prevent files being created with root permissions on host machine.
ARG PUID=1000
ENV PUID ${PUID}
ARG PGID=1000
ENV PGID ${PGID}

# Añadir user video_user as non-root. Si todo se ejecuta como usuario root,
# los archivos no son modificables desde el host
RUN groupadd -g ${PGID} video_user && \
  useradd -u ${PUID} -g video_user -m video_user && \
  usermod -p "*" video_user -s /bin/bash 

WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip \
  && pip install -r requirements.txt \
  && rm -rf /root/.cache

COPY ./src /app

RUN chown -R video_user:video_user /app

WORKDIR /app/src

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
