#!/bin/bash
# Check if server name is provided
if [ -z "$1" ]; then
    echo "Error: Missing argument. Please provide a DNS name for your server."
    echo "Usage: $0 <DNS_NAME>"
    exit 1
fi

# Export the argument as DNS_NAME
export DNS_NAME="$1"
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo usermod -aG docker $USER

# Check if certbot is installed and install it if not
if ! command -v certbot &> /dev/null
then
    echo "Certbot not found. Installing..."
    sudo apt install -y certbot
fi

# Request DNS certificates
sudo certbot certonly --standalone \
    -d "$DNS_NAME" \
    --register-unsafely-without-email \
    --agree-tos 
	
sudo apt-get install git -y
git clone https://github.com/VadimVanak/E115_LaTeXResumeAI.git /home/LaTeXResumeAI
cd /home/LaTeXResumeAI/

#TODO: update DNS name in docker project
#TODO: run docker-compose
