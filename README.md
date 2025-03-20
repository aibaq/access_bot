`access_bot` is a simple telegram bot that controls http/https access to webserver

# Installation
1. Clone the repository
2. Create a virtualenv and install the requirements
3. Create a `.env` file as in the `.env.example` file


# Running the bot
Create a systemd service file for the bot and run the main.py


# Initial setup
Close the access by default
```
iptables -I DOCKER-USER -p tcp --dport 80 -j DROP
iptables -I DOCKER-USER -p tcp --dport 443 -j DROP
```
