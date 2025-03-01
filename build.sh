export CERT_DIR=~/certificates
export DNS_NAME=cv.vanak.de
mkdir -p ./nginx/cert
sudo cp $CERT_DIR/live/$DNS_NAME/fullchain.pem ./nginx/cert
sudo cp $CERT_DIR/live/$DNS_NAME/privkey.pem ./nginx/cert
docker compose -f ./docker-compose.yml up -d --build --remove-orphans
