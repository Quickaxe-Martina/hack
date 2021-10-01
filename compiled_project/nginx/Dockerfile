FROM nginx

COPY nginx.conf /etc/nginx/
COPY server.conf /home/nginx/
RUN mkdir -p /var/www/esv-front/build && mkdir /tmp/static/
COPY static /tmp/static/
