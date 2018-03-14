#!/usr/bin/expect 
set timeout 60

set db_pwd "xswqaz"
set server_pwd "xsw21qaz"

spawn bash /home/junying/whatgame/backups/backup_script.sh
expect "Enter password: "
send "$db_pwd\n"
expect "*assword:"
send "$server_pwd\n"
expect eof