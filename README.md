
When using with docker make the following changes to make `ufw` work with docker:

Open /etc/ufw/after.rules in an editor:

```
sudo vim /etc/ufw/after.rules
```

Append the following lines to the end of the file (you might need to replace eth0 with whatever your external facing interface is, which you can see in ifconfig):
```
# Put Docker behind UFW
*filter
:DOCKER-USER - [0:0]
:ufw-user-input - [0:0]

-A DOCKER-USER -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
-A DOCKER-USER -m conntrack --ctstate INVALID -j DROP
-A DOCKER-USER -i eth0 -j ufw-user-input
-A DOCKER-USER -i eth0 -j DROP
COMMIT
```

```
sudo systemctl restart ufw
```
