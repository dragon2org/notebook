# docker 日记

Dockerfile 是用来 记录怎么 构建一个  docker images

可以使用  docker images ls 查看所有的 images

每个在基于docker images 运行的实例 就叫做 docker container

可以使用 docker container ls 查看所有的 container

可以根据 container id 停止某个 container 

docker container stop 1fa4ab2cf395


## 分享 image

先做 tag . 不知道是不是必须 .字符串只能用小写 

docker tag image username/repository:tag 

做了 tag 的 image 会在 image 列表里面以一个 新image 展示

推送 image 到 云


如果出现如下错误
```
denied: requested access to the resource is denied
```

这是因为你的 命名空间错了。 tag 的第一个字符串必须是 你的用户名


