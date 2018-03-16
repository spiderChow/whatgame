# whatgame
run the web app:
  gunicorn manager:app -b 10.58.5.14:5000 -p whatgame.pid -D
the app server is on 10.58.5.14
the backup server is on 10.58.137.74
if you want to kill the running app: cat whatgame.pid and get the process id and then kill it.
if you want to dump the ranking from db:
	mysql  -u root -p  -e "select * from whatgame.users order by score DESC"  > rank.txt

The DB file should be dumped in ./backups/sql with the datetime in the filename, every hour. If you want to manually dump the DB, just './scpfile.sh' in the command. And the file would show up in that dir. Also, ./backups/rank.txt would be updated meanwhile.
