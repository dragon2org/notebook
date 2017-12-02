# MYSQL #

## 触发器 ##

### 1.什么是触发器（trigger）

>触发器（trigger)是一个特殊的存储过程，它的执行不是由程序调用，也不是手动启动，而是由事件来出发，比如对一个表进行操作（insert, delete, update)时就会激活它执行。
>触发器经常用于加强数据的完整性约束和业务规则等。触发器可以用DBA_TRIGGER, USER_TRIGGER数据字段中查到。
>触发器有一个非常好的特性就是:触发器可以禁止或回滚违反引用完整性的更改，从而取消所尝试的数据修改。

### 2.触发器语法 ###

	CREATE TRIGGER trigger_name trigger_time trgger_event
		ON tbl_name FOR EACH ROW trigger_stmt


触发程序是与表有关的命名数据库对象，当表上出现特定事件时，将激活该对象。
触发程序与命名为tbl_name的表相关。tbl_name必须引用永久性表。不能将触发程序与TEMPORARY表或者视图关联起来。
trigger_tiem是出发程序的动作时间。它可以是BEFORE或AFTER，以指名触发程序是在激活它的语句之前或之后触发。

trigger_event指名了激活触发程序的语句类型。trigger_event可以使下述值之一:
* INSERT: 将新行插入表时激活触发程序，例如，通过INSERT、LOAD DATA和REPLACE语句。
* UPDATE: 更改某一行时激活触发程序，例如，通过UPDATE语句
* DELETE: 从表中删除某一行时激活触发程序，例如,通过DELETE和REPLACE语句。

请注意, trigger_event与表操作方式激活触发程序的SQL语句并不类似，这点很重要。例如，关于INSERT触发的BEFOR触发程序不仅能被INSERT语句激活，也能被LOAD DATA语句激活。
可能会造成混淆的例子之一是INSERT INTO .. ON DUPLICATE UPDATE...语法： BEFORT INSERT 触发程序对于每一行将激活，后跟AFTER INSERT触发程序，或BEFORE UPDATE和AFTER UPDATE触发程序，具体情况取决于行上是否有重复键。
对于具有相同触发程序动作和事件的给定表，不能有两个触发程序。例如，对于某一表，不能有两个BEFORE UPDATE触发程序。但可以有1个BEFORE UPDATE触发程序和1个BEFOR INSERT触发程序，或1个BEFORE UPDATE触发程序和1个AFTER UPDATE触发程序
trigger_stmt是当触发程序激活时执行的语句。如果你打算执行多个语句，可使用BEGIN...END符合语句结构。这样，就能使用存储程序中允许的相同语法。

## 3创建触发器 ##

1. 用户表 user

		#代码如下
		CREATE TABLE `user`(
		`id` INT(11) NOT NULL AUTO_INCREMENT COMMENT "用户id",
		`name` VARCHAR(32) NOT NULL DEFAULT "" COMMENT "名字",
		PRIMARY KEY(`id`)
		)ENGINE=MyISAM DEFAULT CHARSET=utf8;

		INSERT INTO `user` VALUES 
		(1,'小明'),
		(2,'小红');

2. 评论表 comment

		#代码如下
		
		CREATE TABLE `comment`(
		`id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '评论id',
		`user_id` INT(11) NOT NULL COMMENT '用户id',
		`name` VARCHAR(32) NOT NULL DEFAULT '' COMMENT '用户名称',
		`content` TEXT NOT NULL DEFAULT '' COMMENT '评论内容',
		PRIMARY KEY(`id`)
		)ENGINE=InnoDB DEFAULT CHARSET=utf8;

		INSERT INTO `comment` VALUES
		(1, 2,'小红', '测试触发器'),
		(2, 2, '小红', 'hellow'),
		(3, 1, '小明', '哈哈');

在这里有一个冗余字段name,我们在读取评论可以用联合查询来找到user表中的名字，为什么要冗余字段呢，因简单的sql语句执行效率更高，但不是冗余的字段越多越好，冗余字段多了，同样会增加数据库负担。
我要做的十强是，当我更新user表中的name时。触发器同事更新comment表，就不要写php代码去更新了，当用户被删除是，comment表中，有关该用户的数据将被删除时。

3. 更新触发器

		#代码如下
		
		DELIMITER || #mysql默认结束符号是分号。当你在写触发器或者存储过程时有分号出现，会中止转而执行
		DROP trigger if exists updatename || #删除同名的触发器
		CREATE trigger updatename after update on user for each row #建立触发器
		begin
		#old,new 都是代表当前操作的记录行
		if new.name !=old.name then
		update comment set comment.name=new.name where comment.user_id = old.id;
		end if;
		end||
		DELIMITER ;

4. 触发器删除comment数据

		#代码如下

		DELIMITER ||
		DROP trigger if exists deletecomment||
		CREATE trigger deletecomment BEFORE DELETE ON user FOR EACH ROW
		BEGIN
		DELETE FROM comment WHERE comment.user_id=old.id;
		END||
		DELIMITER ;

