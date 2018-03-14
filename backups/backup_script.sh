#!/bin/bash
# Name:backup_script.sh
# dump the database every one hour and send it to the remote server
backupdir=/home/junying/whatgame/backups/sql
time=` date +%Y%m%d%H%M `
dbname=whatgame
filename=$backupdir/$dbname$time.sql

server=root@10.58.137.74:/home/junying/whatgame-backup


mysqldump -u root  -p $dbname  > $filename
scp $filename $server
