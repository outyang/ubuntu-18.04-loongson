this is only some python code to find deb file now.
%%%%%%%%%%%%%%%
pkg.py
find deb file in pwd dir
using: python3 pkg.py pkg1 pkg2 ... pkgn
采用精确匹配
%%%%%%%%%%%%%%%%
pkgex.py
find deb file in pwd dir
using: python3 pkg.py pkg1 pkg2 ... pkgn
采用模糊匹配，建议首先采用第一种

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
首先你需要有个龙芯3a/3b的机器，系统建议loongnix服务器版本（支持docker的其他系统也行，
如果你的系统不支持docker，那么支持debootstrap也行
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
一：安装虚拟机（debian10:buster),建议不要固定大小，并定期备份你的虚拟机
docker版本：
docker run -it debian
(也许需要sudo docker run -it debian)
debootstrap版本：
debootstrap buster debian
(也许需要sudo debootstrap buster debian)
二：更新source-src
docker由于看不见里面的文件，为了方便其见，建议挂载到系统目录下，例如：
docker run -it -v /home/yang/123:/home/yang/123 debian
手动添加source.add里面的源到你的sources.list
例如 cp /etc/apt/sources.list /home/yang/123
编译并保存sources.list
建议apt也用腾讯源

deb http://mirrors.cloud.tencent.com/debian buster main contrib non-free

完成上述步骤后
apt update
如果有错误，请先解决错误，如果解决不了，可以联系我：406959526，QQ


建议docker容器commit新的容器名,例如：
docker commit $id u18
后续载入新的虚拟容器：
docker run -it -v /home/yang/123:/home/yang/123 u18
三：预备工作
docker版本:
cd /home/yang/123
mkdir u18
cd u18
debootstrap版本：
chroot debian
mkdir /home/yang/123
cd /home/yang/123
mkdir u18
cd u18
四：正式开始
在u18目录下新建一个文件run.list
打开run.list,每一行不要用空格和特殊符合，一行一行手动录入需要编译的包，一行只有一个包名，包名必须正确
下载或在编辑zidong.sh:
https://github.com/outyang/ubuntu-18.04-loongson.git
运行
sh zidong.sh
编译开始了
五：存在的bug和注意事项
部分包编译失败，自动脚本不自动停下
自动脚本执行完成可能锁死虚拟机，请直接关闭虚拟机
六：如果确定需要编译的包，怎么分配任务
建议自己决定需要编译的包
在初始的docker镜像里面运行apt install pkg_name,然后取消
然后就会有自己要安装包的依赖(这个依赖不是完整的，ubuntu和debian的包不是完全相同的）
将这些list复制粘贴到run.list并按照步骤四的要求保存
sh zudong.sh

不要删除编译后产生的文件，源码文件夹可以删除，那些文件在发布镜像的时候应该有用到


文档有错误，脚本有错误，要参与项目的都可以联系我
本文档和项目会持续更新，谢谢大家的支持和参与
