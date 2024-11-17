TORRENT_DATA_PATH = /media/pi/Seagate\ Backup\ Plus\ Drive/torrent_files
TORRENT_FILE_PATH = /media/pi/Seagate\ Backup\ Plus\ Drive/
EXCLUDE_TRACKER = tracker.baconbits.org
USERNAME = stiofainf

all: install permissions enable start load

install:
	apt-get update
	apt-get upgrade
	apt-get install transmission-daemon

permissions:
	adduser "debian-transmission" media
	chgrp media /media/

enable:
	systemctl enable transmission-daemon
	sed -i "s/^ExecStart=.*$/ExecStart=\/usr\/bin\/transmission-daemon -f --log-debug --logfile \/etc\/transmission-daemon\/logs\/log.log/" /usr/lib/systemd/system/transmission-daemon.service
	sudo systemctl daemon-reload

start:
	systemctl start transmission-daemon

load:
	python -m pip install tautoloader
	python -m tautoloader.cli -t ${TORRENT_DATA_PATH} -d ${TORRENT_FILE_PATH} -e ${EXCLUDE_TRACKER} -u ${USERNAME} -s 5 -c 0.7

backup:
	cp -rL /var/lib/transmission-daemon/info /home/pi/
	chown pi /home/pi/info

restore:
	rm -r /var/lib/transmission-daemon/.config/transmission-daemon/*
	cp -r /home/pi/info/* /var/lib/transmission-daemon/.config/transmission-daemon/
	chown debian-transmission /var/lib/transmission-daemon/.config/transmission-daemon/
