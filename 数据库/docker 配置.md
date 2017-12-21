# docker 配置

## 安装

mac下载 

```
http://mirrors.aliyun.com/docker-toolbox/mac/docker-for-mac/stable/Docker.dmg #阿里镜像地址
```

拖到到 **docker.app** 到 **Application** 。运行 **docker** 提示需要权限，这里输入 **你的密码**。就完成了docker的安装


## 配置国内下载

访问 **[阿里云开发者平台](https://dev.aliyun.com/search.html)** 。在 **管理中心** 找到你的镜像加速器，获得 **您的专属加速器地址**。

点击状态栏的docker应用图标。选择 **偏好设置->Daemon->Advanced**

在配置文件中添加 

```
{
  "registry-mirrors": ["你的专属加速器地址"]
}

```

点击 **Apply&Rest** 完成加速配置

