# SpiderDemo
## 1. 打开终端
终端默认起始路径是当前用户目录，使用``cd``指令切换到你想存放的位置 \
比如想切换到桌面，可使用``cd Desktop``指令，返回上一级可使用``cd ..``指令
## 2. 安装依赖
输入``pip3 install requests bs4`` 然后回车，等待安装完成 \
依赖只用安装一次，以后就不用了
## 3. 克隆项目
终端输入``git clone https://github.com/hhzhhz1996/spiderDemo.git`` 然后回车，会在当前目录看到spiderDemo的文件夹 \
克隆也只需要一次

## 4. 运行
使用``cd spiderDemo`` 进入到文件夹内 \
指令格式为``python3 spiderDemo.py -u {url} -p {path}`` 来运行脚本 \
-u 表示爬取的网站，用网站地址替换掉```{url}``` \
-p 表示保存地址，用文件夹路径替换掉```{path}``` \
-u -p 这两个参数如果不填，默认网址就是微信发我那个。会在桌面创建一个叫img的文件夹，图片保存在里面

默认指令为 ```python3 spiderDemo.py``` 

## 5. 注意
每次要运行前可以先在spiderDemo文件夹下执行```git fetch``` 这样可以获取到最新的代码