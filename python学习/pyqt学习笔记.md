# PyQt学习日记
>参考资料 http://bbs.fishc.com/thread-59816-1-1.html


1.关于PyQt
PyQt是用来创建GUI应用程序的工具包。它是Python编程语言与已获得成功的Qt库的混合体。其中Qt库是这个星球上最强大的GUI库之一。

PyQt5的实现被视作Python的一个模块。它由300多个类和接近6000个函数有方法构成。作为一个跨平台的工具包，PyQt可以在所有主流的操作系统（Unix、Window、Mac）上运行。PyQt有两种许可，开发者可以在GPL和商业许可证之间做出选择。


## PyQt4结构和介绍 ##


- QtCire模块包含了核心的非GUI功能函数，用于处理一下方面：日期、文件和目录、数据结构、URL、MIME、线程和进程。
- QtGUI模块包含了绘图组件以及绘图相关的类，比如按钮、窗口、状态栏、工具栏、滑块、位图、颜色、字体等。
- QtNetWork模块包含用于网络编程的类，用户可以用这些类实现TCP/IP和UDP的客户端或服务器。并且使用这些类会使网络编程更容易，轻便。
- QtXML包含用于XML文件的类。该模块提供了SAX和DOMAPI两种XML文件处理方式的实现
- QtSVG模块包含了用于显示SVG文件内容的类。
- QtOpenGL模块用于渲染使用OpenGPL库创建的3D或者2D图形。并且它支持QtGUI库和OpenGL库的无缝结合。
- QtSql库则提供了用于操作数据库的类
>PyQt5中。模块结构有所改变，PyQt4中的QtGui模块在PyQt5中分为了GtGUI，QtPrintSuport,QtWidgets三个模块。
>PyQt4中的QtOpenGL模块中，只有QGLContext,QGLFormat和QGLWidget这三个类还可以在PyQt5中使用。

### 2.1初次使用 ###
&nbsp;&nbsp;&nbsp;&nbsp;这段代码非常简单，它的作用只是显示一个小小的窗口，然而你可以对这个窗口作很多事情。我们可以改变窗口的尺寸。最大化，最小化窗口。为了实现这些功能，我们需要编写大量的代码。但是，已经有人将这些实现这些功能的代码写好了，因为这些操作在很多程序中都是重复出现的，没有必要一次此的重新写这些代码，所以这些代码想PyQt的使用者隐藏了。PyQt是一种高层的工具集，如果我们用更底层的工具，以下的是示例代码将会超过几十行。

	# -*-coding: utf-8 -*-
	"""第一个程序"""

	"""载入模块。基本GUI窗口部件都在QtWidgets模块中"""
	from PyQt5 import QtWidgets  
	import sys
	
	"""每一个PyQt5程序都需要一个application对象，application对象包含在QtGui模块中，sys.argv是命令行参数列表"""
	app = QtWidgets.QApplication(sys.argv)  

	"""QWidget部件是PyQt5中所有用户界面的父类。这里我们使用没有参数的默认构造函数，它没有集成其他类。我们称没有分类的first_window为一个window"""
	first_window = QtWidget()  

	"""resize设置窗口大小"""
	first_window.resize(400,300) 
	first_window.setWindowTitle('我的第一个程序')

	"""最后我们进入该程序的主循环。 事件处理从本行语句（sys.exit(app.exec_()) ）开始。主循环接收事件消息并将其分发给程序的各个部件。如果调用exit()或主部件被销毁，主循环就会结束。使用sys.exit()方法退出可以确保程序可以完成的结束，这种情况下系统环境变量会记录程序是如何退出的。"""
	first_window.show()
	sys.exit(app.exec_()) 


### 2.2设置程序图标 ###
程序图标就是一个小图片，通常显示在程序标题栏的左上角。

	# -*- coding: utf-8 -*-
	"""图标"""
	import sys
	from PyQt5 import QtWidgets, QtGui
	
	#创建一个名为Icon的新类，该类继承QtWidgets.QWidget类。因此我们必须调用两个构造函数-Icon的构造函数和继承类QtGui.QWidget类的构造函数
	class Icon(QtWidgets.Qwidget):
		def __init__(self, parent = None):
			QtWidgets.QWidget.__init__(self, parent)

			#setGeometry()方法完成两个功能，设置窗口在屏幕上的位置和设置窗体本身的大小。它的前两个参数是窗口在屏幕上的x,y坐标。后两个参数是窗口本身的宽和高
			self.setGeometry(300, 300, 250, 150)
			self.setWindowTitle("图标")
			#setWindowIcon()方法用来设置程序同步，它需要一个QIcon类型的对象作为参数。调用QIcon构造函数时,我们需要提供要显示的图标的路径
			self.setWindowIcon(QtGui.QIcon(r'samle.ico'))

	app = Qtwidgets.QAppliaction(sys.argv)
	icon = Icon()
	icon.show()
	sys.exit(app.exec_())


### 2.3显示提示信息 ###

我们可以为任何窗口部件设置一个悬停提示。

	#-*- coding: utf-8 -*-
	"""悬停提示信息"""
	import sys
	from PyQt5 import QtWidgets,QtCore,QtGuo

	class Tooltip(QtWidgets.QWidget):
		def __init__(self, parent=None):
		
		self.setGeometry(835, 465, 250, 150)
		self.setWindowTitle("提示信息")
		
		#设置文件信息
		self.setToolTip("this is a <b>Qwidget<b> widget")
		#设置字体
		#QtWidgets.QToolTip.setFont(QtGui.QFont("Times", 10))

	app = QtWidgets.QApplication(sys.argv)
	tooltip = Tooltip()
	tooltip = show()
	sys.exit(app.exec_())

### 2.4关闭窗口 ###
自定义关闭按钮。简要介绍Qt的信号和槽机制
下面是QPushButton的构造函数，我们将会在下面的示例中使用它

	QPushButton(string text, QWidget parent = None)

text表示将显示在按钮上的文本。parent是其对象，用于指定按钮显示在哪个部件中。在我们的实例中。parent是一个Qwidget对象.

	#-*- coding:utf-8 -*-
	"""用按钮关闭程序"""
	import sys
	from PyQt5 import QtWidgets, QtCore, QtGui
	
	class QuitButton(QtWidgets.QWidget):
		def __init__(self, parent=None):
			QtWidgets.QWidget.__init__(self, parent)
			
			self.setGeometry(300, 300, 250, 150)
			self.setWindowTitle("我的关闭程序")
			#实例化按钮对象，传入父级对象
			quit_button = QtWidgets.QPushButton("关闭", self)
			#设置按钮位置
			quit_button.setGeometry(10, 10, 60,35)
			#绑定点击事件
			#PyQt5的时间处理系统建立在信号-槽机制之上。如果我们单击quit按钮，那么信号clicked就会被触发。槽函数可以是PyQt自带的槽函数，也可以是任何Python可以调用的函数。QtCore.QObject.connect()方法可以将信号和槽函数链接起来。在我们的示例中槽函数是PyQt中已定义的quit()函数。通过connect方法就可以建立发送者（quit按钮）和接收者（应用程序对象）之间的通信
			quit_button.clicked.connect(QtWidgets.qApp.quit)

	app = QtWidgets.QApplication(sys.argv)
	quitbutton = QuitButton()
	quitbutton.show()
	sys.exit(app.exec_())
	
	
PyQt4和PyQt5的调用区别
	
	# pyqt5中的做法
	quit_button.clicked.connect(QtWidgets.qApp.quit)
	# pyqt4中的做法  
	self.connect(quit,QtCore.SIGNAL('clicked()'),QtGui.qApp,QtCore.SLOT('quit()'))

>[官方文档-信号和槽](http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html)


### 2.5 消息窗口 ###

默认情况下，如果我们点击了窗口标题栏上的X标记，窗口就会被关闭。但是有时候我们想要改变这一默认行为。比如，我们正在编辑的文件内容发生了变化，这时若单击X标记关闭窗口，编辑器应当弹出确认窗口。

	#-*- coding:utf-8 -*-
	"""消息窗口示例"""
	import sys
	from PyQt5 import QtWidgets, QtGui, QtCore
	
	class MessageBox(QtWidgets.Qwidget):
		def __init__(self, parent=None):
			QtWidgets.QWidget.__init__(self, parent)
			self.setGeometry(300, 300, 250, 150)
			self.setWindowTitle("消息窗口演示程序")
		
		#重写关闭事件
		def closeEvent(self, event):
			replay = QtWidgets.QMessageBox.question(self, '确认推出','你确定要推出么？',QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
			
			if replay == QtWidgets.QmessageBox.Yes:
				event.accept()
			else:
				event.ignore()

	app = QtWidgets.QApplication(sys.argv)
	qb = MessageBox()
	qb.show()
	sys.exit(app.exec_())

### 2.6将窗口放在屏幕中心 ###

以下脚本展示了将窗口放在屏幕中间的位置方法

	#-*- coding: utf-8 -*-
	"""窗口置中"""
	import sys
	from PyQt5 import QtWidgets
	
	class Center(QtWidgets.QWidget):
		def __init__(self, parent=None):
			QtWidgets.QWidget.__init__(self, parent)
			self.setWindowTitle("窗口置中程序")
			self.resize(250, 150)
			self.center()

		def center(self):
			screen = QtWidgets.QDesktopWidget().screenGeometry()
			size = self.geometry()
			self.move((screen.width()- size.width())/2, (screen.height()- size.height()/2)

	app = QtWidgets.QApplication(sys.argv)
	center = Center()
	center.show()
	sys.exit(app.exec_())

## 3.PyQt5中的菜单和工具栏 ##

### 3.1主窗口 ###

QMainWindow 类用来创建应用程序的主窗口。 通过该类，我们可以创建一个包含状态栏、工具栏和菜单的景点应用程序框架。

### 3.2 状态栏 ###

状态栏是用来显示状态信息的串口部件。


	# -*- coding: utf-8 -*-
	"""状态栏程序"""
	import sys
	from PyQt5 import QtWidgets
	
	class MainWindow(QtWidgets.QMainWindow):
		def __init__(self):
			#调用父类的构造方法
			super(MainWindow, self).__init__()
			
			self.resize(250, 150)
			self.setWindowTitle("状态栏程序示例")
			#设置状态栏
			self.statusBar().showMessage("就绪")

	app = QtWidgets.QApplication(sys.argv)
	main_winodw = MainWindow()
	main_window.show()
	sys.exit(app.exec_())

### 3.3菜单栏 ###

菜单栏是GUI程序最明显的组成部分。它由一组位于不同菜单中的命令组成。在控制台程序中，我们必须记住那些晦涩难懂的命令。但在GUI程序中，通过菜单栏我们将命令合理的放置在不同的菜单中来降低学习新应用程序的时间开销。

	# -*- coding: utf-8 -*-
	"""菜单栏"""
	import sys
	from PyQt5 import QtWidgets, QtGui
	
	class MainWindow(QtWidgets.QMainWindow):
		def __init__(self):
			super(MainWindow, self).__init__()
			
			self.resize(250, 160)
			self.setWindowTitle("菜单比例")
			
			#设置菜单项
			exit_menu = QtWidgets.QAction(QtGui.QIcon(r"1.ico", "退出", self)
			#设置文本备注-一般用于显示快捷键。空格应该要转义
			exit_menu.setShortcut("Ctr+Q")
			exit_menu.triggered.connect(QtWidgets.qApp.quit)

			self.statusBar()
			
			menubar = self.menuBar()
			#添加一个菜单
			file = munubar.addMenu("文件")
			#添加事件
			file.addAction(exit_menu)

	app = QtWidgets.QApplication(sys.argv)
	mainwindow = MainWindow()
	mainwindow.show()
	sys.exit(app.exec_())

### 3.4 一个综合的例子 ###

在本章的最后一个示例中，我们将创建一个菜单栏、一个工具栏和一个状态栏。我们还会创建一个中心部件。

	# -*- coding: utf-8 -*-
	"""我的程序"""
	import sys
	from PyQt5 import QtWidgets, QtGui

	class MainWindow(QtWidgets.QMainWindow):
		def __init__(self):
			supert(MainWindow, self).__init__()

			self.resize(350, 250)
			self.setWindowTitle("我的程序")
			#创建文本编辑器控件
			text_edit = QtWidgets(text_edit)
			#设置为中心部件。中心部件将占满窗口空间
			self.setCentralWidget(text_edit)
			
			exit_action = QtWidgets.QAction(QtGui.QIcon(r"sample.png", "退出", self)
			exit_action.setStatusTip("退出程序")
			exit_action.setShortcut("Ctrl+Q")
			exit_action.triggered.connect(QtWidgets.qApp.quit)
				
			self.statusBar()
			
			self.menu_bar = self.menuBar()
			file = self.menu_bar.addMenu("文件")
			file.addAction(exit_action)
			
			self.toolbar = self.addToolBar("退出")
			self.toolbar.addAction(exit_action)

	app = QtWidgets.QAppliaction(sys.argv)
	main_window = MainWindow()
	main_window.shwo()
	sys.exit(app.exec_())

## 4.PyQt5中的布局管理 ##

布局管理器是编程中重要的一部分。所谓布局管理是指我们在窗口中安排部件位置的方法。布局管理有两种工作方式：绝对定位方式（absolute positioning)和布局类别方式(layout classes)

### 4.1 绝对定位方式 ###
该方式下。程序员编程制定每一个不见得位置和像素。当使用绝对定位方式时。需要注意一下几点:
* 改变窗口大小时，窗口中部件的大小和位置不会随之改变。
* 在不同平台上，应用程序可能看起来不尽相同
* 在应用程序中改变字体可能会导致布局混乱
* 如果你打算改变窗口布局，你就必须得重新书写所有的部件布局，这一工作非非常的乏味且耗时较多。



		# -*- coding:utf-8 -*-
		"""绝对定位演示"""

		import sys
		from PyQt5 import QtWidgets, QtGui
	
		class MainWindow(QtWidgets.QMainWindow):
		def __init__(self):
			super(MainWindow, self).__init__()
			
			self.setWindowTitle("绝对定位演示程序")
			self.resize(250, 150)
			
			#使用move x y设置 QLable 部件位置。坐标原点为左上角顶点。
			QtWidgets.QLable('Couldn\'t', self).move(15, 10)
			QtWidgets.QLable('care', self).move(35, 40)
			QtWidgets.QLable('less', self).move(55, 65)
			QtWidgets.QLable('and' , self).move(115, 65)
			QtWidgets.QLable('then', self).move(135, 45)
			QtWidgets.QLable('you', self).move(115, 25)
			QtWidgets.QLable('kiss', self).move(145, 10)
			QtWidgets.QLable('me', self).move(215, 10)

		app = QtWidgets.QApplication(sys.argv)
		main_window = MainWindow()
		main_window.shwo()
		sys.exit(app.exec_())



### 4.2 Box布局 ###
使用布局类别的方式的布局管理比决定定位的布局管理更加灵活实用。它是窗口部件的首先布局管理方式。最基本的布局类别是QHBoxLayout和QVBoxLayout布局管理方式。分别将窗口部件水平和垂直排列。

假设我们要将两个按钮放在窗口的右下角。为创建该布局。我们需要使用一个水平Box和一个垂直的Box,另外为了创建鼻血的空间，我们还需要添加一个伸缩间隔的元素（stretch factor)

		#-*- coding:utf-8 -*-
		"""Box定位演示"""
		
		import sys
		from PyQt5 import QtWidgets
			
		class BoxLayout(QtWidgets.QWidget):
			def __init__(self):
				super(BoxLayout, self).__init__()

			self.setWindowTitle("Box定位演示程序")
			
			self.ok_button = QtWidgets.QPushButton("确定")
			self.cancel_button = QtWidgets.QPushButton("取消")

			self.h_box = QtWidgets.QHBoxLayout()
			self.h_box.addStretch(1)
			self.h_box.addWidget(self.ok_button)
			self.h_box.addWidget(self.cancel_button)
			
			self.v_box = QtWidgets.QVBoxLayout()
			self.v_box.addStretch(1)
			self.v_box.addLayout(self.h_box)
			
			self.setLayout(self.v_box)
			self.resize(300, 150)
		
		app = QtWidgets.QAppliaction(sys.argv)
		box_layout = BoxLayout()
		box_layout.show()
		sys.exit(app.exec_())


### 4.3网格布局

最通用的布局类别是网格布局（QGridLayout)。该布局方式将窗口空间划分为许多行和列。要创建该布局方式，我们需要使用QGridLayout类。

	# -*- coding: utf-8 -*-
	"""网格布局示例"""
	
	import sys
	from PyQt5 import QtWidgets
	
	class GridLayout(QtWidgets.QMainWindow):
		def __init__(self):
			super(GridLayout, self).__init__()
		
			self.setWindowTitle("网格布局演示程序")
        	buttton_names = ['Cls', 'Bck', '', 'Close',
                         '7', '8', '9', '/',
                         '4', '5', '6', '*',
                         '1', '2', '3', '-',
                         '0', '.', '=', '+']
			#创建一组网格布局按钮的实例main_ground,然后setCentraWidget方法将它置为中心部件
			main_ground = QtWidgets.QWidget()
			self.setCentraWidget(main_ground)
			gird = QtWidgets.QGridLayout()
			#创建一个网格布局
			for [n, (x, y)] in enumerate([(i, j) for i in range(5) for j in range(4)]):
	            if (x, y) == (0, 2):
	                grid.addWidget(QtWidgets.QLabel(buttton_names[n]), x, y)
	            else:
	                grid.addWidget(QtWidgets.QPushButton(buttton_names[n]), x, y)
			#将网格布局用setLayout方法置于之前创建好的main_ground实例上
			main_ground.setLayout(grid)
	
	app = QtWidgets.QApplication(sys.argv)
	grid_layout = GridLayout()
	grid_layout.show()
	sys.exit(app.exec_())

在这个示例中，我们创建一组网格布局的按钮。为了填补Bak 和 Close 按钮之间的空白，我们使用QLabel部件。

部件在网格布局中可以跨越多行或多列。我们将下面的示例中演示该情况。

	# -*- coding: utf-8 -*-
	"""网格布局跨行示例"""
	
	import sys
	from PyQt5 import QtWidgets

	class GridLayout(QtWidgets.QMainWindow):
		def __init__(self):
			super(GridLayout, self).__init__()
			
			self.setWindowTitle("网格跨越多行示例")
			
			main_ground = QtWidgets.QWidget()
			self.setCentralWidgets(main_groud)
			
			#创建网格布局，并将该布局中的部件间隔设为20个字距
			grid = QtWidgets.QGridLayout()
			grid.setSpacing(20)

			grid.addWidget(QtWidgets.QLabel("标题:", 1, 0)
			grid.addWidget(QtWidgets.QLineEdit(), 1, 1)
			grid.addWidget(QtWidgets.QLabel("作者：", 2, 0)
			grid.addWidget(QtWidgets.QLineEdit(), 2, 1)
			grid.addWidget(QtWidgets.QLable("评论:", 3, 0)
			#设置Edit部件的行跨度为5，列跨度为1
			grid.addWidget(QtWidgets.QTextEdit(), 3, 1, 5, 1)
			
			main_groud.setLayout(grid)
			self.resize(350, 300)

	app = QtWidgets.QAppliaction(sys.argv)
	grid_layout = GridLayout()
	grid_layout.show()
	sys.exit(app.exec_())

## 5. PyQt5的事件和信号。

在本章学习中。我们将介绍发生在应用程序中的事件和信号。
### 5.1 事件

事件（events)是GUI程序中很重要的一部分。它是由用户或系统产生。当我们调用程序的exec_()方法时，程序就会进入主循环中。主循环捕获事件并将它们发送给相应的对象进行处理。为此。引入了一种独一无二的处理模式：信号与槽机制。

### 5.2 信号槽 ###

当用户点击一个按钮，拖动一个滑块或进行其他动作时，相应的信号就会被发射。除此之外，信号还可以因为环境的变化而被发射。比如一个运动的时钟就会发射间隔时间信号等。而所谓的槽则时一个方法，该方法将会响应它所连接的信号。在Python中。槽可以时任何可以被调用的对象。
	

	# -*- coding: utf-8 -*-
	"""信号槽示例"""
	
	import sys
	from PyQt5 import QtWidgets, QtCore

	class SignalSlot(QtWidgets.QWidget):
		def __init__(self):
			supert(SignalSlot, self).__init__()
			
			self.setWindowTitle("信号槽演示程序")
			#创建一个LCD显示器和一个滑块。
			lcd = QtWidgets.QLCDNumber(self)
			
			#创建滑块
			slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
			
			v_box = QtWidgets.QVBoxLayout()
			v_box.addWidget(lcd)
			v_box.addWidget(slider)
			
			self.setLayout(v_box)
			# emit.signal.connect(accept.slot)
			# 如果信号发送对象为emit。要发射的信号是signal.信号接收者对象accept,对信号做出响应的槽函数slot
			slider.valueChanged.connect(lcd.display)
			self.resize(250, 150)

	app = QtWidgets.QAppliaction(sys.argv)
	qb = SignalSlot()
	qb.show()
	sys.exit(app.exec_())


### 5.3 重写事件的处理方法 ###
PyQt中的事件处理主要依赖重写事件处理函数来实现


	# -*- coding: utf-8 -*-
	"""用Esc键推出示例"""
	import sys
	from PyQt5 import QtWidgets, QtCore

	class Escape(QtWidgets.QWidget):
		def __init__(self):
			super(Escape, self).__init__()
			
			self.setWindowTitle("Esc退出演示程序")
			self.resize(250, 150)
		
		def keyPressEvent(self, event):
			# 如果按下esc,则关闭当前窗口
			if event.key() == QtCore.Qt.Key_Escape:
				self.close()


	app = QtWidgets.QApplication(sys.argv)
	escape = Escape()
	escape.show()
	sys.exit(app.exec_())


### 5.4 发射信号 ###

通过QtCore.QObject创建的对象可以发射信号。如果我们点击按钮，就会生成一个clicked()信号。在以下的例子里我们看到如何发射一个信号。

	# -*- coding: utf-8 -*-
	"""发射信号示例"""
	import sys
	from PyQt5 import QtWidgets, QtCore

	class EmitSignal(QtWidgets.QWidget):
		#创建一个叫做closeEmitApp的信号。
		closeEmitApp = QtCore.pyqtSignal()
		
		def __init__(self):
			super(EmitSignal, self).__init__()
			
			self.setWindowTitle("发射信号演示程序")
			self.resize(250, 150)
			
			self.closeEmitApp.Connect(self.close)
		
		def mousePressEvent(self, QMousetEvent):
			#通过信号变量emit()方法发射一个信号
			self.closeEmitApp.emit()

	app = QtWidgets.QAppliaction(sys.argv)
	es = EmitSignal()
	es.show()
	sys.exit(app.exec_())


## 6 PyQt5中的对话框 ##

对话窗口和对话框是现代GUI应用程序必不可少的一部分。生活中“对话”被定义为发生在两个人或更多人之间的会话。而在计算机世界，“对话”则是人与程序之间的“会话”。人机对话的形式有在输入框内建如内容，修改已有数据，改变应用程序的设置等。
对话框在人机交互中扮演着非常重要的角色。
从本质上说。只存在两种形式对话框：预定义对话框和定制对话框。

### 6.1 QInputDialog输入对话框 ###

	# -*- coding: utf-8 -*-
	"""输入对话框示例"""
	import sys
	from PyQt5 import QtWidgets, QtCore

	class InputDialog(QtWidgets.QWidget):
		def __init__(self):
			super(InputDialog, self).__init__()
			
			self.setWindowTitle("输入对话框演示程序")
			self.setGeometry(300, 300, 350, 80)
			self.button = QtWidgets.QPushButton("对话框”, self)
			self.button.move(20, 20)
			self.button.clicked.connect(self.show_dialog)
			self.setFocus()
			
			self.label = QtWidgets.QLineEdit(self)
			self.label.move(130, 22)
		
		def show_dialog(self)
			text, ok = QtWidgets.QInputDialog.getText(self, "输入对话框", "请输入你的名字"）
			if ok:
				self.label.setText(text)

	app = QtWidgets.QApplication(sys.argv)
	input_dialog = InputDialog()
	input_dialog.show()
	sys.exit(app.exec_())


### 6.2 QColorDialog 颜色对话框

QcolorDialog提供了用于选择颜色的对话框

	# -*- coding: utg-8 -*-
	"""颜色对话框示例"""
	import sys
	from PyQt5 import QtWidgets, QtGui, QtCore
	
	class ColorDialog(QtWidgets.QWidget):
		def __init__(self):
			super(ColorDialog, self).__init__()
			
			self.setWindowTitle("颜色对话框演示程序")
			