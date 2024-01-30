# syntax=docker/dockerfile:1

FROM python:3.11.7-bullseye

RUN apt update
RUN apt install less nano zip openssl openssh-server -y

RUN sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config
# Allow sshd key login
RUN echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config

EXPOSE 2222

# Prepare the game
COPY prepare_the_game.sh /opt/prepare_the_game.sh
RUN chmod +x /opt/prepare_the_game.sh
RUN /opt/prepare_the_game.sh
RUN rm -f /opt/prepare_the_game.sh

WORKDIR /zipper-app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY start_services.sh start_services.sh
RUN chmod +x start_services.sh

COPY . .

EXPOSE 5000

ENTRYPOINT ["/zipper-app/start_services.sh"]
