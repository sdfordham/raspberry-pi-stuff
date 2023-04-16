all: install permissions enable start

install:
	apt-get update
	apt-get upgrade
	apt-get install apt-transport-https
	curl https://downloads.plex.tv/plex-keys/PlexSign.key | gpg --dearmor | sudo tee /usr/share/keyrings/plex-archive-keyring.gpg >/dev/null
	echo deb [signed-by=/usr/share/keyrings/plex-archive-keyring.gpg] https://downloads.plex.tv/repo/deb public main | sudo tee /etc/apt/sources.list.d/plexmediaserver.list
	apt-get update
	apt install plexmediaserver

permissions:
	adduser "pi" plex
	setfacl -m g:plex:rx /media/pi
	chgrp plex "/media/pi/"
	chmod g+rwx "/media/pi/"
	chgrp plex "/media/pi/Seagate Backup Plus Drive/"
	chmod g+rwx "/media/pi/Seagate Backup Plus Drive/"

enable:
	systemctl enable plexmediaserver

start:
	systemctl start plexmediaserver
