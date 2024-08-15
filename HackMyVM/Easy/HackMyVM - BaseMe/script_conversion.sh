#!/bin/bash
for word in $(cat "/usr/share/seclists/Discovery/Web-Content/common.txt");do
	echo "$word" | base64 >> "seclist-commont.txt"
done