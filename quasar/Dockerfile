# base image
FROM node:12.3.1-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /app/package.json
RUN yarn install --frozen-lockfile
RUN yarn global add @quasar/cli@1.2.2

# start app
CMD ["quasar", "dev"]
