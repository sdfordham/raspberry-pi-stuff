Auto Restart
============
File `/etc/systemd/system/transmission-daemon.service`

Command `sudo systemctl edit transmission-daemon`

Systemd override
```
[Service]
Restart=on-failure
RestartSec=5s
```
