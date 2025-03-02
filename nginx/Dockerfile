# Use the official NGINX image
FROM nginx:latest

# Install gettext for envsubst
RUN apt-get update && apt-get install -y gettext-base
# Set working directory

WORKDIR /etc/nginx

# Remove default NGINX configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom NGINX configuration
COPY nginx.conf.template /etc/nginx/conf.d/default.conf.template

# Expose HTTP (80) and HTTPS (443) ports
EXPOSE 80 443

# Copy the entrypoint script
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/docker-entrypoint.sh"]
