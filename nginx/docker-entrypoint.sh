#!/bin/sh

# Ensure the environment variable is set
if [ -z "$DNS_NAME" ]; then
  echo "Error: DNS_NAME environment variable is not set."
  exit 1
fi

# Replace placeholders in the Nginx configuration
envsubst '$DNS_NAME' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf

# Start Nginx
exec nginx -g 'daemon off;'

