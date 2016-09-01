#PyQt学习日记
>参考资料 http://bbs.fishc.com/thread-59816-1-1.html

1.关于PyQt
PyQt是用来创建GUI应用程序的工具包。它是Python编程语言与已获得成功的Qt库的混合体。其中Qt库是这个星球上最强大的GUI库之一。

PyQt5的实现被视作Python的一个模块。它由300多个类和接近6000个函数有方法构成。作为一个跨平台的工具包，PyQt可以在所有主流的操作系统（Unix、Window、Mac）上运行。PyQt有两种许可，开发者可以在GPL和商业许可证之间做出选择。

###PyQt4结构和介绍
- QtCire模块包含了核心的非GUI功能函数，用于处理一下方面：日期、文件和目录、数据结构、URL、MIME、线程和进程。
- QtGUI模块包含了绘图组件以及绘图相关的类，比如按钮、窗口、状态栏、工具栏、滑块、位图、颜色、字体等。
- QtNetWork模块包含用于网络编程的类，用户可以用这些类实现TCP/IP和UDP的客户端或服务器。并且使用这些类会使网络编程更容易，轻便。
- QtXML包含用于XML文件的类。该模块提供了SAX和DOMAPI两种XML文件处理方式的实现
- QtSVG模块包含了用于显示SVG文件内容的类。
- QtOpenGL模块用于渲染使用OpenGPL库创建的3D或者2D图形。并且它支持QtGUI库和OpenGL库的无缝结合。
- QtSql库则提供了用于操作数据库的类
>PyQt5中。模块结构有所改变，PyQt4中的QtGui模块在PyQt5中分为了GtGUI，QtPrintSuport,QtWidgets三个模块。
>PyQt4中的QtOpenGL模块中，只有QGLContext,QGLFormat和QGLWidget这三个类还可以在PyQt5中使用。

##2.1初次使用
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


##2.2设置程序图标
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


###2.3显示提示信息

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
		#QtWidgets.QToolTip.setFont(QtGui.QFont("Times", 10))

	app = QtWidgets.QApplication(sys.argv)
	tooltip = Tooltip()
	tooltip = show()
	sys.exit(app.exec_())
	