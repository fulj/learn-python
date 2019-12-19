https://www.code-learner.com/category/python/


__new__ parameter cls
__init__
hasattr

<<<<<<< HEAD
事实上，super 和父类没有实质性的关联。
super(cls, inst) 获得的是 cls 在 inst 的 MRO 列表中的下一个类。
=======

将 requirements.txt 文件放到虚拟目录 venv 下，pycharm自动识别安装相应的 package。
所有第三方的包都会被pip安装到Python3的site-packages目录下。

安装虚拟环境的包： pip install virtualenv
安装虚拟环境：virtualenv --no-site-packages venv
激活虚拟环境 C:\Python27\Scripts\env\Scripts>activate.bat

激活虚拟环境
linux中： source venv/bin/activate
在cmd中：activate.bat
在powershell中：./activate.ps1
在git命令行中。。。：激活不了。。。

查看解释器路径
import sys
print(sys.excutable)


windows 可以直接在cmd控制台查看
where python
where pip

linux 下
which python


目录
DLLs： Python 自己使用的动态库
Doc： 自带的 Python 使用说明文档（如果上面安装时不选择，应该会没有，这个没具体试过）
include： 包含共享目录
Lib： 自己的标准库，和第三方的库（site-package下）
libs： 编译生成的Python 自己使用的静态库
Scripts： 各种包/模块对应的可执行程序。安装时如果选择了pip。那么pip的可执行程序就在此！
tcl： 桌面编程包
>>>>>>> a5cc05ed79301d5c17259e8bf38b889c90851454
