# 1st flag
openssl rand -base64 24 | tr -d '\n' > /flag.txt

# 2nd flag
mkdir /zipper-app
openssl rand -base64 24 | tr -d '\n' > /zipper-app/flag.txt

export RANDOM_PASSWORD=$(curl -sSL "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt" | shuf -n 1)

mkdir -p ~/.ssh
ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa -N "$RANDOM_PASSWORD"
mv ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys

