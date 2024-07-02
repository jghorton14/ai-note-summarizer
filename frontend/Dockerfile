# Stage 1: Build the Vue 3 application
FROM node:14-alpine as build

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package.json package-lock.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Vue 3 application
RUN npm run build

# Stage 2: Serve the Vue 3 application with Nginx
FROM nginx:alpine

RUN ls -al

# Copy the build output from the previous stage to the Nginx html directory
COPY --from=build /app/dist /usr/share/nginx/html

# Copy a custom Nginx configuration file, if needed (optional)
# COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]