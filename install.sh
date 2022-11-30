#!/bin/bash
clear
echo 
echo
if [[ $(id -u) -ne 0 ]] ; then
	printf "you need root assess to install the program\n\n"

	printf  "so please enter the password to login as root!\n\n"

	sudo bash ${0}
	printf "\n\n"
	exit
fi
printf "NOTE: you also need install necessary packages in requirements.txt\n"
for i in 3 2 1
do
	echo "staring installation process in ${i}" ; 
	sleep 1
done
printf "\n\n" 
rm /usr/bin/jawhead &>/dev/null
cp jawhead.py /usr/bin/jawhead
chmod +x /usr/bin/jawhead
printf "\n\ninstalled successfully!"
