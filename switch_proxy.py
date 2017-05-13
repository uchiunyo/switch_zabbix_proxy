#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.zabbixapi import ZabbixAPI
from lib.zbxcommoncmd import *
import sys

args = sys.argv

url = args[1]
user = args[2]
password = args[3]
proxy_name = args[4]
bkup_proxy_name = args[5]

# connect zabbix server
zbx = ZabbixAPI(url)
zbx.login(user, password)

# Get id of problem proxy
proxyid = get_proxyid(zbx, proxy_name)

# Get id of backup proxy
bkup_proxyid = get_proxyid(zbx, bkup_proxy_name)

# Obtain the id of the host using the problem proxy
hostids = get_use_proxy_hostids(zbx, proxyid)

# Switch proxy of target host for backup
update_hosts(zbx, hostids, {"proxy_hostid":bkup_proxyid})
