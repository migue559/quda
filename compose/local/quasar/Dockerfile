FROM node:12.18.4-alpine3.9

WORKDIR /app

COPY ./quasar/package.json /package.json
RUN npm install -g @quasar/cli@1.1.1
RUN npm i && npm rebuild node-sass
