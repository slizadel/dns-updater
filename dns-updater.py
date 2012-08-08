#!/usr/bin/env python

import clouddns
import requests
import syslog

r = requests.get('http://icanhazip.com')
actual_ip = (r.text).strip()

dns = clouddns.connection.Connection('<RS USERNAME>','<RS API KEY>')
domain = dns.get_domain(name='<ROOT DOMAIN>')
home = domain.get_record(name='<DYNAMIC A RECORD>')

home_ip = home.data

if actual_ip != home_ip:
  syslog.syslog("DNS needs to be updated. Setting to %s." % actual_ip)
  home.update(data=actual_ip,ttl=300)

else:
  syslog.syslog("DNS not updating. Already set to %s." % home_ip)
