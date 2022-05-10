# -*- coding:utf-8 -*-

# check website SSL status

import subprocess
import os
import time
from datetime import datetime
import locale
import sys

# domains to be checked(without https) | 下方填写需要检查的域名列表，无需写https，同时支持端口号
WEBSITELIST = ['baidu.com','google.com','facebook.com']

# use curl to check website SSL certificate status
def check_ssl(website):

    #利用curl检查证书开始时间，注意一下ca.info保存路径，connect-timeout可以控制超时时间，避免假死
    command0 = f"curl https://{website} --connect-timeout 10 -v -s -o /dev/null 2>/tmp/ca.info" 
    subprocess.check_output(command0, shell=True)
    
    # get start date | 检查证书颁发时间
    command1 = "cat /tmp/ca.info | grep 'start date: '"
    out_bytes1 = subprocess.check_output(command1, shell=True)
    out_text1 = out_bytes1.decode('utf-8')
    start_date = time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text1[-25:-5],"%b %d %H:%M:%S %Y"))


    # get expire date | 检查证书到期时间
    command2 = "cat /tmp/ca.info | grep 'expire date: '"
    out_bytes2 = subprocess.check_output(command2, shell=True)
    out_text2 = out_bytes2.decode('utf-8')
    expire_date = time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text2[-25:-5],"%b %d %H:%M:%S %Y"))


    # get ssl issuer | 获取证书颁发机构
    command3 = "cat /tmp/ca.info | grep 'issuer: '" 
    out_bytes3 = subprocess.check_output(command3, shell=True)
    out_text3 = out_bytes3.decode('utf-8')
    issuer_name = out_text3.split('CN=')[1].split('[')[0].strip()


    # remove tmp file ｜ 删除临时文件
    os.system('rm -f /tmp/ca.info')

    
    # caculate days left | 计算证书有效期剩余天数
    check_datetime = datetime.now() 
    expire_datetime = datetime.strptime(out_text2[-25:-5],"%b %d %H:%M:%S %Y")
    left_days = (expire_datetime - check_datetime).days

    print('\n')
    print(f'Website: {website}')
    print(f'Start date: {start_date}')
    print(f'Expire date: {expire_date}')
    print(f'Days left: {left_days} days')
    print(f"Issued by: {issuer_name}")


def main():
    
    # print greeting
    sys_language,_ = locale.getdefaultlocale() # get system default language
    if sys_language == 'zh_CN':
        greeting = '\n感谢使用网站 SSL 证书检查工具。'
        notice = '\n这里是默认示例网站的 SSL 检查演示。请在程序中修改 "WEBSITELIST" 列表，或使用命令行参数检查特定网站 SSL 证书。'
    else:
        greeting = '\nThanks for using website SSL certificate check tool.'
        notice = '\n[!]Here are the example domains to be checked by this tool. Modify "WEBSITELIST" in the script or use command line parameters to check specific domains.'

    print(greeting)

    # get website(s) list from sys.argv | 从命令行接收网站参数
    if len(sys.argv) > 1:
        websitelist = [site.replace('https://','').replace('http://','') for site in sys.argv[1:]]
    
    else:
        # copy default WEBSITELIST
        websitelist = WEBSITELIST 
        print(notice)

    
    # run SSL check function | 调用 SSL 检查的函数
    for website in websitelist:
        try:
            check_ssl(website)
        except Exception as e:
            print(f'Error: {e}')
        time.sleep(1)

if __name__ == "__main__":
    main()
