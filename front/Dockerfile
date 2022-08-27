# pull official base image  (upgrade when fix sass problem)
FROM node:18-alpine

# set work directory
WORKDIR /app

# install dependencies
COPY ./package.json .
COPY ./package-lock.json .

RUN npm install

# copy project
COPY . .

# react default port
EXPOSE 3000

# CMD ["npm", "start"]