Title:使用pelican&github搭建个人主页
Date:2015-09-02

###pelican官方文档###

http://docs.getpelican.com/en/3.6.3/index.html

###准备工作###
- pelican基于python环境，首先要安装python
- 安装pelican及markdown  
  `pip install pelican markdown`
- 创建工作目录  
  `mkdir -p ~/projects/yoursite`  
  `cd ~/projects/yoursite`

###使用pelican###
- 生成pelican目录,运行  
  `pelican-quickstart`
- 创建一篇文章  
  `Title: My First Review`  
  `Date: 2010-12-03 10:20`  
  `Category: Review`  
  `Following is a review of my favorite mechanical keyboard.`