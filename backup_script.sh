#!/bin/bash
# Name:backup_script.sh
# sump the database every one hour and send it to the remote server
backupdir=/home/chow/Documents/whatgame/backups
time=` date +%Y%m%d%H%M `
filename=$backupdir/test$time.sql.gz
mysqldump -u root  testbackup | gzip > $filename
#
scp $filename root@101.132.108.163:/root/junying/backups