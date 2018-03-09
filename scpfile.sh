#!/usr/bin/expect 
set timeout 60

set db_pwd "xswqaz"
set server_pwd "1234567*Chow"

spawn ./backup_script.sh
expect "Enter password: "
send "$db_pwd\n"
expect "*password:"
send "$server_pwd\n"
expect eof