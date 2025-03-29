#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Check website SSL certificate status."""

import subprocess
import os
import time
from datetime import datetime
import locale
import sys
import tempfile
import logging
from typing import List, Tuple, Optional
from pathlib import Path
import socket
import ssl
import OpenSSL.crypto as crypto
from urllib.parse import urlparse

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# domains to be checked(without https) | 下方填写需要检查的域名列表，无需写https，同时支持端口号
WEBSITELIST = ['github.com', 'google.com', 'facebook.com']

class SSLCheckError(Exception):
    """Custom exception for SSL checking errors."""
    pass

def get_system_language() -> str:
    """Get system language in a future-proof way."""
    try:
        return locale.getlocale()[0] or 'en_US'
    except Exception:
        return 'en_US'

def get_ssl_cert(hostname: str, port: int = 443) -> dict:
    """Get SSL certificate information for a given hostname."""
    context = ssl.create_default_context()
    
    try:
        with socket.create_connection((hostname, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                return cert
    except (socket.gaierror, socket.timeout, ssl.SSLError) as e:
        raise SSLCheckError(f"Failed to get SSL certificate: {str(e)}")

def check_ssl(website: str) -> None:
    """Check SSL certificate status for a given website."""
    try:
        # Parse hostname and port
        if ':' in website:
            hostname, port = website.split(':')
            port = int(port)
        else:
            hostname = website
            port = 443
            
        # Get certificate
        cert = get_ssl_cert(hostname, port)
        
        # Parse certificate information
        start_date = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z").strftime("%Y-%m-%d %H:%M:%S")
        expire_date = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z").strftime("%Y-%m-%d %H:%M:%S")
        issuer = dict(x[0] for x in cert['issuer'])
        issuer_name = issuer.get('commonName', 'Unknown')
        
        # Calculate days left
        check_datetime = datetime.now()
        expire_datetime = datetime.strptime(expire_date, "%Y-%m-%d %H:%M:%S")
        left_days = (expire_datetime - check_datetime).days
        
        # Print results
        print('\n')
        print(f'Website: {website}')
        print(f'Start date: {start_date}')
        print(f'Expire date: {expire_date}')
        print(f'Days left: {left_days} days')
        print(f"Issued by: {issuer_name}")
        
    except Exception as e:
        logger.error(f"Error checking SSL for {website}: {str(e)}")
        print(f'Error checking {website}: {str(e)}')

def main() -> None:
    """Main function."""
    # Get system language and set greeting
    sys_language = get_system_language()
    
    if sys_language.startswith('zh_'):
        greeting = '\n感谢使用网站 SSL 证书检查工具。'
        notice = '\n这里是默认示例网站的 SSL 检查演示。请在程序中修改 "WEBSITELIST" 列表，或使用命令行参数检查特定网站 SSL 证书。'
    else:
        greeting = '\nThanks for using website SSL certificate check tool.'
        notice = '\n[!]Here are the example domains to be checked by this tool. Modify "WEBSITELIST" in the script or use command line parameters to check specific domains.'

    print(greeting)

    # Get website(s) list from command line or use default
    websitelist = ([site.replace('https://', '').replace('http://', '')
                   for site in sys.argv[1:]] if len(sys.argv) > 1 else WEBSITELIST)
    
    if len(sys.argv) <= 1:
        print(notice)
    
    # Check SSL for each website
    for website in websitelist:
        try:
            check_ssl(website)
        except Exception as e:
            logger.error(f"Unexpected error checking {website}: {str(e)}")
        time.sleep(1)

if __name__ == "__main__":
    main()
