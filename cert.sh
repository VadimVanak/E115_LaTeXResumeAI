#!/bin/bash
export CERT_DIR=~/certificates
export DNS_NAME=cv.vanak.de

mkdir -p "$CERT_DIR"
export OVERLEAF_DNS_NAME="overleaf.$DNS_NAME"

# Check if certbot is installed and install it if not
if ! command -v certbot &> /dev/null
then
    echo "Certbot not found. Installing..."
    sudo apt update && sudo apt install -y certbot
fi

# Request DNS certificates
sudo certbot certonly --standalone \
    --work-dir "$CERT_DIR" \
    --config-dir "$CERT_DIR" \
    --logs-dir "$CERT_DIR" \
    -w "$CERT_DIR" \
    -d "$DNS_NAME" \
    -d "$OVERLEAF_DNS_NAME" \
    --register-unsafely-without-email \
    --agree-tos \

