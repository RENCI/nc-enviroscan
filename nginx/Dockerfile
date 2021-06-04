FROM node:12.8.1-alpine AS build

WORKDIR /app

COPY quasar/package.json quasar/yarn.lock /app/
RUN yarn global add @quasar/cli

COPY quasar /app
RUN yarn
RUN quasar build

FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d

COPY --from=build /app/dist/spa /dist/
