FROM node:20-alpine
WORKDIR /app

COPY package.json package-lock.json ./
RUN npm config set fetch-retries 5 \
    && npm config set fetch-retry-mintimeout 20000 \
    && npm ci

COPY . .
RUN chown -R node:node /app

# node:20-alpine ships a built-in non-root "node" user (uid/gid 1000);
# no need to create one ourselves.
USER node
EXPOSE 3000
CMD ["npm", "run", "dev"]
