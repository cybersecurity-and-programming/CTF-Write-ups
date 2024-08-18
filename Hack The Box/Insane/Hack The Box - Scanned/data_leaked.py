#!/usr/bin/python3
import requests
import sys
import re
import struct
from argparse import ArgumentParser

def main(url):
    try:
        r = requests.get(url)
        r.raise_for_status()

        response = re.findall(r"sys_4919\(\) = 0x([a-f0-9]+)", r.text, re.MULTILINE)
        data = b""
        for val in response:
            data += struct.pack("Q", int(val, 16))
        print(data.decode())
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
    except IOError as e:
        print(f"Error writing to file: {e}")
    except UnicodeDecodeError as e:
        print(f"Error decoding exfiltrated data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-u", "--url", help="Direccion web del host a analizar", required=True)
    args = parser.parse_args()
    main(args.url)