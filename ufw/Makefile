all: install setup enable

install:
	apt-get install ufw

setup:
	ufw default deny incoming
	ufw default allow outgoing
	ufw limit ssh
	ufw limit 32400
	ufw allow from 192.168.1.1/24 to any port 80
	ufw allow from 192.168.1.1/24 to any port 3000
	ufw allow from 192.168.1.1/24 to any port 8989
	ufw allow from 192.168.1.1/24 to any port 9090
	ufw allow from 192.168.1.1/24 to any port 9091
	ufw logging on

enable:
	systemctl enable ufw
	ufw enable