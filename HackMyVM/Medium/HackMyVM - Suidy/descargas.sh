#!/bin/bash

#codigo para obtener la lista de archivos
archivos=$(cat files | awk {'print $1'} | tr -d '/')

#Descarga cada archivo de la lista
for archivo in $archivos
do
	wget "http://192.168.1.12/shehatesme/$archivo"
done
