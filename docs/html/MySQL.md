# MySQL

## 一、数据库概述

数据库的本质其实就是一款基于网络通信的程序，用于持久化数据，可以理解为存储数据的“仓库”，它保存了一系列有组织的数据。以实现结构化查询，方便管理。

### 1 数据库相关概念

DB：数据库，保存一组有组织的数据的容器

DBMS：数据库管理系统，又称为数据库软件（产品），用于管理DB中的数据

SQL：结构化查询语言，用于和DBMS通信的语言

SQL 的优点：

- 不是某个特定数据库供应商专有的语言，几乎所有 DBMS 都支持 SQL 。
- 简单易学。
- 虽然简单，但实际上是一种强有力的语言，灵活使用其语言元素，可以进行非常复杂和高级的数据库操作。

### 2 数据库存储数据的特点

将数据放到表中，表再放到库中一个数据库中可以有多个表，每个表都有一个的名字，用来标识自己。表名具有唯一性。 表具有一些特性，这些特性定义了数据在表中如何存储，类似java中 “类”的设计。 表由列组成，我们也称为字段。所有表都是由一个或多个列组成的，每一列类似java 中的”属性” 表中的数据是按行存储的，每一行类似于java中的“对象”。

### 3 数据库的分类

关系型数据库：数据之间彼此有关系或者约束，通常以表格的形式存储

- MySQL
- oracle
- db2
- access
- sql server

非关系型数据库：通常是kv形式存储数据，比如mongodb使用bson格式

- redis
- mongodb
- memcache

## 二、MySQL介绍和安装

### 1 介绍

MySQL 数据库隶属于 MySQL AB 公司，总部位于瑞典，后被 Oracle 收购。

官方网站：https://www.mysql.com/

### 2 优点

- 成本低：开放源代码，一般可以免费使用。
- 性能高：执行很快。
- 简单：很容易安装和使用。

### 3 MySQL的版本

- 社区版（免费）
- 企业版（收费）

作为学习使用社区版即可。

### 4 MySQL的安装

#### 4.1 windows安装

访问[该页面](https://dev.mysql.com/downloads/mysql/)，选择windows 5.7版本下载，如图：



下载完成后解压，进入到`bin`目录下启动`mysqld.exe`即开启服务。

#### 4.2 linux安装

以CentOS7安装mysql5.7为例，通过yum安装。

CentOS 7的yum源中默认没有mysql，要先下载mysql的repo源，[点击这里](https://dev.mysql.com/downloads/repo/yum/)获取，如图：



复制下载链接。

```
BASHrpm -ivh https://dev.mysql.com/get/mysql80-community-release-el7-5.noarch.rpm
```

我们可以通过以下方法检测是否已经成功安装了yum源：

```
BASH[root@control-plane ~]# yum repolist enabled | grep "mysql.*-community.*"
mysql-connectors-community/x86_64 MySQL Connectors Community                 230
mysql-tools-community/x86_64      MySQL Tools Community                      138
mysql80-community/x86_64          MySQL 8.0 Community Server                 321
```

当你使用此方法进行安装MySQL的时候，可以看到会默认安装mysql的最新稳定版本（MySQL 8.0 Community Server），如果想要安装以前的版本，比如5.7，需要进行配置。

首先我们先查看MySQL的哪些源被禁用或者启用了：

```
BASH[root@control-plane ~]# yum repolist all | grep mysql
mysql-cluster-7.5-community/x86_64   MySQL Cluster 7.5 Community    禁用
mysql-cluster-7.5-community-source   MySQL Cluster 7.5 Community -  禁用
mysql-cluster-7.6-community/x86_64   MySQL Cluster 7.6 Community    禁用
mysql-cluster-7.6-community-source   MySQL Cluster 7.6 Community -  禁用
mysql-cluster-8.0-community/x86_64   MySQL Cluster 8.0 Community    禁用
mysql-cluster-8.0-community-source   MySQL Cluster 8.0 Community -  禁用
mysql-connectors-community/x86_64    MySQL Connectors Community     启用:    230
mysql-connectors-community-source    MySQL Connectors Community - S 禁用
mysql-tools-community/x86_64         MySQL Tools Community          启用:    138
mysql-tools-community-source         MySQL Tools Community - Source 禁用
mysql-tools-preview/x86_64           MySQL Tools Preview            禁用
mysql-tools-preview-source           MySQL Tools Preview - Source   禁用
mysql57-community/x86_64             MySQL 5.7 Community Server     禁用
mysql57-community-source             MySQL 5.7 Community Server - S 禁用
mysql80-community/x86_64             MySQL 8.0 Community Server     启用:    321
mysql80-community-source             MySQL 8.0 Community Server - S 禁用
```

看到现在启用的是8.0版本系列的。我们需要安装的是5.x系列的。那么我们就可以执行以下命令：

```
BASHyum-config-manager --disable mysql80-community  #禁用8.0版本
yum-config-manager --enable mysql57-community　　#启用5.7版本（需要哪个就启用哪个）　
```

> 上面的命令执行如果提示：`-bash: yum-config-manager: 未找到命令　`
>
> 那么我们就需要安装执行以下命令来安装一个包：`yum install -y yum-utils` 执行成功之后继续执行上面的命令。

再次查看：

```
BASH[root@control-plane ~]# yum repolist enabled | grep "mysql.*-community.*"
mysql-connectors-community/x86_64 MySQL Connectors Community                 230
mysql-tools-community/x86_64      MySQL Tools Community                      138
mysql57-community/x86_64          MySQL 5.7 Community Server                 564
```

变为5.7版本，就可以开始安装mysql了。　　

```
BASHyum install -y mysql-community-server
```

启动mysql服务：

```
BASHsystemctl start mysqld  # 启动服务
systemctl status mysqld # 查看服务状态
```

如果是MySQL5.7版本以前，安装后的默认密码为空，直接回车即可进入。MySQL5.7会在安装后为root用户生成一个随机临时密码。但无论你安装的MySQL是哪个版本，无论使用哪种方式安装，无论是否需要密码登录，始终记住数据库的安全大于一切，所以请设置密码。

本次安装的MySQL没有设置密码，但系统赋予了默认的且临时的密码，如果是第一次安装且没有重复重启服务，打开mysql默认日志文件`/var/log/mysqld.log`，可以查看：

```
BASH# 搜索临时密码，在日志文件中定位
grep 'temporary password' /var/log/mysqld.log
```

拿到密码后可以进行登录：

```
BASHmysql -uroot -p
Enter password:P&runEFZ_9E<
```

#### 4.3 docker安装

以mysql5.7为例，可以前往docker hub上搜索官方镜像：

```
BASHdocker pull mysql:5.7  # 如果不指定tag，默认是latest
```

创建容器：

```
BASHdocker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7
# MYSQL_ROOT_PASSWORD：root密码
```

如果要建立目录映射的mysql容器：

```
BASHdocker run -p 3306:3306 --name mysql \
-v /usr/local/docker/mysql/conf:/etc/mysql \
-v /usr/local/docker/mysql/logs:/var/log/mysql \
-v /usr/local/docker/mysql/data:/var/lib/mysql \
-e MYSQL_ROOT_PASSWORD=123456 \
-d mysql:5.7
```

创建完成后，可以通过远程连接到该机器的3306端口。

### 5 MySQL的卸载

#### 5.1 windows卸载

windows的卸载不难，请自己上网搜索。

#### 5.2 linux卸载

首先查询系统是否安装了mysql

```
BASHrpm -qa | grep -i mysql
```



查看MySQL服务状态：

```
BASHsystemctl status mysqld
```

如果MySQL服务正在运行，停止MySQL服务

```
BASHsystemctl stop mysqld
```

卸载查询出来的这些组件：

```
BASHmysql-community-common-5.7.37-1.el7.x86_64
mysql-community-client-5.7.37-1.el7.x86_64
mysql-community-server-5.7.37-1.el7.x86_64
mysql80-community-release-el7-5.noarch
mysql-community-libs-5.7.37-1.el7.x86_64
mysql-community-libs-compat-5.7.37-1.el7.x86_64
```

命令：

```
BASHrpm -e --nodeps mysql-community-libs-compat-5.7.37-1.el7.x86_64
# 通过该命令删除所有组件
```

和Windows系统一样，MySQL的卸载不仅仅是卸载程序，也需要删除与程序相关的文件夹。才能保证卸载的完整性。

查看MySQL对应的文件夹

```
BASHfind / -name mysql
# 或者
whereis mysql
```

将查找出来的mysql目录`rm -rf`即可。

```
BASHrm -rf  /usr/lib64/mysql
rm -rf  /usr/share/mysql
```

删除MySQL配置文件

```
BASHrm -rf /etc/my.cnf
rm -rf /etc/init.d/mysqld
```

删除mysql用户及用户组

```
BASHid mysql # 查看MySQL用户及用户组
userdel mysql
```

完成。

#### 5.3 docker卸载

docker卸载很简单，首先查看容器id：

```
BASHdocker ps
```

删除该容器

```
BASHdocker stop containerID
docker rm containerID
```

如果挂载了数据卷，删除对应的目录即可完成卸载。

### 6 修改密码

如果是docker安装，在创建容器的时候就可以指定密码。而windows和linux需要修改密码，在终端中输入命令

```
BASHmysqladmin -u用户名 -p password 新密码
# # 其中 username 为要修改密码的用户名，newpwd 为要修改的新密码，比如
mysqladmin -uroot -p password 123456
```

> 如果修改时提示：`ERROR 1819 (HY000): Your password does not satisfy the current policy requirements`，说明新密码比较简单，不符合密码策略。
>
> 可以先将原来的临时密码修改一位，把新密码暂时设置上。比如这样：
>
> ```
> BASHmysqladmin -uroot -p password runEFZ_9E
> ```
>
> 修改完成后，登录进入mysql，查看查看mysql初始的密码策略
>
> ```
> BASHmysql> SHOW VARIABLES LIKE 'validate_password%';
> +--------------------------------------+--------+
> | Variable_name                        | Value  |
> +--------------------------------------+--------+
> | validate_password_check_user_name    | OFF    |
> | validate_password_dictionary_file    |        |
> | validate_password_length             | 8      |
> | validate_password_mixed_case_count   | 1      |
> | validate_password_number_count       | 1      |
> | validate_password_policy             | MEDIUM |
> | validate_password_special_char_count | 1      |
> +--------------------------------------+--------+
> 7 rows in set (0.00 sec)
> ```
>
> 关于 mysql 密码策略相关参数；
>
> - `validate_password_length`固定密码的总长度，默认为8位
>
> - `validate_password_dictionary_file`指定密码验证的文件路径，默认为空
>
> - `validate_password_mixed_case_count`整个密码中至少要包含大/小写字母的总个数，默认为1
>
> - `validate_password_number_count`整个密码中至少要包含阿拉伯数字的个数，默认为1
>
> - `validate_password_policy`指定密码的强度验证等级，默认为`MEDIUM`
>
> - 关于
>
>   ```
>   validate_password_policy
>   ```
>
>   的取值：
>
>   - `0/LOW`：只验证长度
>   - `1/MEDIUM`：验证长度、数字、大小写、特殊字符
>   - `2/STRONG`：验证长度、数字、大小写、特殊字符、字典文件
>
> - `validate_password_special_char_count`整个密码中至少要包含特殊字符的个数，默认为1
>
> 如果需要修改密码策略，使用如下命令：
>
> ```
> BASHmysql> set global validate_password_length=6;  # 设置密码的总长度为6位
> mysql> set global validate_password_policy=LOW;  # 设置密码的强度验证等级为LOW
> ```
>
> 现在可以为mysql设置简单密码了，只要满足六位的长度即可。但是在生产环境下，不要这么做，尽量使用高强度密码。
>
> 介绍另一种修改密码的方式，在登录进入mysql命令行的情况下：
>
> ```
> BASH# MySQL版本5.7.6版本以前用户可以使用如下命令：
> mysql> SET PASSWORD = PASSWORD('123456'); 
> # MySQL版本5.7.6版本开始的用户可以使用如下命令：
> mysql> ALTER USER USER() IDENTIFIED BY '123456';
> 
> # 如果不清楚自己是什么版本，可以将两条都尝试一下。
> ```

现在，退出重新登录测试一下：

```
BASHmysql -uroot -p123456
```

> 如果上面的方式不能修改可以使用下面安全模式修改root密码：
>
> 打开`/etc/my.cnf`文件，加上一行
>
> ```
> BASHskip-grant-tables
> # 表示跳过安全检查（即登录时无需密码）
> ```
>
> 重启服务：
>
> ```
> BASHsystemctl restart mysqld
> ```
>
> 直接登录即可登录成功：
>
> ```
> BASHmysql -uroot
> ```
>
> 登陆后，切换到mysql库
>
> ```
> BASHmysql> use mysql
> Database changed
> ```
>
> 查看表结构
>
> ```
> BASHmysql> desc user;
> ```
>
> 需要注意的是5.7以上版本已经没有了`Password`字段，取而代之的是`authentication_string`字段。
>
> 修改密码：
>
> ```
> BASHmysql> update user set authentication_string='密码' where User='root' and host='localhost';  # 5.7及以上
> mysql> update user set Password='密码' where User='root' and host='localhost'; # 5.6及以下
> mysql> FLUSH PRIVILEGES；
> ```
>
> 修改成功后，要删掉刚刚配置文件中添加的`skip-grant-tables`，否则谁都可以登录了。
>
> 删除之后，再次重启服务
>
> ```
> BASHsystemctl restart mysqld
> ```
>
> 完成。

### 7 MySQL服务的登录和退出

在安装了mysql的客户端的电脑上，通过命令行方式连接数据库：

```
BASHmysql -h主机名 -P端口号 -u用户名 -p密码
# 如果连接本地，主机名和端口可以不写，比如：
mysql -uroot -p
# -p后面可以不写密码，而是根据提示输入密码，这样输入的密码是不可见的
```

还可以通过各种各样的工具来连接mysql，比如Navicat（下载和安装自行上网搜索）：



## 三、基本使用

### 1 MySQL的常见命令

```
BASH# 1.查看当前所有的数据库
show databases;
# 2.切换到指定的库
use 库名
# 3.查看当前库的所有表
show tables;
# 4.查看其它库的所有表
show tables from 库名;
# 5.查看表结构
desc 表名;
# 6.查看服务器的版本
# 方式一：登录到mysql服务端
select version();
# 方式二：没有登录到mysql服务端，在bash窗口下
mysql --version
# 或
mysql --V
# 7.退出
exit
#或者
quit
# 8.查看当前mysql服务端的一些信息，比如编码、连接方式、当前用户等
\s
```

### 2 MySQL的语法规范

- 不区分大小写，但建议关键字大写，表名、列名小写。
- 每条命令用分号结尾
- 每条命令根据需要，可以进行缩进或换行
- 注释
  - 单行注释：`#`
  - 多行注释：`/* */`

### 3 SQL的语言分类

- DML（Data Manipulation Language）：数据操作语言，用于添加、删除、修改、查询数据库记录，并检查数据完整性。
- DDL（Data Definition Language）：数据定义语言，用于库和表的创建、修改、删除。
- DCL（Data Control Language）：数据控制语言，用于定义用户的访问权限和安全级别。
- DQL（Data Query Language）：数据查询语言
- TCL（Transaction Control Language）：事务控制语言

### 4 mysql的配置文件

首先先看看你的mysql在哪，通过which命令

```
BASHwhich mysql
```

显示出目录比如我的是下面这个

```
TEXT/usr/bin/mysql
```

接下来就可以针对这个目录通过命令查看配置文件在哪了：

```
BASH# 查看 mysql 配置文件加载顺序
/usr/bin/mysql --verbose --help | grep -A 1 'Default options'
```

然后在下面会出现一些信息，比如：

```
BASHDefault options are read from the following files in the given order:
/etc/my.cnf /etc/mysql/my.cnf ~/.my.cnf
# 这个信息的意思是：
# 服务器首先读取的是 /etc/my.cnf 文件，如果前一个文件不存在则继续读 /etc/mysql/my.cnf 文件，依此类推，如若还不存在便会去读~/.my.cnf文件。
```

一般来说，mysql配置文件在Windows下叫`my.ini`或者`my-default.ini`，它保存在MySQL的数据目录下，可以通过命令行登录mysql，输入命令查看：

```
BASHselect @@basedir;  # 查看安装目录的路径
select @@datadir;  # 查看数据文件的存放目录
```

配置文件都在数据目录下存放。

在Linux下叫`my.cnf`，该文件一般位于`/etc/my.cnf`，可以通过以下命令查找：

```
BASHfind / -name my.cnf
```

如果以上文件都不存在，则说明在对mysql编译完成之后你没有对mysql进行配置，需要你自己复制一份mysql提供的默认配置文件到`/etc`目录中，然后改名为`my.cnf`，修改文件的属组和属组并赋予执行权限。

配置文件的内容：

```
BASH[client] # 客户端默认的连接参数
# socket=MYSQL
port=3306 # 客户端连接服务器端时使用的端口号，默认的端口号为 3306
default-character-set=utf8  # 默认编码
[mysql]  # 客户端启动立刻加载下面的配置
no-beep  # 发生错误时不要发出蜂鸣声
default-character-set=utf8  # 客户端默认编码
[mysqld] # 服务端启动立刻加载下面的配置
port=3306 # 表示 MySQL 服务器的端口号
character_set_server=utf8  #服务端默认编码（数据库级别）
# basedir="C:/Program Files/MySQL/MySQL Server 5.7/"  # 表示 MySQL 的安装路径
datadir=C:/ProgramData/MySQL/MySQL Server 5.7/Data  # 表示 MySQL 数据文件的存储位置，也是数据表的存放位置
default-storage-engine=INNODB  # 创建数据表时，默认使用的存储引擎
sql-mode="STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"  # 表示 SQL 模式的参数，通过这个参数可以设置检验 SQL 语句的严格程度
log-output=FILE # 日志选择文件类型
general-log=0  # 是否启用一般查询日志
general_log_file="QCFA-CL6GV5.log"  # 一般查询日志文件的名称。
slow-query-log=1  # 是否启用慢查询日志
slow_query_log_file="QCFA-CL6GV5-slow.log"  # 慢查询日志文件的名称。
long_query_time=10  # 慢查询日志包含执行时间超过long_query_time秒的SQL语句
log-error="QCFA-CL6GV5.err"  # 错误记录。
server-id=1  #服务器ID。
lower_case_table_names=1
secure-file-priv="C:/ProgramData/MySQL/MySQL Server 5.7/Uploads"
max_connections=151  # 表示允许同时访问 MySQL 服务器的最大连接数。其中一个连接是保留的，留给管理员专用的
table_open_cache=2000  # 表示所有进程打开表的总数
tmp_table_size=81M  # 表示内存中每个临时表允许的最大大小
thread_cache_size=10  # 表示缓存的最大线程数
myisam_max_sort_file_size=100G  # 表示 MySQL 重建索引时所允许的最大临时文件的大小
myisam_sort_buffer_size=152M  # 表示重建索引时的缓存大小
key_buffer_size=8M  # 表示关键词的缓存大小
read_buffer_size=64K  # 表示 MyISAM 表全表扫描的缓存大小
read_rnd_buffer_size=256K  # 表示将排序好的数据存入该缓存中
innodb_flush_log_at_trx_commit=1 #每次commit 日志缓存中的数据刷到磁盘中。通常设置为 1，意味着在事务提交前“日志已被写入磁盘”， 事务可以运行更长以及服务崩溃后的修复能力。如果你愿意减弱这个安全，或你运行的是比较小的事务处理，可以将它设置为 0 ，以减少写日志文件的磁盘 I/O。
innodb_log_buffer_size=1M # InnoDB 将日志写入日志磁盘文件前的缓冲大小。理想值为 1M 至 8M。大的日志缓冲允许事务运行时不需要将日志保存入磁盘而只到事务被提交(commit)。因此，如果有大的事务处理，设置大的日志缓冲可以减少磁盘I/O。
innodb_buffer_pool_size=8M #InnoDB 用来高速缓冲数据和索引内存缓冲大小。 更大的设置可以使访问数据时减少磁盘 I/O。
innodb_log_file_size=48M #日志组中的每个日志文件的大小(单位 MB)。可以减少刷新缓冲池的次数，从而减少磁盘 I/O。但是大的日志文件意味着在崩溃时需要更长的时间来恢复数据。
innodb_thread_concurrency=25 # InnoDB尝试将InnoDB内并发的操作系统线程数小于或等于此变量给出的限制（InnoDB使用操作系统线程来处理用户事务）。一旦线程数达到此限制，就会在“先进先出”（FIFO）队列中将其他线程置于等待状态以供执行。等待锁的线程不计入并发执行线程的数量。
innodb_autoextend_increment=64 # 增量大小（以MB为单位），用于在自动扩展的InnoDB系统表空间文件变满时扩展其大小。
innodb_buffer_pool_instances=8 #InnoDB缓冲池分区的区域数。对于具有数千兆字节范围的缓冲池的系统，将缓冲池划分为单独的实例可以提高并发性，通过减少争用，因为不同的线程读写缓存页面。
innodb_concurrency_tickets=5000 #确定可以同时进入InnoDB的线程数。
innodb_old_blocks_time=1000 #指定插入旧子列表的块在第一次访问后必须保留的长度（以毫秒为单位），然后才能将其移动到新的子列表。
innodb_open_files=300 # 它指定MySQL可以一次打开的最大.ibd文件数。最小值为10。
innodb_stats_on_metadata=0 # 启用此变量后，InnoDB会在元数据语句期间更新统计信息。
innodb_file_per_table=1 # 当启用时，InnoDB会为每个新创建的表存储数据和索引.在单独的.ibd文件中，而不是在系统表空间中。
innodb_checksum_algorithm=0 #指定如何生成和验证存储在InnoDB表空间的磁盘块中的校验和。使用以下值列表：0表示crc32,1表示strict_crc32，2表示innodb，3表示strict_innodb，4表示无，5表示strict_none。
back_log=80  # back_log参数的值指出在MySQL暂时停止响应新请求之前的短时间内多少个请求可以被存在堆栈中。
flush_time=0  # 如果将此值设置为非零值，则每个flush_time秒都会关闭所有表以释放资源。将未刷新的数据同步到磁盘。此选项最适用于资源最少的系统。
join_buffer_size=256K # 用于普通索引扫描，范围索引扫描和不使用的连接的缓冲区的最小大小索引，从而执行全表扫描。
max_allowed_packet=4M  # 一个数据包或任何生成/中间字符串的最大大小
max_connect_errors=100 # 如果来自主机的多个连续连接请求在没有成功连接的情况下中断，则服务器会阻止该主机执行进一步的连接。
open_files_limit=4161  # #更改mysqld可用的文件描述符的数量。如果mysqld为您提供错误“打开太多文件”，则应尝试增加此选项的值。
sort_buffer_size=256K  # 表示用于排序的缓存大小
table_definition_cache=1400  #可以存储在定义高速缓存中的表定义（来自.frm文件）的数量。如果使用大量表，则可以创建大型表定义高速缓存以加快表的打开。表定义高速缓存占用较少与普通表缓存不同，它不使用文件描述符。
binlog_row_event_max_size=8K  # 指定基于行的二进制日志事件的最大大小（以字节为单位）。如果可能，将行分组为小于此大小的事件。该值应为256的倍数。
sync_master_info=10000  # #如果此变量的值大于0，则复制从站将其master.info文件同步到磁盘。
sync_relay_log=10000  #如果此变量的值大于0，则MySQL服务器将其中继日志同步到磁盘
sync_relay_log_info=10000  #如果此变量的值大于0，则复制从站将其relay-log.info文件同步到磁盘
```

以上内容根据自己的需要对配置文件进行配置，一般来说除了字符集更改一下之外，其它的可以保持默认，以后有需求再更改。注意修改配置文件后一定要重启服务才能生效。

## 四、DDL

DDL主要是库和表的管理。

### 1 库的基本操作

#### 1.1 增

```
SQL# 简单语法：创建数据库
CREATE DATABASE 数据库名;
# 完整语法：创建数据库，指定它的默认字符集和排序规则，如果已存在则不创建
CREATE DATABASE [IF NOT EXISTS] 数据库名 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
# 示例：
CREATE DATABASE Books;
```

#### 1.2 查

```
SQLSHOW DATABASES;  # 查看所有数据库
SELECT DATABASE();  # 查看当前所在的库的名字
USE dbname;  # 切换到指定库下 
```

#### 1.3 改

对于数据库名一般不更改，要修改数据库名可以先删除数据库，再创建新的数据库。

更改数据库的字符集和排序规则：

```
SQLALTER DATABASE 数据库名 CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```

#### 1.4 删

```
SQLDROP DATABASE [IF EXISTS] 数据库名;
# 示例：
DROP DATABASE IF EXISTS Books;
```

### 2 表的基本操作

#### 2.1 增

```
SQLCREATE TABLE 表名(
	列名1 列的类型[长度] [列的约束],
    列名2 列的类型[长度] [列的约束],
    ……
    列名n 列的类型[长度] [列的约束]
);

# 示例
CREATE TABLE student ( 
	id INT primary KEY auto_increment, 
	`name` VARCHAR(255)
);
```

#### 2.2 查

```
SQLSHOW TABLES;  # 查看当前库下面所有的表名
DESC tablename  # 查看某个表结构
```

#### 2.3 改

```
SQLALTER TABLE 表名 add|drop|modify|change column 列名 [列类型 约束];
# 示例：
# 修改列名
ALTER TABLE student CHANGE COLUMN `name` stu_name VARCHAR ( 255 );
# 修改列的类型或约束
ALTER TABLE student MODIFY COLUMN `stu_name` VARCHAR ( 32 );
# 添加新列
ALTER TABLE student ADD COLUMN `salary` DOUBLE;
# 删除列
ALTER TABLE student DROP COLUMN `salary`;
# 修改表名
ALTER TABLE student RENAME TO `new_student`;
```

#### 2.4 删

```
SQLDROP TABLE IF EXISTS 表名;
# 示例：
DROP TABLE IF EXISTS `student`;
```

#### 2.5 复制表

仅复制表结构，不复制数据

```
SQL# 仅复制表的结构
CREATE TABLE 要复制的表名 LIKE 原表名;
# 示例
CREATE TABLE admin_back LIKE admin;
```

复制表的结构和数据：

```
SQL# 复制表的结构和数据：
CREATE TABLE 要复制的表名 SELECT * FROM 原表名;
# 示例
CREATE TABLE admin_back SELECT * FROM admin;
# 本质就是利用子查询，因此可以做到复制部分数据或者结构，比如：
CREATE TABLE admin_back SELECT * FROM admin WHERE nation="中国";
```

### 3 数据类型和约束

#### 3.1 数据类型

创建表的语法中，字段的数据类型主要有以下几种。

- 数值型：整型、小数（定点数、浮点数）
- 字符型：较短的文本（char、varchar）、较长的文本（text、longtext、blob）
- 日期型：date、datetime、timestamp、time、year

数值类型：

- 如果不设置无符号还是有符号，默认都是有符号的。如果需要设置无符号，需要添加`unsigned`关键字。
- 如果插入的数值超过了整型的范围，MySQL 会报（Out of range for column …）异常。
- 如果不设置长度，会有默认的长度。



字符类型：

- char是定长的，可能会浪费空间，但是存取简单；varchar是变长的，节省空间，但是存取稍微麻烦一点。
- varchar最多能存储65535个字节的数据，一般我们最多定义varchar(255)，超过255会被转成text类型



时间类型：

| 类型名称  | 说明                                                         |
| --------- | ------------------------------------------------------------ |
| year      | YYYY 1901~2155                                               |
| time      | HH:MM:SS -838:59:59~838:59:59                                |
| date      | YYYY-MM-DD 1000-01-01~9999-12-3                              |
| datetime  | YYYY-MM-DD HH:MM:SS 1000-01-01 00:00:00~ 9999-12-31 23:59:59 |
| timestamp | YYYY-MM-DD HH:MM:SS 19700101 00:00:01 UTC~2038-01-19 03:14:07UTC |

#### 3.2 约束

为了保证数据的一致性和完整性，SQL 规范以约束的方式对表数据进行额外的条件限制。约束是表级的强制规定。可以在创建表的时候添加约束，或者在表创建之后数据添加之前添加约束。

有如下的六大约束：

- NOT NULL，非空约束，规定某个字段不能为空。
- UNIQUE，唯一约束，规定某个字段在整个表中是唯一的。
- PRIMARY KEY，主键，非空且唯一。
- CHECK，检查约束。
- DEFAULT，默认值。
- FOREIGN KEY，外键。

根据约束的作用范围，约束可以分为：

- 列级约束：只能作用在一个列上，并且是根据列的定义后面。六大约束语法上支持，但是外键约束没有效果。
- 表级约束：可以作用在多个列上，不和列在一起，而是单独定义。除了非空、默认约束，其他约束都支持。

```
SQLCREATE TABLE 表名(
	列名 字段类型 列级约束,
    列名 字段类型 列级约束,
    表级约束(列名1,列名2)
);

# 示例：创建表的时候添加列级约束
CREATE TABLE stu_info (
	id INT PRIMARY KEY,# 主键
	stu_name VARCHAR ( 255 ) NOT NULL,# 非空
	gender CHAR ( 1 ) CHECK (
	gender IN ( '男', '女' )),# 检查约束
	seat INT UNIQUE,# 唯一约束
	age INT DEFAULT 18 # 默认约束
);
# 创建表的时候添加表级约束
CREATE TABLE major ( 
	id INT PRIMARY KEY, 
	`name` VARCHAR ( 255 ) 
);
```

在修改表时也可以添加约束，语法：

```
SQL# 添加列级约束
ALTER TABLE 表名 MODIFY COLUMN 列名 字段类型 新约束;
# 添加表级约束
ALTER TABLE 表名 ADD CONSTRAINT 约束名 约束类型 (字段名) [外键的引用];

# 示例：
# 修改表时添加约束
ALTER TABLE stu_info MODIFY COLUMN id INT PRIMARY KEY; 
ALTER TABLE stu_info MODIFY COLUMN age INT DEFAULT 18; 
ALTER TABLE stu_info ADD CONSTRAINT fk_major_id FOREIGN KEY (major_id) REFERENCES major(id);
# 修改表时删除非空约束
ALTER TABLE stu_info MODIFY COLUMN stu_name  VARCHAR(255) ;
# 修改表时删除默认约束
ALTER TABLE stu_info MODIFY COLUMN age INT;
# 修改表时删除主键
ALTER TABLE stu_info DROP PRIMARY KEY;
# 修改表时删除主键
# 查询唯一键 show index from stu_info
ALTER TABLE stu_info DROP INDEX seat;
# 修改表时删除外键
ALTER TABLE stu_info DROP FOREIGN KEY fk_marjor_id;
```

#### 3.3 主键和唯一的区别

|      | 保证唯一性 | 是否允许为空 | 一个表中可以有多少个 | 是否允许组合  |
| ---- | ---------- | ------------ | -------------------- | ------------- |
| 主键 | √          | ×            | 最多有1个            | √，但是不推荐 |
| 唯一 | √          | √            | 可以有多个           | √，但是不推荐 |

#### 3.4 外键的特点

- 外键的设置：
  - 一对一关系，外键字段建在哪里都可以，但是推荐你建在查询频率较高的一方
  - 一对多关系，外键字段建在多的那方
  - 多对多关系，需要建立第三张表
- 要求从表的外键列的类型要和主表的关联列的类型要求一致或兼容，但是名称不要求一致。
- 主表的关联列必须是一个 key（一般是主键或唯一键）。
- 在删除时，先删除从表，再删除主表（可以设置级联删除）

### 4 标识列

标识列又称为自增长列，可以不用手动插入值，系统提供默认的序列值。特点如下：

- 标识列必须不一定和主键搭配，但是要求是一个 key。
- 一个表中至多有一个标识列。
- 标识列的类型只能是数值型。
- 标识列可以通过 `set auto_increment_increment = 3;` 设置步长，也可以通过手动插入值的方式设置标识列的起始值 `INSERT INTO student(id,name) VALUES (5,'xxx')` 。

示例，创建表的时候设置标识列：

```
SQLCREATE TABLE student ( 
	id INT PRIMARY KEY auto_increment,  # 设置id自增
	`name` VARCHAR ( 255 ) 
);
# 新增数据
INSERT INTO student(`name`) VALUES ('xxx'); # 在插入的时候不需要指定主键id
```

也可以修改表时设置标识列

```
SQLCREATE TABLE student ( 
	id INT PRIMARY KEY ,  # 创建时不设置自增
	`name` VARCHAR ( 255 ) 
);
# 修改表的时候设置标识列
ALTER TABLE student MODIFY COLUMN id PRIMARY KEY auto_increment; # 设置id自增
# 新增数据
INSERT INTO student(`name`) VALUES ('xxx'); # # 在插入的时候不需要指定主键id
```

删除标识列，比如删除自增：

```
SQL# 创建表的时候设置标识列
CREATE TABLE student ( 
  id INT PRIMARY KEY auto_increment, 
  `name` VARCHAR ( 255 ) 
);
# 修改表时删除标识列
ALTER TABLE student MODIFY COLUMN id PRIMARY KEY;
```

### 5 一对多表关系的创建

示例：

```
SQL# 学生表和班级表是一对多关系，外键在学生表建立
CREATE TABLE class(
	id int PRIMARY KEY auto_increment,
	NAME VARCHAR(255)
);

CREATE TABLE student ( 
	id INT PRIMARY KEY auto_increment, 
	name VARCHAR ( 255 ) ,
    class_id INT,
    FOREIGN KEY(class_id) REFERENCES class(id)
);
```

注意：

- 先创建从表，再创建主表
- 录入数据时，先录入从表，再录入主表
- 删除数据时，先删除从表，再删除主表

这种操作方式比较费力，可以设置级联更新和级联删除。如下：

```
SQL# 学生表和班级表是一对多关系，外键在学生表建立
CREATE TABLE class(
	id int PRIMARY KEY auto_increment,
	NAME VARCHAR(255)
);

CREATE TABLE student ( 
	id INT PRIMARY KEY auto_increment, 
	name VARCHAR ( 255 ) ,
    class_id INT,
    # cascade 级联操作，设置级联更新和级联删除
    FOREIGN KEY(class_id) REFERENCES class(id) ON UPDATE CASCADE ON DELETE CASCADE
);
```

### 6 多对多表关系创建

示例：

```
SQL# 学生表和老师表是多对多关系，在第三张表创建关系
CREATE TABLE student(
	id int PRIMARY KEY auto_increment,
	NAME VARCHAR(255)
);

CREATE TABLE teacher(
	id int PRIMARY KEY auto_increment,
	NAME VARCHAR(255)
);

CREATE TABLE student2teacher(
	id int PRIMARY KEY auto_increment,
	teacher_id INT,
    student_id INT,
    FOREIGN KEY(teacher_id) REFERENCES teacher(id)
    ON UPDATE CASCADE 
    ON DELETE CASCADE,
    FOREIGN KEY(student_id) REFERENCES student(id)
    ON UPDATE CASCADE 
    ON DELETE CASCADE
);
```

### 7 一对一表关系创建

示例：

```
SQL# 学生表和学生信息是一对一关系，外键在哪张表都可以创建，可以创建在查询频率高的表上
CREATE TABLE student(
	id int PRIMARY KEY auto_increment,
	NAME VARCHAR(255),
	details_id INT,
	FOREIGN KEY(details_id) REFERENCES student_details(id) 
	ON UPDATE CASCADE
	ON DELETE CASCADE
);

CREATE TABLE student_details(
	id int PRIMARY KEY auto_increment,
	telephone INT,
  address VARCHAR(255)
);
```

## 五、DQL

数据查询语言DQL基本结构是由SELECT子句，FROM子句，WHERE子句组成的查询块。要查询的东西可以是常量值、表达式、字段、函数等。

### 1 基础查询

语法：

```
SQLSELECT 查询列表
FROM 表名;
```

示例：

```
SQL# 查询表中的单个字段 
SELECT last_name FROM employees;

# 查询表中的多个字段
SELECT
	last_name,
	salary,
	email 
FROM
	employees;

# 查询表中的所有字段（当数据量大的时候，不建议使用）
SELECT * FROM employees;

# 查询常量值
SELECT 100;
SELECT 'john';

# 查询表达式
SELECT 100*98;

# 查询函数
SELECT version();

# 起别名
SELECT 100 as '常量值';
SELECT
	first_name AS '姓',
	last_name AS '名' 
FROM
	employees;

# DISTINCT去重，查询员工表中的所有部门编号
SELECT DISTINCT
	department_id as '部门编号'
FROM
	employees;

# 查询员工名和姓连接成一个字段，并显示为姓名，使用CONCAT
SELECT
	CONCAT( last_name, first_name ) AS '姓名' 
FROM
	employees;
```

### 2 条件查询

语法：

```
SQLSELECT 查询列表
FROM 表名
WHERE 条件表达式;
```

分类：

- 按条件表达式筛选：条件运算符：`>`、`<`、`=`、`<>`、`!=`、`>=`、`<=`。
- 按逻辑表达式筛选：逻辑运算符：`&&`（`and`）、`||`（`or`）、`!`（`not`）。
- 模糊查询：`like`、`between` `and`、`in`、`is null`、`is not null`。

示例：

```
SQL# 查询员工工资 > 12000 的员工信息 
SELECT
  * 
FROM
  employees 
WHERE
  salary > 12000;

# 查询部门编号不等于 90 号的员工名和部门编号
SELECT
  last_name,
  department_id 
FROM
  employees 
WHERE
  department_id != 90;
  
# 查询工资在 10000 到 20000 之间的员工名、工资以及奖金
SELECT
  last_name AS '员工名',
  salary AS '工资',
  commission_pct AS '奖金' 
FROM
  employees 
WHERE
  salary >= 10000 
  AND salary <= 20000;

# 查询部门编号不是在 90 到 110 之间，或者工资高于 15000 的员工信息
SELECT
  * 
FROM
  employees 
WHERE
  ( department_id < 90 OR department_id > 110 ) 
  OR ( salary > 15000 );

# 查询员工名中包含字符 a 的员工信息，百分号%用来通配任意N个字符，类似于正则表达式中的 .*
SELECT
  * 
FROM
  employees 
WHERE
  last_name LIKE '%a%';

# 查询员工名中第二个字符为 _ 的员工信息
SELECT
  * 
FROM
  employees 
WHERE
  last_name like '_\_%';

# 查询工资在 10000 到 20000 之间的员工名、工资以及奖金
SELECT
  last_name AS '员工名',
  salary AS '工资',
  commission_pct AS '奖金' 
FROM
  employees 
WHERE
  salary BETWEEN 10000 
  AND 20000;

# 查询员工的工种编号是 IT_PROG 、AD_VP 的员工信息
SELECT
  * 
FROM
  employees 
WHERE
  job_id IN ( 'IT_PROG', 'AD_VP' );

# 查询没有奖金的员工信息
SELECT
  * 
FROM
  employees 
WHERE
  commission_pct IS NULL;
```

### 3 排序查询

语法：

```
SQLSELECT 查询列表
FROM 表名
WHERE 条件表达式
ORDER BY 排序列表(字段 [asc],字段 [desc],……);
```

ASC升序，DESC降序。

示例：

```
SQL# 查询员工信息，要求工资从高到低排序
SELECT
  * 
FROM
  employees 
ORDER BY
  salary DESC;

# 查询部门编号 >= 90 的员工信息，按入职时间的先后进行排序
SELECT
  * 
FROM
  employees 
WHERE
  department_id >= 90 
ORDER BY
  hiredate ASC;

# 按年薪的高低显示员工的信息和年薪
SELECT
  *,
  salary * 12 * ( IFNULL( commission_pct, 0 ) + 1 ) AS '年薪' 
FROM
  employees 
ORDER BY
  年薪 ASC;

# 查询员工信息，要求先按工资排序，再按员工编号排序
SELECT
  * 
FROM
  employees 
ORDER BY
  salary,
  employee_id;
```

### 4 常见函数

分类：

- 单行函数：将一个数据进行处理，返回一个值，如 length() 、concat() 等。
- 分组函数：将虚拟表看做一个组，处理一组数据，返回一个值。

#### 4.1 单行函数之字符函数

```
SQL# 获取参数值的字节个数： length(str)
SELECT LENGTH( 'john' ); -- 4 
SELECT LENGTH( '张三丰hahaha' ); -- 15

# 拼接字符串： concat(str1,str2,……)
SELECT
  CONCAT( last_name, '_', first_name ) AS '姓名' 
FROM
  employees;

# 将字符变为大写：upper(str)
SELECT
  UPPER(last_name)
FROM
  employees;

# 将字符变为小写： lower(str)
SELECT
  LOWER( last_name ) 
FROM
  employees;

# 截取字符：substr(str,position,[length])
# 截取从指定索引处后面所有字符
SELECT
  SUBSTR( '李莫愁爱上了陆展元', 7 );
# 截取从指定索引处指定字符长度的字符
SELECT
  SUBSTR( '李莫愁爱上了陆展元', 1,3 );

# 用于返回子串在原字符串中的第一次出现的索引，如果找不到返回0：instr(str,substr)
SELECT
  INSTR( '杨不悔爱上了殷六侠', '殷六侠' );

# 去除左右空格：trim(str)
SELECT
  trim( '           杨不悔爱上了殷六侠           ' );

# 替换： replace(str,from_str,to_str)
SELECT 
REPLACE ( '杨不悔爱上了殷六侠', '爱上了', '怎么可能爱上' );

# 用指定的字符实现左填充指定长度：lpad(str,len,padstr)
SELECT
  LPAD( '杨不悔爱上了殷六侠', 20, '*' );

# 用指定的字符实现右填充指定长度： rpad(str,len,padstr))
SELECT
  RPAD( '杨不悔爱上了殷六侠', 20, '*' );
```

#### 4.2 单行函数之数学函数

```
SQL# 四舍五入：round(x,d)
SELECT
  ROUND(1.65)
SELECT
  ROUND(1.45)
SELECT
  ROUND(1.567,2)

# 向上取整：ceil(x)
SELECT
  CEIL(1.11)
# 向下取整： floor(x)
SELECT
  FLOOR(1.567)

# 截断：truncate(x,d)
SELECT
  TRUNCATE(1.567,2)

# 取余。返回n除以m后的余数，mod(n,m)
SELECT
  MOD(3,1)
```

#### 4.3 单行函数之日期函数

```
SQL# 返回当前系统日期+时间：now()
select NOW();

# 返回当前系统日期：curdate()
select CURDATE()

# 返回当前时间：curtime()
select CURTIME();

# 获取指定的部分，年、月、日、小时、分钟、秒：
SELECT YEAR(NOW());
SELECT MONTH(NOW());
SELECT DAY(NOW());
SELECT HOUR(NOW());
SELECT MINUTE(NOW());
SELECT SECOND(NOW());

# 将日期格式的字符转换成指定格式的日期：str_to_date(str,format)
SELECT STR_TO_DATE('9-13-1999','%m-%d-%y');

# 将日期转换为字符：date_format(date,format)
SELECT DATE_FORMAT(NOW(),'%Y年-%m月-%d日');
```

其中，format为格式化字符，如下：

| 格式字符 | 说明                                           |
| -------- | ---------------------------------------------- |
| %a       | 缩写星期名                                     |
| %b       | 缩写月名                                       |
| %c       | 月，数值                                       |
| %D       | 带有英文前缀的月中的天                         |
| %d       | 月的天，数值(00-31)                            |
| %e       | 月的天，数值(0-31)                             |
| %f       | 微秒                                           |
| %H       | 小时 (00-23)                                   |
| %h       | 小时 (01-12)                                   |
| %I       | 小时 (01-12)                                   |
| %i       | 分钟，数值(00-59)                              |
| %j       | 年的天 (001-366)                               |
| %k       | 小时 (0-23)                                    |
| %l       | 小时 (1-12)                                    |
| %M       | 月名                                           |
| %m       | 月，数值(00-12)                                |
| %p       | AM 或 PM                                       |
| %r       | 时间，12-小时（hh:mm:ss AM 或 PM）             |
| %S       | 秒(00-59)                                      |
| %s       | 秒(00-59)                                      |
| %T       | 时间, 24-小时 (hh:mm:ss)                       |
| %U       | 周 (00-53) 星期日是一周的第一天                |
| %u       | 周 (00-53) 星期一是一周的第一天                |
| %V       | 周 (01-53) 星期日是一周的第一天，与 %X 使用    |
| %v       | 周 (01-53) 星期一是一周的第一天，与 %x 使用    |
| %W       | 星期名                                         |
| %w       | 周的天 （0=星期日, 6=星期六）                  |
| %X       | 年，其中的星期日是周的第一天，4 位，与 %V 使用 |
| %x       | 年，其中的星期一是周的第一天，4 位，与 %v 使用 |
| %Y       | 年，4 位                                       |
| %y       | 年，2 位                                       |

#### 4.4 单行函数之其他函数

```
SQL# 显示当前数据库的版本：version()
SELECT version();

# 显示当前在那个数据库中：database()
SELECT DATABASE ();

# 显示当前登录的用户：user()
SELECT USER();
```

#### 4.5 单行函数之流程控制函数

```
SQL# 类似于 java 中的 switch ... case 语句：
case 要判断的字段或表达式
when 常量1 then 要显示的值1或语句1;
when 常量2 then 要显示的值2或语句2;
……
else 要显示的值n或语句n;
end;

# 类似于 java 中的 if ... else 语句：
case 
when 条件1 then 要显示的值1或语句1
when 条件2 then 要显示的值2或语句2
……
else 要显示的值n或语句n
end;

# 举例
SELECT
  *,
  CASE
    commission_pct 
  WHEN NULL THEN '没有奖金' 
  ELSE '有奖金' 
  END 
FROM
  employees;
```

#### 4.6 分组（聚合）函数

常见的分组函数是：

- avg()：求平均值。
- count()：求总数。
- max()：求最大值。
- min()：求最小值。
- sum()：求和。

特点：

- 一般而言，sum 和 avg 用于处理数值型。max 、min 、count 可以处理任何类型。
- avg 、count 、max 、min 、sum 都忽略 null 值。
- count 函数一般单独使用，一般使用 count(*) 来统计行数。
- 和分组函数一同查询的字段要求是 group by 后的字段。

示例：

```
SQLSELECT
	avg( salary ), -- 平均值
	count(*),  -- 总数
	MAX( salary ), -- 最大值
	MIN( salary ),　-- 最小值
	sum( salary )  -- 求和
FROM
	employees;
```

### 5 分组（聚合）查询

语法：

```
SQLSELECT 分组函数,列[要求出现在group by后面]
FROM 表名
WHERE 条件表达式
group by 分组表达式
having 分组条件表达式
ORDER BY 排序列表(字段 [asc],字段 [desc],……);
```

示例：

```
SQL# 示例：查询每个部门的平均工资 
SELECT
  avg( salary ) ,department_id
FROM
  employees 
GROUP BY
  department_id;

# 示例：查询每个工种的最高工资
SELECT
  max( salary ),
  job_id 
FROM
  employees 
GROUP BY
  job_id;

# 示例：查询每个位置上的部门个数
SELECT
  count(*),
  location_id 
FROM
  departments 
GROUP BY
  location_id;

# 示例：邮箱中包含 a 字符的，每个部门的平均工资
SELECT
  AVG( salary ),
  department_id 
FROM
  employees 
WHERE
  email LIKE '%a%' 
GROUP BY
  department_id;

# 示例：查询有奖金的每个领导手下员工的最高工资
SELECT
  max(salary),manager_id
from employees
where commission_pct is not null
GROUP BY manager_id;

# 示例：查询那个部门的员工个数 > 2
SELECT
  department_id,
  count(*) AS `count` 
FROM
  employees 
GROUP BY
  department_id 
HAVING
  `count` > 2

# 示例：查询每个工种有奖金的员工的最高工资 > 12000 的工种编号和其最高工资
SELECT
  job_id,
  max( salary ) AS `max` 
FROM
  employees 
WHERE
  commission_pct IS NOT NULL 
GROUP BY
  job_id 
HAVING
  `max` > 12000;

# 示例：按员工姓名的长度分组，查询每一组的员工个数，筛选出员工个数 > 5 的
SELECT
  count(*) ,LENGTH( last_name ) 
FROM
  employees 
GROUP BY
  LENGTH( last_name ) 
HAVING
  count(*) > 5;

# 示例：查询每个部门每个工种的员工的平均工资
SELECT
  AVG( salary ),
  department_id,
  job_id 
FROM
  employees 
GROUP BY
  department_id,
  job_id;
```

### 6 连表查询

#### 6.1 笛卡尔积

连表查询通过如下语句：

```
SQLSELECT name,boyName from boys,beauty;
```



表A有m行，表B有n行，查询结果为m*n行，这种情况叫做笛卡尔积的错误。

为了避免笛卡尔积，需要在 WHERE 中加入有效的连接条件。

#### 6.2 连接查询的分类

按年代分类：

- SQL 92 标准。
- SQL 99 标准（推荐使用）。

按功能分类：

- 内连接
  - 等值连接。
  - 非等值连接。
  - 自连接。
- 外连接
  - 左外连接。
  - 左右连接。
  - 全外连接（MySQL中不支持）。
- 交叉连接

#### 6.3 SQL 92 标准

SQL 92 标准支持所有的内连接。

等值连接：

```
SQL# 查询女神名和其对应的男神名
SELECT
  `name`,
  boyName 
FROM
  beauty,
  boys 
WHERE
  beauty.boyfriend_id = boys.id;

# 示例：查询员工名和其对应的部门名
SELECT
  last_name,
  department_name 
FROM
  employees,
  departments 
WHERE
  employees.department_id = departments.department_id;

# 示例：查询有奖金的员工名、部门名
SELECT
  e.last_name,
  d.department_name 
FROM
  employees e,
  departments d 
WHERE
  e.department_id = d.department_id 
  AND e.commission_pct IS NOT NULL;
```

非等值连接：

```
SQL# 查询员工的工资等级
SELECT
  e.salary,
  jg.grade_level 
FROM
  employees e,
  job_grades jg 
WHERE
  e.salary BETWEEN jg.lowest_sal 
  AND jg.highest_sal;
```

自连接：

```
SQLSELECT
	e.last_name as last_name ,
	m.last_name as  manager_name
FROM
	employees as e,
	employees as m 
WHERE
	e.manager_id = m.employee_id;
```

#### 6.4 SQL 99 标准

语法：

```
SQLSELECT 查询列表
FROM 表1 别名 [连接类型 inner|left|right] join 表2 别名 
ON 连接条件
WHERE 筛选条件
group by 分组字段
having 分组筛选条件
order by 排序列表;

# 说明： 
# 内连接：inner join
# 外连接： 
#   左外连接：left [outer] join
#   右外连接：right [outer] join
#   全外连接：full [outer] join
# 交叉连接：cross join
```

内连接示例：

```
SQL# 查询女神名和其对应的男神名
SELECT
	`name`,
	boyName 
FROM
	beauty
	INNER JOIN boys 
	ON beauty.boyfriend_id = boys.id;
	
# 查询员工的工资等级
SELECT
	e.salary,
	jg.grade_level 
FROM
	employees e
	INNER JOIN job_grades jg ON e.salary BETWEEN jg.lowest_sal 
	AND jg.highest_sal;
SELECT
  e.salary,
  jg.grade_level 
FROM
  employees e
  INNER JOIN job_grades jg ON e.salary BETWEEN jg.lowest_sal 
  AND jg.highest_sal;

# 查询员工的名称和其上级的名称
SELECT
  e.last_name AS last_name,
  m.last_name AS manager_name 
FROM
  employees AS e
  INNER JOIN employees AS m ON e.manager_id = m.employee_id;
```

内连接主要查询的是两个表中某个字段数据相同的交集部分，外连接主要用于查询一个表中有，另一个表中没有的数据。

外连接查询时，分为主表和从表，用作主表的表写在运算符左边时用左外连接，主表写在运算符右边时用右外连接。

比如主表A外连接从表B，查询结果为主表中的所有记录，如果从表中有匹配的，就显示，如果从表没有匹配，则显示null。换句话说，相当于：外连接的查询结果=内连接结果+主表中有但从表中没有的记录

```
SQL# 查询没有男朋友的女神名
SELECT
  beauty.`name`,
  boys.boyName 
FROM
  beauty  # beauty为主表，写在左边所以使用左外连接
  LEFT JOIN boys ON beauty.boyfriend_id = boys.id 
WHERE
  boys.boyName IS NULL;
```

交叉连接（笛卡尔积）：

```
SQLSELECT
	beauty.`name`,
	boys.boyName 
FROM
	beauty
	CROSS JOIN boys;
```

### 7 子查询

子查询：出现在其他语句内部的select语句，称为子查询。而内部嵌套其他select语句的查询，称为主查询或外查询。

子查询的分类，按照子查询出现的位置：

- select 后面：仅仅支持标量子查询
- from 后面：支持表子查询
- where 或 having 后面：支持标量子查询或列子查询，行子查询
- exists 后面（又称为相关子查询）：支持表子查询

按照结果集的行列数不同：

- 标量子查询（结果集只有一行一列）
- 列子查询（结果集只有一列多行）
- 行子查询（结果集有一行多列）
- 表子查询（结果集，一般为多行多列）

select后面支持标量子查询；

from后面支持表子查询；

where或having后面支持标量子查询，列子查询，行子查询；

exists后面支持表子查询。

#### 7.1 在where或having后面

这种子查询是最常用的。它的特点：

- 子查询放在小括号内
- 子查询一般放在条件的右侧
- 标量子查询，一般搭配单行操作符使用（>、<、>=、<=、<>）
- 列子查询，一般搭配多行操作符使用（in、any/some、all）

标量子查询示例：

```
SQL# 查询谁的工资比 Abel 高
SELECT
  last_name 
FROM
  employees 
WHERE
  salary > ( SELECT salary FROM employees WHERE last_name = 'Abel' );

# 返回 job_id 和 141 号员工相同，salary 比 143 号员工多的员工姓名、job_id 和工资
SELECT
  last_name,
  job_id,
  salary 
FROM
  employees 
WHERE
  job_id = ( SELECT job_id FROM employees WHERE employee_id = 141 ) 
  AND salary > ( SELECT salary FROM employees WHERE employee_id = 143 );

# 返回公司工资最少的员工的 last_name 、job_id 和 salary
SELECT
  last_name,
  job_id,
  salary 
FROM
  employees 
WHERE
  salary = ( SELECT min( salary ) FROM employees );

# 查询最低工资大于 50 号部门最低工资的部门 id 和其最低工资
SELECT
  department_id,
  MIN( salary ) 
FROM
  employees 
GROUP BY
  department_id 
HAVING
  min( salary ) > ( SELECT min( salary ) FROM employees WHERE department_id = 50 );
```

列子查询示例：

```
SQL# 返回 location_id 是 1400 或 1700 的部门中的所有员工姓名
SELECT
  last_name 
FROM
  employees 
WHERE
  department_id IN ( SELECT DISTINCT department_id FROM departments WHERE location_id IN ( 1400, 1700 ) );
# 返回其它工种中比 job_id 为 'IT_PROG' 工种任一工资低的员工的员工号、姓名、job_id 以及 salary
SELECT
  employee_id,
  last_name,
  job_id,
  salary 
FROM
  employees 
WHERE
  salary < ANY ( SELECT DISTINCT salary FROM employees WHERE job_id = 'IT_PROG' ) and job_id !=  'IT_PROG';
# 返回其它工种中比 job_id 为 'IT_PROG' 工种所有工资低的员工的员工号、姓名、job_id 以及 salary
SELECT
  employee_id,
  last_name,
  job_id,
  salary 
FROM
  employees 
WHERE
  salary < ALL ( SELECT DISTINCT salary FROM employees WHERE job_id = 'IT_PROG' ) and job_id !
```

行子查询不常用，示例：

```
SQL# 查询员工编号最小并且工资最高的员工信息
SELECT * FROM employees 
WHERE ( salary, employee_id ) = (( SELECT max( salary ) FROM employees ),( SELECT min( employee_id ) FROM employees ) );
```

#### 7.2 在select后面

示例：

```
SQL# 查询每个部门的员工个数
SELECT d.*,( SELECT count(*) FROM employees e WHERE e.department_id = d.department_id ) as '员工个数'
FROM
  departments d;
```

#### 7.3 在from后面

```
SQL# 查询每个部门的平均工资的工资等级
SELECT
  temp.department_id,
  jg.grade_level 
FROM
  ( SELECT department_id AS department_id, avg( salary ) AS `avg` FROM employees GROUP BY department_id ) temp
  INNER JOIN ( SELECT grade_level, highest_sal, lowest_sal FROM job_grades ) jg ON temp.avg BETWEEN jg.lowest_sal 
  AND jg.highest_sal;
```

#### 7.4 在exists后面

语法：

```
SQLexists(查询语句)
# 返回 0或者1
```

示例：

```
SQL# 查询有员工的部门名
SELECT
  department_name 
FROM
  departments d 
WHERE
  EXISTS ( SELECT * FROM employees e WHERE d.department_id = e.department_id );
```

### 8 分页查询

应用场景：实际的web项目中需要根据用户的提交请求，返回对应的分页

语法：

```
SQLSELECT 查询列表
FROM 表 [join type] JOIN 表2
ON 连接条件
WHERE 筛选条件
GROUP BY 分组字段
HAVING 分组筛选条件
ORDER BY 排序字段
LIMIT 起始索引(从0开始)，每页显示条数。
```

特点：

- 起始条目索引从0开始
- limit子句放在查询语句的最后
- 公式：`select * from 表 limit （page-1）*sizePerPage,sizePerPage`，其中每页显示条目数`sizePerPage`，要显示的页数`page`

示例：

```
SQL# 查询前 5 条员工信息
SELECT
  * 
FROM
  employees 
  LIMIT 0,5;
```

### 9 联合查询

将多条查询语句的结果合并成一个结果。

语法：

```
SQL查询语句1
UNION
查询语句2
...;
```

特点：

- 多条查询语句的查询的列数必须是一致的
- 多条查询语句的查询的列的类型几乎相同
- union代表去重，union all代表不去重，可以包含重复项

示例：

```
SQL# 查询部门编号 > 90 或邮箱包含 a 的员工信息 
SELECT * FROM employees WHERE last_name LIKE '%a%'  
UNION
SELECT * FROM employees WHERE department_id > 90 ;
```

## 六、DML

DML：数据的插入和删除、修改。

### 1 插入

语法：

```
SQLINSERT INTO 表名(列名1,列名2,……,列名n) values(值1,值2,……,值n),(值1,值2,……,值n),……;
```

特点：

- 字段类型和值类型一致或兼容，而且一一对应
- 可以为空的字段，可以不用插入值，或用null填充
- 不可以为空的字段，必须插入值
- 字段个数和值的个数必须一致
- 插入时，字段可以省略，但默认为所有字段，并且顺序和表中的存储顺序一致

示例：

```
SQL# 新增雇员信息
INSERT INTO employees ( first_name, last_name, email, phone_number, job_id, salary, commission_pct, manager_id, department_id, hiredate )
VALUES
	(
		'xx',
		'xxx',
		'xxx@qq.com',
		'18888888',
		NULL,
		3000,
		NULL,
		NULL,
		NULL,
	'2019-11-11')
```

### 2 修改

语法：

```
SQLUPDATE 表名
SET 列1=值1,列2=值2,……,列n=值n
[WHERE 条件];
```

示例：

```
SQL# 修改表中姓名为 K_ing 的手机号码为 12345678901
UPDATE employees 
SET phone_number = '12345678901' 
WHERE
  last_name = 'K_ing';
```

### 3 删除

语法：

```
SQL# 方式1：delete语句 
DELETE FROM 表名
[WHERE 筛选条件];

# 方式2：truncate语句，删除现有数据表中的所有数据。
truncate table 表名
```

示例：

```
SQL# 删除 last_name 为 xxx 的员工
DELETE 
FROM
	employees 
WHERE
	last_name = 'xxx';
DELETE 
FROM
  employees 
WHERE
  last_name = 'xxx';
```

两种删除方式的区别：

- truncate不能加where条件，而delete可以加where条件
- truncate的效率高一丢丢
- truncate 删除带自增长的列的表后，如果再插入数据，数据从1开始
- delete 删除带自增长列的表后，如果再插入数据，数据从上一次的断点处开始
- truncate删除不能回滚，delete删除可以回滚

## 七、TCL

### 1 介绍

TCL：事务控制语言。

事物是由单独单元的一个或多个 SQL 语句组成，在这个单元中，每个 SQL 语句是相互依赖的。而整个单独单元作为一个不可分割的整体，如果单元中的某条 SQL 语句一旦执行失败或产生错误，整个单元将会回滚。所有受到影响的数据将返回到事务开始之前的状态；如果单元中的所有 SQL 语句都执行成功，则事务执行成功。

简单讲，事务指逻辑上的一组操作，组成这组操作的各个单元，要不全部成功，要不全部不成功。

事物的特点如下：

- 原子性（A:atomicity）： 事务是最小的执行单位，不允许分割。事务的原子性确保动作要么都执行，要么都回滚；
- 一致性（C:consistency）：执行事务前后，数据保持一致，多个事务对同一个数据读取的结果是相同的；
- 隔离性（I:isolation）： 并发访问数据库时，一个用户的事务不被其他事务所干扰，各并发事务之间数据库是独立的；
- 持久性（D:durability）： 一个事务被提交之后。它对数据库中数据的改变是持久的，即使数据库发生故障也不应该对其有任何影响。

事物的原理：事务开启之后，所有的操作都会临时保存在事务日志中，事务日志只有在得到 `commit` 命令才会同步到数据库中，其他的任何情况都会清空事务日志（ `rollback` ，断开连接）。

隐式事物：默认情况下，MySQL 中的事务是默认自动提交的，比如INSERT、DELETE语句，都可以看做开启了一个事物，自动提交。

显式事物：在需要原子性操作的时候，需要手动开启事务。

使用场景：转账、订单的生成、付款等。

### 2 事务的创建

主要介绍显示事物的创建。

前提：需要关闭隐式事物的自动提交

```
SQLSET autocommit = 0;
```

创建事务的完整语法：

```
SQLSTART TRANSACTION; # 开启事物
SQL 语句..;
SQL 语句..;
SQL 语句..;
...
COMMIT[ROLLBACK]; # 提交事务(COMMIT)或回滚事务(ROLLBACK)
```

示例：

```
SQL# 张三向李四转账 500
SET autocommit = 0;
START TRANSACTION;
UPDATE account SET balance = balance - 500 WHERE username = '张三';
UPDATE account SET balance = balance + 500 WHERE username = '李四';
COMMIT;
```

### 3 隔离级别

对于同时运行的多个事务，当这些事务访问数据库中相同的数据时，如果没有采取必要的隔离机制，就会导致各种并发问题。比如脏读、幻读、不可重复读。

- 脏读(Drity Read)：对于两个事务T1、T2，T1读取了已经被T2更新但是还没提交的字段。之后，如果T2回滚，T1读取的内容就是临时且无效的。
- 不可重复读(Non-repeatable read)：在一个事务的两次查询之中数据不一致，这可能是两次查询过程中间插入了一个事务更新的原有的数据。
- 幻读(Phantom Read):在一个事务的两次查询中数据笔数不一致，例如有一个事务查询了几列(Row)数据，而另一个事务却在此时插入了新的几列数据，先前的事务在接下来的查询中，就会发现有几列数据是它先前所没有的。

为此，引入了数据库事务的隔离级别来避免事务的并发问题。

一个事务和其他事务隔离的程序称为隔离级别。数据库规定了多种事务隔离级别，不同隔离级别对应不同的干扰程序，隔离级别越高，数据一致性就越好，但是并发性就越低。

为了满足事务的四大特性，数据库定义了4种不同的事务隔离级别，从低到高依次是：

- READ-UNCOMMITTED(读取未提交)： 最低的隔离级别，允许读取尚未提交的数据变更，可能会导致脏读、幻读或不可重复读。
- READ-COMMITTED(读取已提交)： 允许读取并发事务已经提交的数据，可以阻止脏读，但是幻读或不可重复读仍有可能发生。
- REPEATABLE-READ(可重复读)： 对同一字段的多次读取结果都是一致的，除非数据是被本身事务自己所修改，可以阻止脏读和不可重复读，但幻读仍有可能发生。
- SERIALIZABLE(可串行化)： 最高的隔离级别，完全服从ACID的隔离级别。所有的事务依次逐个执行，这样事务之间就完全不可能产生干扰，也就是说，该级别可以防止脏读、不可重复读以及幻读。

下表展示了四种隔离级别的强度，会造成并发问题用`√`表示，不会造成并发问题用`×`表示：

| 隔离级别         | 脏读 | 不可重复读 | 幻影读 |
| ---------------- | ---- | ---------- | ------ |
| READ-UNCOMMITTED | √    | √          | √      |
| READ-COMMITTED   | ×    | √          | √      |
| REPEATABLE-READ  | ×    | ×          | √      |
| SERIALIZABLE     | ×    | ×          | ×      |

每启动一个 MySQL 客户端程序，就会获取一个单独的数据库连接。每个数据库连接都会有一个全局变量 @@tx_isolation ，表示当前的事务隔离级别。 设置隔离级别：

```
SQLSET SESSION|GLOBAL TRANSACTION ISOLATION LEVEL 隔离级别名;
# SESSION表示设置当前连接的隔离级别
# GLOBAL表示设置系统隔离级别
```

查看当前的隔离级别：

```
SELECT @@tx_isolation;
```

> Oracle 默认支持 2 种事务隔离级别：READ COMMITTED（读已提交）和SERIALIZABLE（串行化）。Oracle 默认的事务隔离级别是 READ COMMITTED（读已提交）。
>
> MySQL 支持 4 种事务隔离级别。MySQL 默认的事务隔离级别是 REPEATABLE READ（可重复读）。
>
> 在分布式事物中，一般会使用最高的隔离级别SERIALIZABLE

## 八、DCL

DCL：用于定义用户的访问权限和安全级别。

### 1 介绍

目前为止，默认使用的都是 root 用户，超级管理员，拥有全部权限。但是，一个公司里面的数据库服务器上面可能同时运行着很多项目的数据库，所以，我们应该根据不同的项目建立不同的用户、分配不同的权限来管理和维护数据库。

### 2 创建用户

语法：

```
SQLCREATE USER '用户名'@'主机名' IDENTIFIED BY '密码';
 
#用户名：要创建的用户
#主机名：指定该用户在哪个主机上可以登录，如果是本地用户可以使用 localhost ，如果想让该用户可以从任意远程主机登录，可以使用通配符 % 
#密码：该用户的登录密码，密码可以为空，如果为空则表示该用户可以不需要密码登录服务器。 
```

示例：

```
SQL# user1 用户只能在 localhost 这个 IP 登录 mysql 服务器 
CREATE USER 'user1'@'localhost' IDENTIFIED BY '123';
# user2 用户可以在任何电脑上远程登录 mysql 服务器
CREATE USER 'user2'@'%' IDENTIFIED BY '123';
```

### 3 授权和取消授权

授权语法：

```
SQLGRANT 权限1, 权限2... ON 数据库名.表名 TO '用户名'@'主机名';

# GRANT：授权关键字 
# 授予用户的权限：如 SELECT ，INSERT ，UPDATE 等。如果要授予所的权限则使用 ALL 。 
# 数据库名.表名：该用户可以操作哪个数据库的哪些表。如果要授予该用户对所有数据库和表的相应操作权限则可用 * 表示，如 *.* 。 
# '用户名'@'主机名': 给哪个用户授权。 
```

示例：

```
SQL# 给 user1 用户分配对 test 这个数据库操作的权限 
GRANT CREATE,ALTER,DROP,INSERT,UPDATE,DELETE,SELECT ON test.* TO 'user1'@'localhost';
# 给 user2 用户分配对所有数据库操作的权限
GRANT ALL ON *.* TO 'user2'@'%';
```

撤销授权语法：

```
SQLREVOKE  权限1, 权限2... ON 数据库.表名 FROM '用户名'@'主机名';
```

示例：

```
SQL# 撤销 user1 用户对 test 操作的权限
REVOKE ALL ON test.* FROM 'user1'@'localhost';
```

### 4 查看权限

语法：

```
SQLSHOW GRANTS FOR '用户名'@'主机名';
```

示例：

```
SQL# 查看 user2 用户的权限
SHOW GRANTS FOR 'user2'@'%';
```

### 5 删除用户

语法：

```
SQLDROP USER '用户名'@'主机名'
```

示例：

```
SQL# 删除 user2
DROP USER 'user2'@'%';
```

### 6 修改用户密码

#### 6.1 修改管理员密码

语法（在bash终端，登录之前操作）：

```
BASHmysqladmin -uroot -p password 新密码
```

#### 6.2 修改普通用户的密码

语法（root用户登录后操作）：

```
SQLSET PASSWORD FOR '用户名' @'主机名' = PASSWORD ( '新密码' );
```

## 九、视图

### 1 介绍

MySQL 从 5.0.1 版本开始提供了视图功能。可以把它理解为一种虚拟存在的表，行和列的数据来自自定义视图的查询中使用的表，并且是在使用视图的时候动态生成的，只保存了SQL的逻辑，不保存查询结果。

视图使开发者只关心感兴趣的某些特定数据和所负责的特定任务，只能看到视图中所定义的数据，而不是视图所引用表中的数据，从而提高了数据库中数据的安全性。

视图的特点如下:

- 视图的列可以来自不同的表，是表的抽象和在逻辑意义上建立的新关系。
- 视图是由基本表(实表)产生的表(虚表)。
- 视图的建立和删除不影响基本表。
- 对视图内容的更新(添加，删除和修改)直接影响基本表。
- 当视图来自多个基本表时，不允许添加和删除数据。

视图的优点：

- 提高了sql语句重用性，效率高
- 和表实现了分离，提高了安全性、
- 逻辑数据独立性。视图对重构数据库提供了一定程度的逻辑独立性

### 2 使用场景

视图根本用途：简化sql查询，提高开发效率。

下面是视图的常见使用场景：

- 重用SQL语句；
- 简化复杂的SQL操作。在编写查询后，可以方便的重用它而不必知道它的基本查询细节；
- 使用表的组成部分而不是整个表；
- 保护数据。可以给用户授予表的特定部分的访问权限而不是整个表的访问权限；
- 更改数据格式和表示。视图可返回与底层表的表示和格式不同的数据。

### 3 创建视图

语法：

```
SQLCREATE VIEW 视图名
AS
查询语句;
```

示例：

```
SQL# 查询姓名中包含 a 字符的员工名、部门名和工种信息
CREATE VIEW v1
AS
SELECT
  e.last_name,
  d.department_name,
  j.job_title
FROM
  employees e
  INNER JOIN departments d ON e.department_id = d.department_id
  INNER JOIN jobs j ON e.job_id = j.job_id;

SELECT * FROM v1 WHERE last_name like '%a%';
```

### 4 查看视图

语法：

```
SQLDESC 视图名;
# 或者
SHOW CREATE VIEW 视图名;
```

### 5 修改视图

语法：

```
SQLALTER VIEW 视图名
AS
查询语句;
```

### 6 删除视图

语法：

```
SQLDROP VIEW 视图名,视图名...;
```

## 十、MySQL逻辑架构

### 1 整体架构

- 和其它数据库相比，MySQL有点与众不同，它的架构可以在多种不同场景中应用并发挥良好作用。主要体现在存储引擎的架构上。
- 插件式的存储引擎架构将查询处理和其它的系统任务以及数据的存储提取相分离。这种架构可以根据业务的需求和实际需要选择合适的存储引擎。

整体架构如图所示：



### 2 连接层

最上层是一些客户端和连接服务，包含本地sock通信和大多数基于客户端/服务端工具实现的类似于tcp/ip的通信。主要完成一些类似于连接处理、授权认证、及相关的安全方案。在该层上引入了线程池的概念，为通过认证安全接入的客户端提供线程。同样在该层上可以实现基于SSL的安全链接。服务器也会为安全接入的每个客户端验证它所具有的操作权限。

- `Connections`：指的是不同语言中与SQL的交互。

- ```
  Connection Pool
  ```

  ：连接池，管理、缓冲用户连接，线程处理等需要缓存的需求。

  - 负责监听对 MySQL Server 的各种请求，接收连接请求，转发所有连接请求到线程管理模块。
  - 每一个连接上 MySQL Server 的客户端请求都会被分配（或创建）一个连接线程为其单独服务。而连接线程的主要工作就是负责 MySQL Server 与客户端的通信。接受客户端的命令请求，传递 Server 端的结果信息等。线程管理模块则负责管理维护这些连接线程。包括线程的创建，线程的 cache 等。

### 3 服务层

第二层架构主要完成大多数的核心服务功能，如SQL接口，并完成缓存的查询，SQL的分析和优化及部分内置函数的执行。所有跨存储引擎的功能也在这一层实现，如过程、函数等。在该层，服务器会解析查询并创建相应的内部解析树，并对其完成相应的优化如确定查询表的顺序，是否利用索引等，最后生成相应的执行操作。如果是select语句，服务器还会查询内部的缓存。如果缓存空间足够大，这样在解决大量读操作的环境中能够很好的提升系统的性能。

- `Enterprise Management Serveices & Utilities`：系统管理和控制工具。备份、安全、复制、集群等等。

- `SQL Interface`：接受用户的SQL命令，并且返回用户需要查询的结果。

- ```
  Parser
  ```

  ：SQL语句解析器。将SQL语句进行语义和语法的分析，分解成数据结构，然后按照不同的操作类型进行分类，然后做出针对性的转发到后续步骤，以后SQL语句的传递和处理就是基于这个结构的。

  - SQL命令传递到解析器的时候会被解析器验证和解析。解析器是由Lex和YACC实现的，是一个很长的脚本。
  - 在 MySQL中我们习惯将所有 Client 端发送给 Server 端的命令都称为 Query，在 MySQL Server 里面，连接线程接收到客户端的一个 Query 后，会直接将该 Query 传递给专门负责将各种 Query 进行分类然后转发给各个对应的处理模块。
  - 如果在分解构成中遇到错误，那么就说明这个sql语句是不合理的

- `Optimizer`：查询优化器，SQL语句在查询之前会使用查询优化器对查询进行优化。就是优化客户端请求query，根据客户端请求的 query 语句，和数据库中的一些统计信息，在一系列算法的基础上进行分析，得出一个最优的策略，告诉后面的程序如何取得这个 query 语句的结果。举例： `select uid,name from user where gender = 1;`这个`select`查询先根据`where`语句进行选取，而不是先将表全部查询出来以后再进行`gender`过滤；然后根据`uid`和`name`进行属性投影，而不是将属性全部取出以后再进行过滤。最后将这两个查询条件联接起来生成最终查询结果。

- `Caches & Buffers`：查询缓存。主要功能是将客户端提交给MySQL 的 Select 类 query 请求的返回结果集 cache 到内存中，与该 query 的一个 hash 值做一个对应。该 Query 所取数据的基表发生任何数据的变化之后， MySQL 会自动使该 query 的Cache 失效。在读写比例非常高的应用系统中， Query Cache 对性能的提高是非常显著的。当然它对内存的消耗也是非常大的。如果查询缓存有命中的查询结果，查询语句就可以直接去查询缓存中取数据。这个缓存机制是由一系列小缓存组成的。比如表缓存，记录缓存，key缓存，权限缓存等。

### 4 引擎层

存储引擎层，存储引擎真正的负责了MySQL中数据的存储和提取，服务器通过APl与存储引擎进行通信。不同的存储引擎具有的功能不同，这样我们可以根据自己的实际需要进行选取。常用的存储引擎是MyISAM和InnoDB。

- `Pluggable Storage Engines`：存储引擎接口。MySQL区别于其他数据库的最重要的特点就是其插件式的表存储引擎(存储引擎是基于表的，而不是数据库)。MySQL插件式的存储引擎架构提供了一系列标准的管理和服务支持，这些标准与存储引擎本身无关，可能是每个数据库系统本身都必需的，如SQL分析器和优化器等，而存储引擎是底层物理结构的实现，每个存储引擎开发者都可以按照自己的意愿来进行开发。

### 5 存储层

数据存储层，主要是将数据存储在运行于裸设备的文件系统之上，并完成与存储引擎的交互。

- `File System`：数据落地到磁盘上，就是文件的存储。

### 6 存储引擎详解

可以通过`show engines;`命令查看当前支持的所有引擎：



查看当前数据库正在使用的存储引擎：

```
SQLSHOW VARIABLES LIKE 'default_storage_engine%';
```

常用的存储引擎有以下：

- Innodb引擎：Innodb引擎提供了对数据库ACID事务的支持。并且还提供了行级锁和外键的约束。它的设计的目标就是处理大数据容量的数据库系统。
- MyIASM引擎(原本Mysql的默认引擎)：不提供事务的支持，也不支持行级锁和外键。
- MEMORY引擎：所有的数据都在内存中，数据的处理速度快，但是安全性不高。

MyISAM与InnoDB区别：

|                                                              | MyISAM                                                       | Innodb                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 存储结构                                                     | 每张表被存放在三个文件：frm-表格定义、MYD(MYData)-数据文件、MYI(MYIndex)-索引文件 | 所有的表都保存在同一个数据文件中（也可能是多个文件，或者是独立的表空间文件），InnoDB表的大小只受限于操作系统文件的大小，一般为2GB |
| 存储空间                                                     | MyISAM可被压缩，存储空间较小                                 | InnoDB的表需要更多的内存和存储，它会在主内存中建立其专用的缓冲池用于高速缓冲数据和索引 |
| 可移植性、备份及恢复                                         | 由于MyISAM的数据是以文件的形式存储，所以在跨平台的数据转移中会很方便。在备份和恢复时可单独针对某个表进行操作 | 免费的方案可以是拷贝数据文件、备份 binlog，或者用 mysqldump，在数据量达到几十G的时候就相对痛苦了 |
| 文件格式                                                     | 数据和索引是分别存储的，数据`.MYD`，索引`.MYI`               | 数据和索引是集中存储的，`.ibd`                               |
| 记录存储顺序                                                 | 按记录插入顺序保存                                           | 按主键大小有序插入                                           |
| 外键                                                         | 不支持                                                       | 支持                                                         |
| 事务                                                         | 不支持                                                       | 支持                                                         |
| 锁支持（锁是避免资源争用的一个机制，MySQL锁对用户几乎是透明的） | 表级锁定                                                     | 行级锁定、表级锁定，锁定力度小并发能力高                     |
| SELECT                                                       | MyISAM更优                                                   |                                                              |
| INSERT、UPDATE、DELETE                                       |                                                              | InnoDB更优                                                   |
| select count(*)                                              | MyISAM更快，因为MyISAM内部维护了一个计数器，可以直接调取。   |                                                              |
| 索引的实现方式                                               | B+树索引，MyISAM是堆表                                       | B+树索引，InnoDB是索引组织表                                 |
| 哈希索引                                                     | 不支持                                                       | 支持                                                         |
| 全文索引                                                     | 支持                                                         | 不支持                                                       |

存储引擎选择方面，如果没有特别的需求，使用默认的InnoDB即可。

MyISAM：以读写插入为主的应用程序，比如博客系统、新闻门户网站。

InnoDB：更新（删除）操作频率也高，或者要保证数据的完整性；并发量高，支持事务和外键。比如OA自动化办公系统。

### 7 MySQL一条语句的查询流程

客户端请求 —> 连接器（验证用户身份，给予权限） —> 查询缓存（存在缓存则直接返回，不存在则执行后续操作） —> 分析器（对SQL进行词法分析和语法分析操作） —> 优化器（主要对执行的sql优化选择最优的执行方案方法） —> 执行器（执行时会先看用户是否有执行权限，有才去使用这个引擎提供的接口） —> 去引擎层获取数据返回（如果开启查询缓存则会缓存查询结果）



## 十一、索引

### 1 介绍

索引（Index）是帮助MySQL高效获取数据的数据结构——索引是一种数据结构，是数据库管理系统中一个排序的数据结构，以协助快速查询、更新数据库表中数据。索引的实现通常使用B树及其变种B+树。

索引是一种特殊的文件（InnoDB数据表上的索引是表空间的一个组成部分），它们包含着对数据表里所有记录的引用指针。一般来说索引本身占用内存空间也很大，不可能全部存储在内存中，因此索引往往以文件形式存储在硬盘上，占据一定的物理空间。

更通俗的说，索引就相当于目录。为了方便查找书中的内容，通过对内容建立索引形成目录。可以简单理解为排好序的快速查找数据结构“，即索引 = 排序 + 查找，建立索引之后，查找起来会变快。

### 2 建立索引

#### 2.1 单值索引

假设有如下查询语句经常被使用：

```
SQLSELECT * FROM user WHERE NAME = 'xxx';
```

可以通过建立索引，使得杂乱的数据变得有序、易查询。

```
SQLCREATE INDEX idx_user_name ON USER (name);
# idx_user_name：约定俗成的命名规范，idx表示这是一个索引，user表示在user表建立索引，name是建立索引的字段
```

#### 2.2 复合索引

复合索引就是给多个字段建立索引：

```
SQLCREATE INDEX idx_user_name ON USER (name,email);
```

### 3 索引的优缺点

索引的优点：

- 可以大大加快数据的检索速度，这也是创建索引的最主要的原因。
- 通过使用索引，可以在查询的过程中，使用优化隐藏器，提高系统的性能。
- 降低数据排序成本，降低了CPU的消耗

索引的缺点：

- 时间方面：创建索引和维护索引要耗费时间，具体地，当对表中的数据进行增加、删除和修改的时候，索引也要动态的维护，会降低增/改/删的执行效率；
- 空间方面：索引需要占物理空间。

### 4 索引分类

主键索引：数据列不允许重复，不允许为NULL，一个表只能有一个主键。

- 可以通过 `ALTER TABLE table_name ADD PRIMARY KEY(column);` 创建主键索引

唯一索引：数据列不允许重复，允许为NULL值，一个表允许多个列创建唯一索引。

- 可以通过 `ALTER TABLE table_name ADD UNIQUE (column);` 创建唯一索引
- 可以通过 `ALTER TABLE table_name ADD UNIQUE (column1,column2);` 创建唯一复合索引

普通索引：基本的索引类型，没有唯一性的限制，即一个索引只包含单个列，允许为NULL值。一个表可以有多个单列索引；建议一张表索引不要超过5个。

- 可以通过`ALTER TABLE table_name ADD INDEX index_name (column);`创建普通索引
- 可以通过`ALTER TABLE table_name ADD INDEX index_name(column1, column2, column3);`创建复合索引

全文索引： 是目前搜索引擎使用的一种关键技术。

- 可以通过`ALTER TABLE table_name ADD FULLTEXT (column);`创建全文索引

### 5 索引语法

#### 5.1 建立索引

```
SQLCREATE [UNIQUE] INDEX  indexName ON mytable(columnname(length));
# 或者
ALTER mytable ADD [UNIQUE]  INDEX [indexName] ON(columnname(length));

# 如果是CHAR和VARCHAR类型，length可以小于字段实际长度；如果是BLOB和TEXT类型，必须指定length。
```

#### 5.2 删除索引

```
SQLDROP INDEX [indexName] ON mytable;
```

#### 5.3 查看索引

`\G`表示将查询到的横向表格纵向输出，方便阅读

```
PLAINTEXTSHOW INDEX FROM table_name\G
```

### 6 索引的数据结构

索引的数据结构和具体存储引擎的实现有关，在MySQL中使用较多的索引有Hash索引，B+树索引等，而我们经常使用的InnoDB存储引擎的默认索引实现为：B+树索引。对于哈希索引来说，底层的数据结构就是哈希表，因此在绝大多数需求为单条记录查询的时候，可以选择哈希索引，查询性能最快；其余大部分场景，建议选择BTree索引。

#### 6.1 BTree索引

B树索引是Mysql数据库中使用最频繁的索引类型，基本所有存储引擎都支持BTree索引。通常我们说的索引不出意外指的就是（B树）索引。

如下图的一颗 B 树， 浅蓝色的块我们称之为一个磁盘块， 可以看到每个磁盘块包含几个数据项（深蓝色所示） 和指针（黄色所示）。比如磁盘块 1 包含数据项 17 和 35， 包含指针 P1、 P2、 P3。P1 表示小于 17 的磁盘块， P2 表示在 17 和 35 之间的磁盘块， P3 表示大于 35 的磁盘块，以此类推。

如果要查找数据项 29， 那么首先会把磁盘块 1 由磁盘加载到内存， 此时发生一次 IO， 在内存中用二分查找确定 29在 17 和 35 之间， 锁定磁盘块 1 的 P2 指针， 内存时间因为非常短（相比磁盘的 IO） 可以忽略不计 通过磁盘块 1的 P2 指针的磁盘地址把磁盘块 3 由磁盘加载到内存， 发生第二次 IO， 29 在 26 和 30 之间， 锁定磁盘块 3 的 P2 指针 通过指针加载磁盘块 8 到内存， 发生第三次 IO， 同时内存中做二分查找找到 29， 结束查询， 总计三次 IO。

#### 6.2 B+Tree索引

B+树的关键字（数据项）和记录是放在一起的； B+树的非叶子节点中只有关键字和指向下一个节点的索引， 记录只放在叶子节点中。

在 B 树中， 越靠近根节点的记录查找时间越快， 只要找到关键字即可确定记录的存在； 而 B+ 树中每个记录的查找时间基本是一样的， 都需要从根节点走到叶子节点， 而且在叶子节点中还要再比较关键字。从这个角度看 B 树的性能好像要比 B+ 树好， 而在实际应用中却是 B+ 树的性能要好些。 因为 B+ 树的非叶子节点不存放实际的数据，这样每个节点可容纳的元素个数比 B 树多， 树高比 B 树小， 这样带来的好处是减少磁盘访问次数。

尽管 B+ 树找到一个记录所需的比较次数要比 B 树多， 但是一次磁盘访问的时间相当于成百上千次内存比较的时间， 因此实际中B+ 树的性能可能还会好些， 而且 B+树的叶子节点使用指针连接在一起， 方便顺序遍历（范围搜索）， 这也是很多数据库和文件系统使用 B+树的缘故。

下图是一个B+树的示例：



B+tree性质：

- B+跟B树不同B+树的非叶子节点不保存关键字记录的指针，只进行数据索引，这样使得B+树每个非叶子节点所能保存的关键字大大增加
- B+树叶子节点保存了父节点的所有关键字记录的指针，所有数据地址必须要到叶子节点才能获取到。所以每次数据查询的次数都一样
- 叶子节点本身依关键字的大小自小而大顺序链接。左边结尾数据都会保存右边节点开始数据的指针。

总的来说，B+树查找的效率要比B树更高、更稳定。由于非叶子节点并不是最终指向文件内容的节点， 而只是叶子节点中关键字的索引， 所以任何关键字的查找必须走一条从根节点到叶子节点的路。 所有关键字查询的路径长度相同，使得每一个数据的查询效率相当。

#### 6.3 Hash索引

类似于数据结构中简单实现的HASH表（散列表）一样，当我们在mysql中用哈希索引时，主要就是通过Hash算法（常见的Hash算法有直接定址法、平方取中法、折叠法、除数取余法、随机数法），将数据库字段数据转换成定长的Hash值，与这条数据的行指针一并存入Hash表的对应位置；如果发生Hash冲突（两个不同关键字的Hash值相同），则在对应Hash键下以链表形式存储（拉链法），如图：



### 7 何时需要建索引

#### 7.1 适合建立索引的情况

- 主键自动建立唯一索引
- 频繁作为查询的条件的字段应该创建索引
- 查询中与其他表关联的字段，外键关系建立索引
- 查询中排序的字段，排序字段若通过索引去访问将大大提高排序的速度
- 查询中统计或者分组字段

#### 7.2 不适合建立索引的情况

- 频繁更新的字段不适合创建索引
- Where 条件里用不到的字段不创建索引
- 表记录太少
- 数据重复且分布平均的表字段，注意，如果某个数据列包含许多重复的内容，为它建立索引就没有太大的实际效果。假如一个表有10万行记录，有一个字段A只有T和F两种值，且每个值的分布概率大约为50%，那么对这种表A字段建索引一般不会提高数据库的查询速度。

#### 7.3 总结

索引的创建最好符合以下原则：

- 最左前缀匹配原则。组合索引非常重要的原则，mysql会一直向右匹配直到遇到范围查询(>、<、between、like)就停止匹配，比如`a = 1 and b = 2 and c > 3 and d = 4`如果建立(a,b,c,d)顺序的索引，d是用不到索引的，如果建立(a,b,d,c)的索引则都可以用到，a,b,d的顺序可以任意调整。
- 较频繁作为查询条件的字段才去创建索引
- 更新频繁字段不适合创建索引
- 若是不能有效区分数据的列不适合做索引列(如性别，男女未知，最多也就三种，区分度实在太低)
- 尽量的扩展索引，不要新建索引。比如表中已经有a的索引，现在要加(a,b)的索引，那么只需要修改原来的索引即可。
- 定义有外键的数据列一定要建立索引。
- 对于那些查询中很少涉及的列，重复值比较多的列不要建立索引。
- 对于定义为text、image和bit的数据类型的列不要建立索引。

另外，索引的选择性是指索引列中不同值的数目与表中记录数的比。如果一个表中有2000条记录，表索引列有1980个不同的值，那么这个索引的选择性就是1980/2000=0.99。一个索引的选择性越接近于1，这个索引的效率就越高。

### 8 聚簇索引、回表

#### 8.1 基本概念

聚簇索引：将数据与索引存放到一起，找到索引就可以直接找到数据。

非聚簇索引：将数据存储与索引分开，索引结构的叶子节点存储的是对应数据的地址，并不能直接获取到数据。

回表：举个例子，非聚簇索引中找到了叶子节点，获取叶子节点存储的地址，根据这个地址再去查找一次，这个过程叫做回表。

下图为一个聚簇索引：



一个表建立后，如果有主键，主键就是默认的聚簇索引。如果表中没有定义主键，InnoDB会选择一个唯一的非空索引代替。如果没有这样的索引，InnoDB会隐式定义一个主键来作为聚簇索引。

由于存储引擎负责实现索引，因此不是所有的存储引擎都支持聚簇索引（比如MyISAM不支持聚簇索引），MyISAM使用非聚簇索引，如下图：



需要注意：

- 聚簇索引不是一种单独的数据类型，而是一种数据存储方式。
- InnoDB的聚簇索引实际上在同一结构中保存了B+Tree索引和数据，当表有聚簇索引时，它的数据行实际上存放在索引的叶子节点中。
- 因为无法同时把数据行放在两个不同的地方，所以一个表只能有一个聚簇索引。
- InnoDB中，在聚簇索引之上创建的索引称之为辅助索引，辅助索引访问数据总是需要二次查找，非聚簇索引都是辅助索引。辅助索引叶子节点存储的不再是行的物理位置，而是主键值

#### 8.2 聚簇索引和费聚簇索引的区别



InnoDB使用的是聚簇索引，将主键组织到一棵B+树中，而行数据就储存在叶子节点上，若使用“where id = 14“ 这样的条件查找主键，则按照B+树的检索算法即可查找到对应的叶节点，之后获得行数据。

若对Name列进行条件搜索，则需要两个步骤：第一步在辅助索引B+树中检索Name，到达其叶子节点获取对应的主键。第二步使用主键在主索引B+树种再执行一次B+树检索操作，最终到达叶子节点即可获取整行数据。（重点在于通过其他键需要建立辅助索引）

聚簇索引优点：

- 由于行数据和叶子节点存储在一起，同一页中会有多条行数据，访问同一数据页不同行记录时，已经把页加载到了Buffer中，再次访问的时候，会在内存中完成访问，不必访问磁盘。这样主键和行数据是一起被载入内存的，找到叶子节点就可以立刻将行数据返回了，如果按照主键Id来组织数据，获得数据更快。
- 聚簇索引适合用在排序的场合，非聚簇索引不适合
- 取出一定范围数据的时候，使用用聚簇索引速度快
- 可以把相关数据保存在一起。例如实现电子邮箱时，可以根据用户 ID 来聚集数据，这样只需要从磁盘读取少数的数据页就能获取某个用户的全部邮件。如果没有使用聚簇索引，则每封邮件都可能导致一次磁盘 I/O。

聚簇索引缺点：

- 如果使用UUId（随机ID）作为主键，使数据存储稀疏，这就会出现聚簇索引有可能有比全表扫面更慢。聚簇索引的数据的物理存放顺序与索引顺序是一致的，即：只要索引是相邻的，那么对应的数据一定也是相邻地存放在磁盘上的。因此，主键通常使用自增id。
- 如果主键比较大的话，那辅助索引将会变的更大，因为辅助索引的叶子存储的是主键值；过长的主键值，会导致非叶子节点占用占用更多的物理空间。

下图展示了使用uuid主键和自增主键的区别：





#### 8.3 非聚簇索引与回表

非聚簇索引不一定进行回表查询。

这涉及到查询语句所要求的字段是否全部命中了索引，如果全部命中了索引，那么就不必再进行回表查询。

举个简单的例子，假设我们在员工表的年龄上建立了索引，那么当进行`SELECT age FROM employee WHERE age < 20`的查询时，在索引的叶子节点上，已经包含了age信息，就不会再次进行回表查询。

#### 8.4 何时使用聚簇索引与非聚簇索引



### 9 MyISAM索引与InnoDB索引的区别

- InnoDB索引是聚簇索引，MyISAM索引是非聚簇索引。
- InnoDB的主键索引的叶子节点存储着行数据，因此主键索引非常高效。
- MyISAM索引的叶子节点存储的是行数据地址，需要再寻址一次才能得到数据。
- InnoDB非主键索引的叶子节点存储的是主键和其他带索引的列数据，因此查询时做到覆盖索引会非常高效。

> 覆盖索引：
>
> 如果要查询的字段都建立过索引，那么引擎会直接在索引表中查询而不会访问原始数据（否则只要有一个字段没有建立索引就会做全表扫描），这叫索引覆盖。因此我们需要尽可能的在`select`后只写必要的查询字段，以增加索引覆盖的几率。
>
> 这里值得注意的是不要想着为每个字段建立索引，因为优先使用索引的优势就在于其体积小。

### 10 联合索引

MySQL可以使用多个字段同时建立一个索引，叫做联合索引。在联合索引中，如果想要命中索引，需要按照建立索引时的字段顺序挨个使用，否则无法命中索引。



如图，我们在三个列上建立了一个联合索引：整形id、字符串name、日期birthDate。那么索引的排序为：先按照id 排序，如果id 相同，则按照name排序，如果name的值也相等，则按照birthDate进行排序。

当进行查询时，此时索引仅仅按照id严格有序，因此必须首先使用id字段进行等值查询，之后对于匹配到的列而言，其按照name字段严格有序，此时可以使用name字段用做索引查找，以此类推。如果直接按照name查找： `select* from employee where name='Staff'` 就不会走索引，因为name是依靠着id进行排序的。

因此，在建立联合索引的时候应该注意索引列的顺序，一般情况下，将查询需求频繁或者字段选择性高的列放在前面。此外可以根据特例的查询或者表结构进行单独的调整。

## 十二、性能分析

### 1 SQL变慢的原因

性能下降、 SQL 慢、执行时间长、等待时间长的原因一般有：

- 关联查询使用太多JOIN语句
- 索引失效（建立了索引，但没有用到）：
- 查询语句本身的问题
- 服务器调优及各个参数设置（缓冲、线程数等）

### 2 JOIN详解

SQL变慢的其中一个原因是使用了太多JOIN，为什么会这样？首先需要了解SQL语句的执行顺序。

#### 2.1 SQL 执行顺序

我们手写的sql一般如下，看起来是从上到下顺序执行的：

```
SQLSELECT DISTINCT
	< select_list > 
FROM
	< left_table > < join_type >
	JOIN < right_table > ON < join_condition > 
WHERE
	< where_condition > 
GROUP BY
	< groupby_list > 
HAVING
	< having_condition > 
ORDER BY
	< order_by_condition > 
	LIMIT < limit_number >;
```

但是这些语句在解析器的执行顺序却并不是这样，实际执行顺序如下（随着 Mysql 版本的更新换代， 其优化器也在不断的升级， 优化器会分析不同执行顺序产生的性能消耗不同而动态调整执行顺序）：

```
SQLFROM
	< left_table > 
ON < join_condition > < join_type >
	JOIN < right_table > 
WHERE
	< where_condition > 
GROUP BY
	< groupby_list > 
HAVING
	< having_condition > 
SELECT DISTINCT
	< select_list > 
ORDER BY
	< order_by_condition > 
	LIMIT < limit_number >;
```

可以看到解析器首先执行FROM，最关心数据是从哪里来的，sql语句在机器看来的解析顺序如下图：



#### 2.2 JOIN图

所有的JOIN如图所示：



### 3 MySQL 常见瓶颈

对于MySQL的运行来说，有如下常见瓶颈：

- CPU 瓶颈：CPU在饱和的时候一般发生在数据装入在内存或从磁盘上读取数据时候
- IO 瓶颈：磁盘I/O瓶颈发生在装入数据远大于内存容量时
- 服务器硬件的性能瓶颈：使用top、free、iostat和vmstat来查看系统的性能状态

### 4 EXPLAIN

#### 4.1 如何使用

使用EXPLAIN关键字可以模拟优化器执行SQL语句，从而知道MySQL是如何处理SQL语句的，可以用于分析你的查询语句或者是结构的性能瓶颈。

使用方法：

```
SQL# 原sql语句：SELECT * FROM student;
# EXPLAIN+原sql语句
EXPLAIN SELECT * FROM student;
```

结果如下：



可以看到返回了一些字段，根据这些字段可以得到如下信息：

- 表的读取顺序（`id`字段）
- 数据读取操作的操作类型（`select_type`字段）
- 哪些索引可以使用（`possible_keys`字段）
- 哪些索引被实际使用（`keys`字段）
- 表之间的引用（`ref`字段）
- 每张表有多少行被优化器查询（`rows`字段）

#### 4.2 各个字段的详细解释

> 1、`id`字段

- select查询的序列号，包含一组数字，表示查询中执行select子句或操作表的顺序。

- 它的取值有三种情况

  - `id`相同，执行顺序由上至下

    

  - `id`全不同，如果是子查询，id的序号会递增，id值越大优先级越高，越先被执行

    

  - `id`部分相同，可以这样理解：id相同的可以认为是一组，每组中表的读取顺序为从上往下顺序执行；在所有组之间，id值越大的那一组优先级越高，越先执行

    

> 2、`select_type`字段，为查询的类型，主要用于区别普通查询、联合查询、子查询等复杂查询

- SIMPLE：简单的select查询，查询中不包含子查询或者UNION
- PRIMARY：查询中若包含任何复杂的子部分，最外层查询则被标记为PRIMARY
- SUBQUERY：在SELECT或者WHERE列表中包含了子查询
- DERIVED：在FROM列表中包含的子查询被标记为DERIVED（衍生）MySQL会递归执行这些子查询，把结果放在临时表里
- UNION：若第二个SELECT出现在UNION之后，则被标记为UNION；若UNION包含在FROM子句的子查询中，外层SELECT将被标为：DERIVED
- UNION RESULT：从UNION表获取结果的SELECT

> 3、`table`字段，显示这一行的数据是关于哪张表的。

> 4、`type`字段，访问类型排列，显示查询使用了何种类型

- 结果值从最好到最坏依次是

  - `system>const>eq_ref>ref>fultext>ref_or_null>index_merge>unique_subquery>index_subquery>range>index>ALL`
  - 挑重要的来说`system>const>eq_ref>ref>range>index>ALL`，一般来说，百万以上级别的数据要保证查询至少达到range级别，最好能达到ref。

- 类型详解：

  - system：表只有一行记录（等于系统表），这是`const`类型的特例，平时不会出现，可以忽略不计。

  - const：表示通过索引一次就找到了，const用于比较primary key或者unique索引。因为只匹配一行数据，所以很快。如将主键置于where列表中，MySQL就能将该查询转换为一个常量，如图：

    

  - eq_ref：唯一性索引，对于每个索引键，表中只有一条记录与之匹配，常见于主键或唯一索引扫描

    

  - ref：非唯一索引扫描，返回匹配某个单独值的所有行。本质上也是一种索引访问，它返回所有匹配某个单独值的行，然而，它可能会找到多个符合条件的行，所以他应该属于查找和扫描的混合体

    

  - range：只检索给定范围的行，使用一个索引来选择行。key列显示使用了哪个索引一般就是在你的where语句中出现了`between`、`<`、`>`、`in`等的查询这种范围扫描索引扫描比全表扫描要好，因为他只需要开始索引的某一点，而结束于另一点，不用扫描全部索引（在范围内扫描）

    

  - index：Full Index Scan（全索引扫描），index与ALL区别为index类型只遍历索引树。这通常比ALL快，因为索引文件通常比数据文件小。（也就是说虽然all和index都是读全表，但index是从索引中读取的，而all是从硬盘数据库文件中读的）

    

  - all：FullTable Scan，将遍历全表以找到匹配的行（全表扫描），最差的扫描

    

> 5、`possible_keys`字段

- 显示可能应用在这张表中的索引，一个或多个
- 若查询涉及的字段上存在索引，则该索引将被列出，但不一定被查询实际使用

> 6、`key`字段

- 实际使用的索引，如果为null，则没有使用索引

- 若查询中使用了覆盖索引，则该索引仅出现在key列表中

  

> 7、`key_len`字段

- 表示索引中使用的字节数，可通过该列计算查询中使用的索引的长度。在不损失精确性的情况下，长度越短越好

- `key_len`显示的值为索引最大可能长度，并非实际使用长度，即`key_len`是根据表定义计算而得，不是通过表内检索出的

- 要查询的精度越高，所消耗的索引字节数就越多：

  

> 8、`ref`字段

- 显示索引哪一列被使用了，如果可能的话，最好是一个常数。说明了哪些列或常量被用于查找索引列上的值。

- 如图，先加载t2，类型为全表扫描，再加载t1，使用到了索引，由`key_len`可知t1表的索引idx_col1_col2被充分使用，t2表的col被用于在索引上查找，常量’ac’也被用于在索引上查找。

  

> 9、`rows`字段

- 根据表统计信息及索引选用情况，大致估算出找到所需的记录所需要读取的行数（越小越好）

> 10、`Extra`字段，包含不适合在其他列中显示但十分重要的额外信息

- Using filesort（文件排序）

  - MySQL中无法利用索引完成排序操作称为“文件排序”，说明mysql会对数据使用一个外部的索引排序，而不是按照表内的索引顺序进行读取。

    出现 Using filesort 不好，需要尽快优化 SQL

    

- Using temporary（创建临时表)

  - 使用了临时表保存中间结果，MySQL在对查询结果排序时使用临时表。常见于排序 order by 和分组查询 group by

  - 出现 Using temporary 非常不好，需要立即优化 SQL

    

- Using index（覆盖索引）

  - 表示相应的select操作中使用了覆盖索引（Coveing Index），避免访问了表的数据行，效率不错。

  - 如果同时出现using where，表明索引被用来执行索引键值的查找

  - 如果没有同时出现using where，表明索引用来读取数据而非执行查找动作

    

- Using where：表明使用了where过滤

- Using join buffer：表明使用了连接缓存

- impossible where：where子句的值总是false，不能用来获取任何元组

- select tables optimized away：在没有GROUPBY子句的情况下，基于索引优化MIN/MAX操作或者对于MyISAM存储引擎优化COUNT(*)操作，不必等到执行阶段再进行计算，查询执行计划生成的阶段即完成优化。

- distinct：优化distinct，在找到第一匹配的元组后即停止找同样值的工作

## 十三、索引优化

### 1 单表索引优化案例

准备数据：

```
SQL# 模拟，博客文章的数据库
CREATE TABLE IF NOT EXISTS article(
	id INT(10) UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
	author_id INT(10) UNSIGNED NOT NULL,
	category_id INT(10) UNSIGNED NOT NULL,
	views INT(10) UNSIGNED NOT NULL,
	comments INT(10) UNSIGNED NOT NULL,
	title VARCHAR(255) NOT NULL,
	content TEXT NOT NULL
);

INSERT INTO article(author_id,category_id,views,comments,title,content)
VALUES
(1,1,1,1,'1','1'),
(2,2,2,2,'2','2'),
(1,1,3,3,'3','3');
```

需求为：查询`category_id`为1且`comments`大于1的情况下，`views`最多的`id`，查询语句如下：

```
SQLSELECT id, author_id FROM article WHERE category_id = 1 AND comments > 1 ORDER BY views DESC LIMIT 1;
+----+-----------+
| id | author_id |
+----+-----------+
|  3 |         1 |
+----+-----------+
```

此时没有建立索引，尝试用explain分析：

```
SQLEXPLAIN SELECT id, author_id FROM article WHERE category_id = 1 AND comments > 1 ORDER BY views DESC LIMIT 1;
```



很显然，type是ALL，即最坏的情况，没有用到索引。Extra里出现了Using filesort文件排序，也是最坏的情况，所以优化是必须的。

首先想到的是为每个查询的字段都建立索引：

```
SQLCREATE INDEX idx_article_ccv ON article ( category_id, comments, views );
SHOW INDEX FROM article;
```

再次分析：



type变成了range，这是可以忍受的。但是extra里使用Using filesort仍是无法接受的。但是我们已经建立了索引，为什么没用呢？因为按照B+Tree索引的工作原理，先排序category_id，如果遇到相同的ategory_id则再排序comments，如果遇到相同的comments则再排序 views。当comments字段在联合索引里处于中间位置时，因为`comments>1`条件是一个范围值（range），MySQL无法利用索引再对后面的views部分进行检索，即range类型查询字段后面的索引失效。

于是有了第二个索引建立思路，对于范围查询的字段不建索引，直接把它跳过去，为后面的字段建索引。首先把原来的索引删掉：

```
SQLDROP INDEX [indexName] ON mytable;
```

重新建立索引：

```
SQLCREATE INDEX idx_article_ccv ON article ( category_id, views );
```

再次分析：可以看到，type变为了ref，Extra中的Using filesort也消失了，结果非常理想：



### 2 双表索引优化案例

准备数据：

```
SQLCREATE TABLE IF NOT EXISTS class(
	id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
	card INT(10) UNSIGNED NOT NULL,
	PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS book(
	bookid INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
	card INT(10) UNSIGNED NOT NULL,
	PRIMARY KEY(bookid)
);

INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO class(card) VALUES(FLOOR(1+(RAND()*20)));

INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO book(card) VALUES(FLOOR(1+(RAND()*20)));
```

需求为：实现两表的外连接，连接条件是 class.card = book.card，查询语句如下：

```
SQLSELECT * FROM class LEFT JOIN book ON class.card = book.card;
```

用explain分析：

```
SQLEXPLAIN SELECT * FROM class LEFT JOIN book ON class.card = book.card;
```



可以看到没有添加索引时，type为All ，rows为表中数据总行数，说明class和book进行了全表检索。Extra中Using join buffer，表明连接过程中使用了join缓冲区。

由于是左连接，左边的数据肯定都要查询，所以右表才是我们的关键点，一定需要建立索引。即：左表连接右表，则需要拿着左表的数据去右表里面查，索引需要在右表中建立索引。

```
SQLALTER TABLE book ADD INDEX Y(card);
```

再次分析：



可以看到第二行的type变为了ref，rows也变成了优化比较明显，且Using join buffer也消失了。

如果只在左表建索引：

```
SQLDROP INDEX Y ON book;  # 删除右表索引
ALTER TABLE class ADD INDEX X(card); # 添加左表索引
```

再次分析：



效果是不如在右表建立索引好的，这也印证了之前的理论。

当然，为两个表都建索引也是可行的。但是如果只建一个索引，那么原则就是为相反的表建索引：

- 左外连接，为右表的字段建索引
- 右外连接，为左表的字段建索引

### 3 三表索引优化案例

准备数据（以及案例2中的class表和book表）：

```
SQLCREATE TABLE IF NOT EXISTS phone(
	phoneid INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
	card INT(10) UNSIGNED NOT NULL,
	PRIMARY KEY(phoneid)
)ENGINE=INNODB;

INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
INSERT INTO phone(card) VALUES(FLOOR(1+(RAND()*20)));
```

需求为：实现三表的外连接，查询语句如下：

```
SQLSELECT * FROM class LEFT JOIN book ON class.card = book.card LEFT JOIN phone ON book.card = phone.card;
```

用explain分析：



可以看到没有添加索引时，type为All，rows 为表数据总行数，说明class、book和phone表都进行了全表检索Extra中Using join buffer，表明连接过程中使用了join缓冲区。

根据前面的理论，我们需要在右表建立索引，所以book要建立，phone也是右表，也要建立：

```
SQLALTER TABLE book ADD INDEX Y (card);
ALTER TABLE phone ADD INDEX Z (card);
```

再次分析：



后2行的type都是ref，且总rows优化很好。因此索引最好设置在需要经常查询的字段中。

得出Join语句优化的结论：

- 尽可能减少Join语句中的NestedLoop的循环总次数
- 永远用小结果集驱动大的结果集（在大结果集中建立索引，在小结果集中遍历全表）
- 优先优化NestedLoop的内层循环
- 保证Join语句中被驱动表上Join条件字段已经被索引
- 当无法保证被驱动表的Join条件字段被索引且内存资源充足的前提下，不要太吝惜JoinBuffer的设置

### 4 避免索引失效

避免索引失效：

- 尽量使用全值匹配

- 使用最佳左前缀法则：如果索引了多例，要遵守最左前缀法则。指的是查询从索引的最左前列开始并且不跳过索引中的列。

- 不在索引列上做任何操作（计算、函数、（自动or手动）类型转换），会导致索引失效而转向全表扫描

- 范围条件右边的索引会失效

- 尽量使用覆盖索引（只访问索引的查询（索引列和查询列一致）），减少使用`select *`

- mysql在使用不等于（!=或者<>）的时候无法使用索引会导致全表扫描

- is null，is not null 也无法使用索引（早期版本不能走索引，后续版本应该优化过，可以走索引）

- like以通配符开头（

  ```
  %abc…
  ```

  ）索引失效，会变成全表扫描操作

  - 解决`like '%str%'` 索引失效的问题：使用覆盖索引

- 字符串不加单引号索引失效

  - 如果字符串忘记用单引号括起来，那么mysql会为我们进行隐式的类型转换，而进行了类型转换，索引就会失效

- 少用or，用or连接时会索引失效

现在回头再看看前面提到的[何时需要建索引](#index)，会有更加清晰的认识。

## 十四、SQL优化工具

### 1 慢查询日志

MySQL的慢查询日志是MySQL提供的一种日志记录，它用来记录在MySQL中响应时间超过阀值的语句，具体指运行时间超过long_query_time值的SQL，则会被记录到慢查询日志中。long_query_time的默认值为10，运行10秒以上的SQL语句会被记录下来。由慢查询日志来查看哪些SQL超出了我们的最大忍耐时间值，比如一条sql执行超过5秒钟，我们就算慢SQL，希望能收集超过5秒的sql，结合explain进行全面分析。

#### 1.1 开启慢查询日志

默认情况下，MySQL数据库没有开启慢查询日志，需要我们手动来设置这个参数。如果不是调优需要，一般不建议开启该参数，因为开启慢查询日志或多或少会带来一定的性能影响。

首先查看mysql的慢查询日志是否开启，通过如下命令：

```
SQLSHOW VARIABLES LIKE '%slow_query_log%';
```



`slow_query_log`为`OFF`表示关闭了慢查询日志，`slow_query_log_file`表示日志的存放位置。

使用如下命令开启慢查询日志：

```
SQLSET GLOBAL slow_query_log = 1;
```

使用此方法开启了慢查询日志只对当前数据库生效，如果MySQL重启后则会失效。如果要永久生效，就必须修改配置文件`my.cnf`。修改如下位置即可：

```
PLAINTEXT[mysqld]
slow_query_log =1
slow_query_log_file=/var/lib/mysql/Heygo-slow.log
```

#### 1.2 修改参数

开启慢查询日志后，什么样的SQL会记录到慢查询里面？这个是由参数`long_query_time`控制，默认情况下long_query_time的值为10秒，使用如下命令查看慢SQL记录的阈值：

```
SQLSHOW VARIABLES LIKE 'long_query_time%';
```

另外，运行时间正好等于`long_query_time`并不会被记录下来。

可以手动修改这个阈值，通过命令临时修改（永久修改需要修改`my.cnf`）：

```
SQLSET GLOBAL long_query_time = 5;
```

执行之后需要重新连接或者新开一个客户端连接才能看到修改值。

#### 1.3 查看日志

现在，执行如下语句，一定会被慢日志记录：

```
SQLSELECT sleep(6); 
```

慢查询日志文件默认在`/var/lib/mysql/` 下，后缀为`-slow.log`，查看一下：

```
BASHcat 68926f356828-slow.log 

mysqld, Version: 5.7.37 (MySQL Community Server (GPL)). started with:
Tcp port: 3306  Unix socket: /var/run/mysqld/mysqld.sock
Time                 Id Command    Argument
# Time: 2022-01-28T10:57:27.035023Z
# User@Host: root[root] @  [192.168.142.3]  Id:     7
# Query_time: 6.000578  Lock_time: 0.000000 Rows_sent: 1  Rows_examined: 0
SET timestamp=1643367447;
SELECT sleep(6);
```

查询当前系统中有多少条慢查询记录：

```
SQLSHOW GLOBAL STATUS LIKE '%Slow_queries%';
```

#### 1.4 日志分析命令

在生产环境中，如果要手工分析日志，查找、分析SQL，显然是个体力活，MySQL提供了日志分析工具`mysqldumpslow`。

```
BASH# 查看帮助：mysqldumpslow --help
Usage: mysqldumpslow [ OPTS... ] [ LOGS... ]

Parse and summarize the MySQL slow query log. Options are

  --verbose    verbose
  --debug      debug
  --help       write this text to standard output

  -v           verbose
  -d           debug
  -s ORDER     what to sort by (al, at, ar, c, l, r, t), 'at' is default # 表示按何种方式排序 默认为at
                al: average lock time  # 按平均锁定时间
                ar: average rows sent  # 按平均返回记录数
                at: average query time  # 按平均查询时间
                 c: count  # 按访问次数
                 l: lock time  # 按锁定时间
                 r: rows sent  # 按返回记录
                 t: query time   # 按查询时间
  -r           reverse the sort order (largest last instead of first)
  -t NUM       just show the top n queries  # 只显示前N条查询
  -a           don't abstract all numbers to N and strings to 'S'
  -n NUM       abstract numbers with at least n digits within names
  -g PATTERN   grep: only consider stmts that include this string  # 匹配指定字符串
  -h HOSTNAME  hostname of db server for *-slow.log filename (can be wildcard),
               default is '*', i.e. match all
  -i NAME      name of server instance (if using mysql.server startup script)
  -l           don't subtract lock time from total time
```

常见使用示例：

```
BASH# 得到返回记录集最多的10个SQL
mysqldumpslow -s r -t 10 /var/lib/mysql/68926f356828-slow.log 
# 得到访问次数最多的10个SQL
mysqldumpslow -s c -t 10 /var/lib/mysql/68926f356828-slow.log
# 得到按照时间排序的前10条里面含有左连接的查询语句
mysqldumpslow -s t -t 10 -g "left join" /var/lib/mysql/68926f356828-slow.log
# 在使用这些命令时结合 | 和more使用，因为如果日志很大，可能会刷屏
mysqldumpslow -s r -t 10 /var/lib/mysql/68926f356828-slow.log | more
```

### 2 Show Profile

Show Profile是mysql提供可以用来分析当前会话中语句执行的资源消耗情况，可以用于SQL的调优测量。默认情况下，参数处于关闭状态，并保存最近15次的运行结果。

#### 2.1 开启Show Profile

查看Show Profile是否开启，使用如下命令：

```
SQLSHOW VARIABLES LIKE 'profiling%';
```

开启Show Profile：

```
SQLSET profiling = ON;
```

#### 2.2 使用Show Profile

下面运行几条SQL尝试一下：

```
SQL# 普通sql
select * from tbl_emp;
select * from tbl_emp e inner join tbl_dept d on e.deptId = d.id;
select * from tbl_emp e left join tbl_dept d on e.deptId = d.id;

# 慢sql
select * from emp group by id%10 limit 150000;
select * from emp group by id%10 limit 150000;
select * from emp group by id%20 order by 5;
```

查看结果：

```
SQLmysql> SHOW PROFILES;
+----------+------------+----------------------------------------------------------------------+
| Query_ID | Duration   | Query                                                                |
+----------+------------+----------------------------------------------------------------------+
|        1 | 0.00052700 | show variables like 'profiling%'                                     |
|        2 | 0.00030300 | select * from tbl_emp                                                |
|        3 | 0.00010650 | select * from tbl_emp e inner join tbl_dept d on e.'deptId' = d.'id' |
|        4 | 0.00031625 | select * from tbl_emp e inner join tbl_dept d on e.deptId = d.id     |
|        5 | 0.00042100 | select * from tbl_emp e left join tbl_dept d on e.deptId = d.id      |
|        6 | 0.38621875 | select * from emp group by id%20 limit 150000                        |
|        7 | 0.00014900 | select * from emp group by id%20 order by 150000                     |
|        8 | 0.38649000 | select * from emp group by id%20 order by 5                          |
|        9 | 0.06782700 | select COUNT(*) from emp                                             |
|       10 | 0.35434400 | select * from emp group by id%10 limit 150000                        |
+----------+------------+----------------------------------------------------------------------+
```

#### 2.3 诊断SQL

查看SQL语句执行的具体流程以及每个步骤花费的时间：

```
SQLSHOW PROFILE cpu,block io FOR QUERY SQL编号;
# 查询参数解释：

# ALL：显示所有的开销信息
# BLOCK IO：显示块IO相关开销
# CONTEXT SWITCHES：上下文切换相关开销
# CPU：显示CPU相关开销信息
# IPC：显示发送和接收相关开销信息
# MEMORY：显示内存相关开销信息
# PAGE FAULTS：显示页面错误相关开销信息
# SOURCE：显示和Source_function，Source_file，Source_line相关的开销信息
# SWAPS：显示交换次数相关开销的信息
```

示例：

```
SQLmysql> SHOW PROFILE cpu,block io FOR QUERY 2;
+----------------------+----------+----------+------------+--------------+---------------+
| Status               | Duration | CPU_user | CPU_system | Block_ops_in | Block_ops_out |
+----------------------+----------+----------+------------+--------------+---------------+
| starting             | 0.000055 | 0.000000 |   0.000000 |            0 |             0 |
| checking permissions | 0.000007 | 0.000000 |   0.000000 |            0 |             0 |
| Opening tables       | 0.000011 | 0.000000 |   0.000000 |            0 |             0 |
| init                 | 0.000024 | 0.000000 |   0.000000 |            0 |             0 |
| System lock          | 0.000046 | 0.000000 |   0.000000 |            0 |             0 |
| optimizing           | 0.000018 | 0.000000 |   0.000000 |            0 |             0 |
| statistics           | 0.000008 | 0.000000 |   0.000000 |            0 |             0 |
| preparing            | 0.000019 | 0.000000 |   0.000000 |            0 |             0 |
| executing            | 0.000003 | 0.000000 |   0.000000 |            0 |             0 |
| Sending data         | 0.000089 | 0.000000 |   0.000000 |            0 |             0 |
| end                  | 0.000004 | 0.000000 |   0.000000 |            0 |             0 |
| query end            | 0.000003 | 0.000000 |   0.000000 |            0 |             0 |
| closing tables       | 0.000005 | 0.000000 |   0.000000 |            0 |             0 |
| freeing items        | 0.000006 | 0.000000 |   0.000000 |            0 |             0 |
| cleaning up          | 0.000006 | 0.000000 |   0.000000 |            0 |             0 |
+----------------------+----------+----------+------------+--------------+---------------+
```

> 如果你使用Navicat软件，也可以在`剖析`中查看到这些数据。

如果status状态出现以下几种，需要警惕：

- converting HEAP to MyISAM：查询结果太大，内存都不够用了往磁盘上搬了。
- Creating tmp table：创建临时表，mysql 先将拷贝数据到临时表，然后用完再将临时表删除
- Copying to tmp table on disk：把内存中临时表复制到磁盘
- locked：锁表

### 3 SQL优化思路

配合慢查询日志和Show Profile，梳理一下SQL的优化思路。当整个sql server变慢之后，可以按照如下方法进行分析：

- 开启慢查询，捕获慢sql
- 使用explain对慢查询日志中的sql进行分析
- 使用show profile查询sql在mysql服务器里面的执行细节和生命周期情况
- 对sql数据库服务器的参数进行调优

## 十五、锁

在数据库中，除传统的计算资源（如CPU、RAM、I/O等）的争用以外，数据也是一种供许多用户共享的资源，当数据库有并发事务的时候，可能会产生数据的不一致，这时候需要一些机制来保证访问的次序，锁机制就是这样的一个机制。

### 1 锁分类

#### 1.1 按操作类型分

- 读锁（共享锁）：当用户要进行数据的读取时，多个读操作可以同时进行而不会互相影响。共享锁可以同时加上多个。
- 写锁（排它锁）：当用户要进行数据的写入时，对数据加上排他锁。排他锁只可以加一个，他和其他的排他锁，共享锁都相斥。

#### 1.2 按操作粒度分

- 表锁：表级锁是MySQL中锁定粒度最大的一种锁，表示对当前操作的整张表加锁，它实现简单，资源消耗较少，被大部分MySQL引擎支持。最常使用的MYISAM与INNODB都支持表级锁定。表级锁定分为表共享读锁（共享锁）与表独占写锁（排他锁）。特点：开销小，加锁快；不会出现死锁；锁定粒度大，发出锁冲突的概率最高，并发度最低。
- 页锁页级锁是MySQL中锁定粒度介于行级锁和表级锁中间的一种锁。表级锁速度快，但冲突多，行级冲突少，但速度慢。所以取了折衷的页级，一次锁定相邻的一组记录。特点：开销和加锁时间界于表锁和行锁之间；会出现死锁；锁定粒度界于表锁和行锁之间，并发度一般
- 行锁，行级锁是Mysql中锁定粒度最细的一种锁，表示只针对当前操作的行进行加锁。行级锁能大大减少数据库操作的冲突。其加锁粒度最小，但加锁的开销也最大。行级锁分为共享锁和排他锁。特点：开销大，加锁慢；会出现死锁；锁定粒度最小，发生锁冲突的概率最低，并发度也最高。

|      | 开销 | 加锁速度 | 可能出现死锁 | 并发程度 |
| ---- | ---- | -------- | ------------ | -------- |
| 表锁 | 小   | 快       | 否           | 低       |
| 页锁 | 中等 | 中等     | 是           | 中等     |
| 行锁 | 大   | 慢       | 是           | 高       |

存储引擎使用什么类型的锁：

- MyISAM采用表级锁
- InnoDB支持行级锁和表级锁，默认为行级锁
- BDB引擎采用页级锁

### 2 锁的使用

查看当前数据库中表的上锁情况：

```
SQLshow open tables;  
# 0 表示未上锁
```

#### 2.1 表锁

表锁一般是MyISAM引擎使用。

添加表锁

```
SQLlock table 表名1 read(write), 表名2 read(write), ...;
```

释放所有表锁

```
SQLunlock tables;
```

会话session1将表A加读锁之后：

- session1可以对A进行读操作，其它sessions也可以对A进行读操作
- session1不能修改表A，其它sessions此时修改表A，会被提示阻塞直到锁被释放
- session1此时不可以读其它表（比如表B）

会话session1将表A加写锁之后：

- session1可以对A进行读操作，其它sessions不可以对A进行读操作
- session1可以修改表A，其它sessions此时修改表A，会被提示阻塞直到锁被释放
- session1此时不可以读其它表（比如表B）

结论：

- MyISAM在执行查询语句（SELECT）前，会自动给涉及的所有表加读锁，在执行增删改操作前，会自动给涉及的表加写锁。
- 简而言之，就是读锁会阻塞写，但是不会堵塞读。而写锁则会把读和写都堵塞。

其他分析工具：

可以通过检查`table_locks_waited`和`table_locks_immediate`状态变量来分析系统上的表锁定：

```
SQLshow status like 'table%';
+----------------------------+--------+
| Variable_name              | Value  |
+----------------------------+--------+
| Table_locks_immediate      | 500440 |
| Table_locks_waited         | 1      |
| Table_open_cache_hits      | 500070 |
| Table_open_cache_misses    | 5      |
| Table_open_cache_overflows | 0      |
+----------------------------+--------+
5 rows in set (0.00 sec)
```

- `Table_locks_immediate`：产生表级锁定的次数，表示可以立即获取锁的查询次数，每立即获取锁值加1；
- `Table_locks_waited`：出现表级锁定争用而发生等待的次数（不能立即获取锁的次数，每等待一次锁值加1），此值高则说明存在着较严重的表级锁争用情况；
- 此外，MyISAM的读写锁调度是写优先，这也是MyISAM不适合做写为主表的引擎。因为写锁后，其他线程不能做任何操作，大量的更新会使查询很难得到锁，从而造成永远阻塞。

#### 2.2 行锁

行锁一般是InnoDB引擎使用。

InnoDB基于索引来自动加行锁：对于UPDATE、DELETE和INSERT语句，InnoDB会自动给涉及数据集加排他锁；对于普通SELECT语句，InnoDB不会加任何锁。

但是，行锁可能因为未使用索引而升级为表锁，所以除了检查索引是否创建的同时，也需要通过explain查询索引是否被实际使用。行锁相对于表锁来说，优势在于高并发场景下表现更突出，毕竟锁的粒度小。

### 3 乐观锁和悲观锁

数据库管理系统（DBMS）中的并发控制的任务是确保在多个事务同时存取数据库中同一数据时不破坏事务的隔离性和统一性以及数据库的统一性。乐观并发控制（乐观锁）和悲观并发控制（悲观锁）是并发控制主要采用的技术手段。

悲观锁：假定会发生并发冲突，屏蔽一切可能违反数据完整性的操作。在查询完数据的时候就把事务锁起来，直到提交事务。实现方式：使用数据库中的锁机制

乐观锁：假设不会发生并发冲突，只在提交操作时检查是否违反数据完整性。在修改数据的时候把事务锁起来，通过version的方式来进行锁定。实现方式：乐一般会使用版本号机制或CAS算法实现。

两种锁的使用场景

从上面对两种锁的介绍，我们知道两种锁各有优缺点，不可认为一种好于另一种，像乐观锁适用于写比较少的情况下（多读场景），即冲突真的很少发生的时候，这样可以省去了锁的开销，加大了系统的整个吞吐量。

但如果是多写的情况，一般会经常产生冲突，这就会导致上层应用会不断的进行retry，这样反倒是降低了性能，所以一般多写的场景下用悲观锁就比较合适。

## 十六、主从

### 1 介绍

和Redis的主从一样，mysql主从复制能使得从mysql服务器能精确得复制主mysql服务器，即master和slave的主从数据同步，并且MySQL的复制和Redis一样默认是异步的。整个过程如图所示：



1. master会将变动记录到二进制日志里面
2. master启动I/O线程将二进制日志发送到slave
3. slave的I/O线程把master发送的二进制写入到relay日志中
4. slave的SQL线程按照relay日志读取出数据进行同步

### 2 搭建过程

这里基于本地docker环境进行搭建，采用mysql5.7镜像，其中：

- 主库：10086端口
- 从库：10087端口

获取镜像

```
BASHdocker pull mysql:5.7
```

创建目录，用于主库目录映射。

```
BASHmkdir /home/mysql
mkdir /home/mysql/conf.d
mkdir /home/mysql/data/
```

创建配置文件

```
BASHtouch /home/mysql/my.cnf
```

从库也如此创建

```
BASHmkdir /home/mysql2
mkdir /home/mysql2/conf.d
mkdir /home/mysql2/data/
touch /home/mysql2/my.cnf
```

修改主库的配置文件`my.cnf`，添加如下内容：

```
BASH[mysqld]
user=mysql
character-set-server=utf8
default_authentication_plugin=mysql_native_password
secure_file_priv=/var/lib/mysql
expire_logs_days=7
sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
max_connections=1000
server-id=1  # 服务器id
log-bin=mysql-bin # 开启binlog日志，其中mysql-bin代表的是basename就是生成二进制日志文件的前缀部分,默认的位置在datadir目录下,也可以设置为其他的路径
[client]
default-character-set=utf8
[mysql]
default-character-set=utf8
```

修改从库的配置文件`my.cnf`，添加如下内容：

```
BASH[mysqld]
user=mysql
character-set-server=utf8
default_authentication_plugin=mysql_native_password
secure_file_priv=/var/lib/mysql
expire_logs_days=7
sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
max_connections=1000
server-id=2  # 服务器id，不要与其它库重复
log-bin=mysql-slave-bin # 开启binlog日志
relay_log=relaylog-slave-bin  # 开启中继日志，从服务器在这里读取内容并应用到从服务器
[client]
default-character-set=utf8
[mysql]
default-character-set=utf8
```

配置完成后，启动主从mysql容器：

```
BASH#启动主库容器（进行目录映射，端口映射成10086，初始密码为123456）
docker run  -di -v /home/mysql/data/:/var/lib/mysql -v /home/mysql/conf.d:/etc/mysql/conf.d -v /home/mysql/my.cnf:/etc/mysql/my.cnf -p 10086:3306 --name mysql-master -e MYSQL_ROOT_PASSWORD=123456 mysql:5.7

#启动从库容器（进行目录映射，端口映射成10087，初始密码为123456）
docker run  -di -v /home/mysql2/data/:/var/lib/mysql -v /home/mysql2/conf.d:/etc/mysql/conf.d -v /home/mysql2/my.cnf:/etc/mysql/my.cnf -p 10087:3306 --name mysql-slave -e MYSQL_ROOT_PASSWORD=123456 mysql:5.7
```

测试连接成功：



主库建立一个复制帐户，专门用于主从复制。连接到主库之后：

```
SQLCREATE USER 'copy'@'%' IDENTIFIED BY '123';  # 创建用户
GRANT REPLICATION SLAVE ON *.* TO 'copy'@'%'; # 授权
FLUSH PRIVILEGES;  # 刷新权限
```

查看主库状态：

```
SQLSHOW MASTER STATUS;
```



- File：主库的binlog日志名
- Position：当操作数据库导致bin-log日志增加时，position位点也会增加

连接从库，进行配置：

```
SQLCHANGE MASTER TO master_host = '192.168.142.88',  # 主库地址
master_port=10086,  # 端口号
master_user = 'copy',  # 进行复制的用户
master_password = '123',  # 密码
master_log_file = 'mysql-bin.000004',  # 主库binlog文件名
master_log_pos = 0;  # 从position之后开始复制，设置为0即全部复制

# 启动从库，开始复制
START SLAVE;
```

查看从库状态：

```
SQLSHOW SLAVE STATUS;
```

主要关注这两个参数，



可以看到`Slave_IO_Running: Yes`，即IO线程正常运行，`Slave_SQL_Running: Yes`，SQL线程正常运行。说明主从已经搭建成功。

### 3 测试主从同步

创建一些数据测试：

```
SQLcreate DATABASE db1;
USE db1;

CREATE TABLE student ( 
	id INT primary KEY auto_increment, 
	name VARCHAR(255)
);

INSERT INTO student(name) VALUES("张三"),("李四"),("王五");

SELECT * FROM student;
```

切换到从库查看：

```
SQLSHOW DATABASES;
USE db1;
SELECT * FROM student;
```





- https://www.yyyzyyyz.cn/posts/5ba9bcd26307/

