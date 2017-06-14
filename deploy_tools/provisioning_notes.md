配置新网站
========

## 需要安装的包：
* nginx
* Python 3
* Git
* Pip
* Virtualenv

以ubuntu为例，可以执行下面的命令安装
 sudo apt-get update
 sudo apt-get install nginx git python3 python3-pip
 sudo pip3 install virtualenv

## 配置自动部署
* fabric
* sudo apt-get install fabric
* fab deploy:host=ubuntu@staging.artshub.xyz -i superlists.pem



## 配置Nginx虚拟主机
 * 参考nginx.template.conf
 * 把SITENAME替换成所需的域名，例如staging.my-domain.com
 * 放在/etc/nginx/site-availables
 * 创建一个符号链接：sudo ln -s /etc/nginx/site-availables/$SITENAME /etc/nginx/site-enabled/$SITENAME
 * 重新启动nginx服务
 * sed "s/SITENAME/staging.artshub.xyz/g;s/USER/ubuntu/g" nginx.template.conf | sudo tee /etc/nginx/sites-available/staging.artshub.xyz


## Systemd任务
 * 参考gunicorn-systemd.template.service
 * 放在/etc/systemd/system
 * 通过sudo systemctl start xxx 启动
 * sed "s/SITENAME/staging.artshub.xyz/g;s/USER/ubuntu/g" gunicorn-systemd.template.service | sudo tee /etc/systemd/system/gunicorn-staging.artshub.xyz.service

## 文件夹结构：
 * 假设有用户账户，家目录为/home/username
 └── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv
