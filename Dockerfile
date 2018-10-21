FROM    python:3.6-alpine3.7 as builder

RUN     mkdir /install
WORKDIR /install
COPY    requirements.txt /requirements.txt
RUN     pip install --install-option="--prefix=/install" -r /requirements.txt

FROM    python:3.6-alpine3.7
####
# Runtime arguments & Environment variables
ENV     DEBUG='No'
ENV     SECRET_KEY '99U[5?+;v9d.A9S'
ENV     ENVIRONMENT 'production'

# By default, run 2 processes
ENV     UWSGI_CHEAPER 2
# By default, when on demand, run up to 16 processes
ENV     UWSGI_PROCESSES 16

# By default, allow unlimited file sizes, modify it to limit the file sizes
# To have a maximum of 1 MB (Nginx's default) change the line to:
ENV     NGINX_MAX_UPLOAD 1m
# By default, Nginx will run a single worker process, setting it to auto
# will create a worker for each CPU core
ENV     NGINX_WORKER_PROCESSES 1
# By default, Nginx listens on port 80.
# To modify this, change LISTEN_PORT environment variable.
# (in a Dockerfile or with an option for `docker run`)
ENV     LISTEN_PORT 80

###
# Install Nginx uWSGI, Supervisor
RUN     apk add --no-cache su-exec nginx uwsgi uwsgi-python3 supervisor && \
	    rm /etc/nginx/conf.d/default.conf


###
# Copy configuration files
COPY    ./deploy/nginx.conf /etc/nginx/nginx.conf
# Copy the modified Nginx conf
COPY    ./deploy/nginx-custom.conf /etc/nginx/conf.d/nginx.conf

# Copy the base uWSGI ini file to enable default dynamic uwsgi process number
COPY    ./deploy/uwsgi.ini /etc/uwsgi/
# Which uWSGI .ini file should be used, to make it customizable
ENV     UWSGI_INI /app/api/uwsgi.ini

# Custom Supervisord config
COPY    ./deploy/supervisord.conf /etc/supervisord.conf

###
# Copy Project doe and dependencies
COPY    --from=builder /install /usr/local
COPY    ./api /app/api

WORKDIR /app
ENV     PYTHONPATH /app

EXPOSE  80
EXPOSE  443

# Set entry point
COPY    ./deploy/entrypoint.sh /entrypoint.sh
RUN     chmod +x /entrypoint.sh

ENTRYPOINT ["sh", "/entrypoint.sh"]

CMD     ["/usr/bin/supervisord"]
