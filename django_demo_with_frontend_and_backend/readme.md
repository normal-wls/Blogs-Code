### 代码对应文章：
[手把手Django+Vue前后端分离开发入门(附demo)](https://zhuanlan.zhihu.com/p/128976272)

### 目录结构
- appfront：前端部分代码
- book_demo：后端部分代码（这里面前端代码已经build好放进去了，对应于dist文件夹）

### 运行
- 安装好文章中所需要的python包。

- terminal（命令行）中运行：
``` bash
cd book_demo
python manage.py migrate
python manage.py runserver
```

- 打开浏览器，访问: 127.0.0.1:8000