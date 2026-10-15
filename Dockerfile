FROM python:3.13-alpine AS builder

WORKDIR /src
COPY categories /src/categories
RUN python3 categories/build.py --output /dist

FROM nginx:1.28-alpine3.21
LABEL org.opencontainers.image.source https://github.com/openzim/content-classification-system

COPY --from=builder /dist /usr/share/nginx/html
COPY docker/nginx-default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
