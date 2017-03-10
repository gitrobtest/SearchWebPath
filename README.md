# SearchWebPath

### Function
根据网站URL(http://www.xxx.com/a/b/c?id=1)
判断出URL所在的网站物理路径地址(c:/web/cms/a/b/c).

应用场景：利用漏洞可以执行系统命令，然而并不知道网站物理路径，此时可上传此脚本跑出网站物理路径，写入一句话木马。

### Usage

#### python源码文件
```bash
python searchweburl.py -p "./" -u "http://www.xxx.com/a/b/c/d?id=1"
```

#### windows绿色版
```bash
searchweburl.exe -p "./" -u "http://www.xxx.com/a/b/c/d?id=1"
```

#### linux绿色版
```bash
./searchweburl -p "./" -u "http://www.xxx.com/a/b/c/d?id=1"
```

### Parameter

* -p --path　　　　待检测的磁盘路径
* -u --url　　　　 待检测的网站url
* -h --help　　　　帮助信息


### 详情参考博客：[SearchWebPath](http://thief.one)
<hr>
By nMask

@2017.03.10



