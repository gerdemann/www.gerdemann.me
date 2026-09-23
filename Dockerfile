FROM alpine:3.22@sha256:5291449c3df73caf6ed85e649dec1b9e818b39a5d8c871e97afc13e9cd5e8fa8 AS hugo

ARG TARGETARCH
ARG HUGO_VERSION=0.166.0

WORKDIR /data

RUN apk add --no-cache ca-certificates curl tar tzdata \
    && archive="hugo_${HUGO_VERSION}_linux-${TARGETARCH}.tar.gz" \
    && release="https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}" \
    && curl --fail --show-error --silent --location --remote-name "${release}/${archive}" \
    && curl --fail --show-error --silent --location "${release}/hugo_${HUGO_VERSION}_checksums.txt" \
        | grep " ${archive}$" \
        | sha256sum -c - \
    && tar --extract --gzip --file "${archive}" --directory /usr/local/bin hugo \
    && rm "${archive}"

COPY ./ /data

RUN hugo --gc --minify

FROM nginx:1.30.5-alpine@sha256:bf3201ab56f23e5954646379c775d511fc466e9f11376d9725361064ad07ed35

COPY ./Docker/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./docs/legacy-redirects.nginx.conf /etc/nginx/snippets/legacy-redirects.conf
COPY --from=hugo /data/public /usr/share/nginx/html
