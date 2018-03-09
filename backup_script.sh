#!/bin/bash
# Name:backup_script.sh
# dump the database every one hour and send it to the remote server
backupdir=/home/chow/Documents/whatgame/backups
time=` date +%Y%m%d%H%M `
dbname=whatgame
filename=$backupdir/$dbname$time.sql

server=root@101.132.108.163:/root/junying/backups


mysqldump -u root  -p $dbname  > $filename
scp $filename $server