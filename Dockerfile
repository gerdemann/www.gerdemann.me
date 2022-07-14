FROM alpine as hugo

WORKDIR /data

COPY ./ /data

RUN apk add --update tzdata hugo \
    && hugo -D

FROM nginx:1.22-alpine

COPY ./Docker/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=hugo /data/public /usr/share/nginx/html