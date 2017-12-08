# 0X00 安装

```
brew install tmux
yum install tmux
```

# 0X01 结构
session>widnow>pane
一个会话（Session）可以包含多个窗口，一个窗口（Window）可以包含多个窗格（Pane）

会话适用于分别管理大的工作内容，例如日常工作，实验或是系统管理，都可以分别在一个会话中进行。
窗口适用于分别管理这些大工作中的项目。例如，在用于实验的会话中可能有一叫做 noderestapi 的窗口用于调试 node REST API，有一个叫做 lua 的窗口用于调试 lua 脚本。
窗格适用于查看当前的项目。例如，在系统管理的会话中有一个叫做 logs 的窗口，在这个窗口中可以打开多个窗格分别用于查看 access log，error log和system log。


# 0X02 会话命令

PK = Ctrl +  B

```
显示所有会话
PK  s
tmux ls

新建会话
tmux new -s session-name

进入已有会话
tmux a
tmux a -t session-name

断开会话
tmux detach
PK d

关闭会话
tmux kill-session -t session-name

重命名当前会话
PK $

```

# 0x03 window管理

```
c 创建一个新窗口
, 重命名当前窗口
w 列出所有窗口
% 水平分割窗口
" 竖直分割窗口
n 选择下一个窗口
p 选择上一个窗口
0~9 选择0~9对应的窗口
```

# 0X04 pane管理

```
% 创建一个水平窗格
" 创建一个竖直窗格
h 将光标移入左侧的窗格*
j 将光标移入下方的窗格*
l 将光标移入右侧的窗格*
k 将光标移入上方的窗格*
q 显示窗格的编号
o 在窗格间切换
} 与下一个窗格交换位置
{ 与上一个窗格交换位置
! 在新窗口中显示当前窗格
x 关闭当前窗格> 要使用带“*”的快捷键需要提前配置，配置方法可以参考上文的“在窗格间移动光标”一节
```