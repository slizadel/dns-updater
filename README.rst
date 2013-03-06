==================================================================
 Script to dynamically update DNS record with a host's NAT'd IP
==================================================================

:Homepage:  https://github./slizadel/dns-updater
:Credits:   Copyright 2012 Slade Cozart <slade.cozart@gmail.com>
:Licence:   BSD
:API Reference: http://docs.rackspace.com/cdns/api/v1.0/cdns-devguide/content/index.html

Dependencies
============

- pyrax >= 1.3.2 (pip install pyrax)
- argh (pip install argh)
- argcomplete (pip install argcomplete)
- requests (pip install requests)

Usage
=====

1. Add a credentials file with the following format:

    [rackspace_cloud]

    username = myusername

    api_key = 01234567890abcdef

2. Add the command to cron:

    /path/to/dns_updater.py example.com me@example.com -s host1 --public

3. ???
4. Profit.
