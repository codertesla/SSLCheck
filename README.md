# SSL certificate Check Tool | SSL 证书检查工具

Check SSL certificate status of your website with Python. 
用 Python 检查你网站的 SSL 证书有效期及颁发机构。


## Usage

### One Way
1. Modify "WEBSITELIST" in the script
2. Run script : ` python3 SSLCheck.py `

### The Other Way (recommend)
1. Run script with command line parameters： `python3 SSLCheck.py google.com`


## Output 

```
$ python3 checkSSL.py google.com

Thanks for using website SSL certificate check tool.

Website: google.com
Start date: 2020-07-07 08:04:38
Expire date: 2020-09-29 08:04:38
Days left: 59 days
Issued by: GTS CA 1O1
```


## Thanks
This project is highly inspired by : [https://flyhigher.top/develop/755.html](https://flyhigher.top/develop/755.html)

## Similar Projects
* [SukkaW/CheckSSL](https://github.com/SukkaW/CheckSSL)

## Author
SSLCheck @[CoderTesla](https://github.com/codertesla) , Released under the MIT License.

---


## 用法


### 方式一
1. 修改代码中顶部的 "WEBSITELIST" ，把你想检查的网站域名填进去
2. 然后运行程序： ` python3 SSLCheck.py `



### 方式二 （推荐）
1. 带参数运行本程序： `python3 SSLCheck.py google.com`



## 输出

```
$ python3 checkSSL.py google.com

感谢使用网站 SSL 证书检查工具。

Website: google.com
Start date: 2020-07-07 08:04:38
Expire date: 2020-09-29 08:04:38
Days left: 59 days
Issued by: GTS CA 1O1
```

## 特别致谢

本项目深受此文启发，特别鸣谢 
[https://flyhigher.top/develop/755.html](https://flyhigher.top/develop/755.html)


## 同类项目
* [SukkaW/CheckSSL](https://github.com/SukkaW/CheckSSL)

## 作者
SSLCheck @[CoderTesla](https://github.com/codertesla) , 遵循 MIT 开源协议。
