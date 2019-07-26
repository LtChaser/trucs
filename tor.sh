#!/bin/bash
if [ -z "$1" ]
then
	output=$(systemctl is-active tor.service)
	if [ "$output" = "inactive" ]
	then
		echo "Tor is inactive: start it ? (y/n)"
		read usrChoice
		if [ "$usrChoice" = "y" ]
		then
			sudo systemctl start tor.service
		elif [ "$usrChoice" != "n" ]
		then
			echo "Wrong input"
		fi

	else
		echo "Tor is active: stop it ? (y/n)"
		read usrChoice
		if [ "$usrChoice" = "y" ]
		then
			sudo systemctl stop tor.service
		elif [ "$usrChoice" != "n" ]
		then
			echo "$usrChoice"
			echo "Wrong input"
		fi
	fi
else
	if [ $1 == "start" ]
	then
		sudo systemctl start tor.service
		systemctl status tor.service

	elif [ $1 == "stop" ]
	then
		sudo systemctl stop tor.service
		systemctl status tor.service
	elif [ $1 == "status" ]
	then
		systemctl status tor.service
	fi
fi
