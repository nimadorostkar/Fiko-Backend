FROM nginxinc/nginx-unprivileged:1.20-alpine

COPY ./run.sh /run.sh
COPY default.conf /etc/nginx/default.conf.tpl

ENV LISTEN_PORT=443
ENV APP_HOST=app
ENV APP_LISTEN=443

USER root

RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x run.sh

VOLUME /vol/static

USER nginx


CMD ["./run.sh"]
