
#同步插入
DELIMITER $
DROP TRIGGER IF EXISTS sync_package_insert$
CREATE TRIGGER sync_package_insert AFTER INSERT ON rht_train.rht_package FOR EACH ROW
BEGIN
INSERT INTO `rhi_idc`.`rhi_package` (`id`, `appname`, `appid`, `name`, `sortid`, `stars`, `imgurl`, `total`, `ytotal`, `isfree`, `details`, `stime`, `etime`, `remark`, `flag`, `istj`, `ctime`) VALUES (new.id, new.appname, new.appid, new.name, new.sortid, new.stars, new.imgurl, new.total, new.ytotal, new.isfree, new.details, new.stime, new.etime, new.remark, new.flag, new.istj, new.ctime);
END$
DELIMITER ;



#同步删除
DELIMITER $
DROP TRIGGER IF EXISTS sync_package_delete$
CREATE TRIGGER sync_package_delete BEFORE  DELETE ON rht_train.rht_package FOR EACH ROW
BEGIN
DELETE FROM rhi_idc.rhi_package where rhi_idc.rhi_package.id = old.id;
END$
DELIMITER ;


#同步更新
DELIMITER $
DROP TRIGGER IF EXISTS synv_package_update$
CREATE TRIGGER sync_package_update AFTER UPDATE ON `rht_train`.`rht_package` FOR EACH ROW
BEGIN
IF (`new`.`appname` != `old`.`appname` OR `new`.`appid` != `old`.`appid` OR `new`.`name` != `old`.`name` OR `new`.`sortid` != `old`.`sortid` OR `new`.`stars` != `old`.`stars` OR `new`.`imgurl` != `old`.`imgurl` OR `new`.`total` != `old`.`total` OR `new`.`ytotal` != `old`.`ytotal` OR `new`.`isfree` != `old`.`isfree` OR `new`.details != `old`.`details` OR `new`.`stime` != `old`.`stime` OR `new`.`etime` != `old`.`etime` OR `new`.`remark` != `old`.`remark` OR `new`.`flag` != `old`.`flag` OR `new`.`istj` != `old`.`istj` OR `new`.`ctime` != `old`.`ctime`)
THEN
UPDATE `rhi_idc`.`rhi_package` SET `appname`=`new`.`appname`, `appid`=`new`.`appid`, `name`=`new`.`name`, `sortid`=`new`.`sortid`, `stars`=`new`.`stars`, `imgurl`=`new`.`imgurl`, `total`=`new`.`total`, `ytotal`=`new`.`ytotal`, `isfree`=`new`.`isfree`, `details`=`new`.`details`, `stime`=`new`.`stime`, `etime`=`new`.`etime`, `remark`=`new`.`remark`, `flag`=`new`.`flag`, `istj`=`new`.`istj`, `ctime`=`new`.`ctime` WHERE (`id`=`old`.id);
END IF;
END$
DELIMITER ;
