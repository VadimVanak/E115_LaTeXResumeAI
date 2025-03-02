# Check if server name is provided
if [ -z "$1" ]; then
    echo "Error: Missing argument. Please provide a DNS name for your server."
    echo "Usage: $0 <DNS_NAME>"
    exit 1
fi

mkdir -p /var/pdflatex
DNS_NAME="$1" docker compose -f ./docker-compose.yml up -d --build --remove-orphans
