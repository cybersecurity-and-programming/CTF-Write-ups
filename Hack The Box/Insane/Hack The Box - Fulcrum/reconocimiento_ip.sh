#!/bin/bash

function exit_app(){
	echo -e "\e[1;31m[!] Saliendo de la aplicacion\e[0m"
	exit 1
}
trap exit_app INT
for i in 130 132 228; do
	(ping -c 1 192.168.1.122.${i})
done