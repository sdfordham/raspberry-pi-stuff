all: install permissions start

install:
	apt-get update
	apt-get upgrade
	apt-get install transmission-daemon

permissions:
	adduser "debian-transmission" plexmediaserver

start:
	systemctl start transmission-daemon
