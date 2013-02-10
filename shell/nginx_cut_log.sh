#!/bin/bash
nginx_dir=/usr/local/nginx
logs_dir=/var/log/nginx
bak_dir=/var/www/nginx_log_bak

echo '> move...'
cd $logs_dir
mv *log $bak_dir
sleep 1

echo '> rebuild log...'
$nginx_dir/sbin/nginx -c /etc/nginx/nginx.conf -s reopen
sleep 1

echo '> doing package...'
cd $bak_dir
tar czf `date +%Y%m%d`.tgz *log
sleep 2

echo '> clear temp logs...'
rm -f *log

echo '> DONE!'
