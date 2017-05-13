#!/bin/bash

IFS="@"
set -- $1
proxy=$1
bkup_proxy=$2
url='http://localhost/zabbix/'
user="Admin"
password="zabbix"


cd /usr/lib/zabbix/alertscripts/switch_proxy
/bin/python switch_proxy.py ${url} ${user} ${password} ${proxy} ${bkup_proxy}
