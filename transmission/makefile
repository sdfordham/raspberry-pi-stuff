TORRENT_DATA_PATH = /media/pi/Seagate\ Backup\ Plus\ Drive/torrent_files
TORRENT_FILE_PATH = /media/pi/Seagate\ Backup\ Plus\ Drive/
EXCLUDE_TRACKER = tracker.baconbits.org
USERNAME = stiofainf

all: install permissions start load

install:
	apt-get update
	apt-get upgrade
	apt-get install transmission-daemon

permissions:
	adduser "debian-transmission" plex

start:
	systemctl start transmission-daemon

load:
	python -m pip install tautoloader
	python -m tautoloader.cli -t ${TORRENT_DATA_PATH} -d ${TORRENT_FILE_PATH} -e ${EXCLUDE_TRACKER} -u ${USERNAME} -s 5 -c 0.7
