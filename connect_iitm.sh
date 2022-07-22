#!/bin/bash
# Script to auto-connect to IITM LDAP Ethernet.

# Ping with a few packets to see if it's up.
if ping -c 1 netaccess.iitm.ac.in &> /dev/null
then
	# Verify whether we're already connected.
	if ping -c 1 google.com &> /dev/null
	then
		echo "Connected Already"
		sleep 1h
		exit 0
	else
		echo "Ethernet Connected, No Internet Access"
		python3 /path/to/your/main.py 
		echo "Done"
	fi
fi
