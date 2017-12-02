# 0x00 nginx 错误

```
502
upstream sent too big header while reading response header from upstream
```

header头超过默认1k的大小。

```
[http]
fastcgi_buffer_size 128k;
fastcgi_buffers 32 32k;
```

```
warnning
a client request body is buffered to a temporary file 
```
nginx的fastcgi设置的fastcgi_buffers太小，导致将缓存写入磁盘。


```
[http]
client_body_buffer_size 1024k;

```

