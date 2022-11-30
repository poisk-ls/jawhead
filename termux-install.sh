#!/bin/bash
clear
printf "\n\n"
rm /data/data/com.termux/files/usr/bin/jawhead&>/dev/null
cp jawhead.py /data/data/com.termux/files/usr/bin/jawhead
chmod +x /data/data/com.termux/files/usr/bin/jawhead
printf "\n\ninstalled successfully!\n"
