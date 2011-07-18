#!/usr/bin/expect
set timeout 60
spawn /usr/bin/ssh -CTnN -D 7070 username@host

expect {
    "password:" {
	send  "password\r"
    }
}
interact {
    timeout 60 { send " "}
}
