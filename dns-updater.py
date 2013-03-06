#!/usr/bin/env python

import os
import syslog
import socket

import pyrax
import requests
import argh

def main(domain, email, subdomain=None, ttl=300, rec_type='A', public=False, 
         comment=None, creds_file='~/.rackspace_cloud_credentials'):
  domainName = domain

  if public:
    r = requests.get('http://icanhazip.com')
    actual_ip = (r.text).strip()
  else:
    actual_ip = socket.gethostbyname(socket.gethostname())

  pyrax.set_credential_file(os.path.expanduser(creds_file))
  dns = pyrax.cloud_dns

  if subdomain:
    subDomainName = subdomain
    fqdn = '%s.%s' % (subDomainName, domainName)
  else:
    fqdn = domainName

  emailAddress = email

  new_record = { "type": rec_type,
                 "name": fqdn,
                 "data": actual_ip
               }

  try:
    domain = dns.find(name=domainName)
    record = domain.find_record(rec_type, name=fqdn)
    if not record:
      record = domain.add_record(new_record)
      syslog.syslog("Record not found, but a new one was created with IP: %s" % acutal_ip)
    elif record.data != actual_ip:
      record.update(data=actual_ip)
      syslog.syslog("Domain needed updating. Updated to %s from %s" % (acutal_ip, record.data))
  except pyrax.exceptions.NotFound:
    try:
      dom = dns.create(name=domainName, emailAddress=emailAddress,
              ttl=ttl, comment=comment)
      dom.add_record(new_record)
      syslog.syslog("Nothing existed! We created the Domain and Record for the first time.")
    except pyrax.exceptions.DomainCreationFailed as e:
      syslog.syslog("Nothing existed! Domain creation failed: %s" % e)

if __name__ == '__main__':
  argh.dispatch_command(main)
