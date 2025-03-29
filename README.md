# SSL Certificate Check Tool | SSL 证书检查工具

使用 Python 检查网站的 SSL 证书状态，包括有效期、颁发机构等信息。
Check SSL certificate status of websites with Python, including validity period and issuer information.

![Python 3.7+](https://img.shields.io/badge/python-v3.7%2B-blue)

## 功能特点 | Features

- 支持检查单个或多个网站的 SSL 证书
- 支持自定义端口号（例如：example.com:8443）
- 显示证书的生效时间、过期时间、剩余有效天数
- 显示证书颁发机构信息
- 支持中英文界面（根据系统语言自动切换）
- 完善的错误处理和日志记录

## 安装 | Installation

1. 克隆仓库 | Clone the repository
```bash
git clone https://github.com/codertesla/SSLCheck.git
cd SSLCheck
```

2. 安装依赖 | Install dependencies
```bash
# 方式一：使用 requirements.txt（推荐）| Method 1: Using requirements.txt (Recommended)
pip3 install -r requirements.txt

# 方式二：手动安装 | Method 2: Manual installation
pip3 install pyOpenSSL>=25.0.0 cryptography>=44.0.2 typing-extensions>=4.9.0
```

## 使用方法 | Usage

### 方式一：命令行参数（推荐）| Method 1: Command Line Arguments (Recommended)

```bash
# 检查单个网站 | Check single website
python3 SSLCheck.py github.com

# 检查多个网站 | Check multiple websites
python3 SSLCheck.py github.com google.com

# 检查指定端口 | Check specific port
python3 SSLCheck.py example.com:8443
```

### 方式二：修改配置 | Method 2: Modify Configuration

1. 编辑 `SSLCheck.py` 中的 `WEBSITELIST` 变量
2. 运行程序：`python3 SSLCheck.py`

## 输出示例 | Output Example

```bash
$ python3 SSLCheck.py github.com

Thanks for using website SSL certificate check tool.

Website: github.com
Start date: 2025-02-05 00:00:00
Expire date: 2026-02-05 23:59:59
Days left: 313 days
Issued by: Sectigo ECC Domain Validation Secure Server CA
```

```bash
python3 SSLCheck.py google.com

Thanks for using website SSL certificate check tool.


Website: google.com
Start date: 2025-03-10 08:35:59
Expire date: 2025-06-02 08:35:58
Days left: 64 days
Issued by: WR2
```

## 注意事项 | Notes

- 所有域名无需添加 `https://` 前缀
- 如果需要检查特定端口，使用 `hostname:port` 格式
- 程序会自动记录错误日志
- 默认超时时间为 10 秒

## 错误处理 | Error Handling

- 程序会优雅地处理各种错误情况：
  - 无效的域名
  - 连接超时
  - SSL 证书验证失败
  - 不支持的端口
- 所有错误都会被记录到日志中

## 开发计划 | Roadmap

- [ ] 添加证书链信息显示
- [ ] 添加证书有效期预警功能
- [ ] 支持导出检查结果到文件
- [ ] 添加异步检查支持
- [ ] 添加证书信息缓存功能

## 作者 | Author

SSLCheck @[CoderTesla](https://github.com/codertesla), Released under the MIT License.

## 致谢 | Thanks

本项目受以下文章启发：
- [https://flyhigher.top/develop/755.html](https://flyhigher.top/develop/755.html)

## 相关项目 | Similar Projects

- [SukkaW/CheckSSL](https://github.com/SukkaW/CheckSSL)
