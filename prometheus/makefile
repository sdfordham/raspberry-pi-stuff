all: install enable start

install:
	apt-get install prometheus

enable:
	systemctl enable prometheus.service

start:
	systemctl start prometheus.service
