# Dockerfile使用介绍

## Dockerfile 概念

Docker 镜像是一个特殊的文件系统，除了提供容器运行时所需的程序、库、资源、配置等文件外，还包含了一些为运行时准备的一些配置参数（如匿名卷、环境变量、用户等）。镜像不包含任何动态数据，其内容在构建之后也不会被改变。

镜像的定制实际上就是定制每一层所添加的配置、文件。如果我们可以把每一层修改、安装、构建、操作的命令都写入一个脚本，用这个脚本来构建、定制镜像，那么之前提及的无法重复的问题、镜像构建透明性的问题、体积的问题就都会解决。这个脚本就是 Dockerfile。

Dockerfile 是一个文本文件，其内包含了一条条的指令(Instruction)，每一条指令构建一层，因此每一条指令的内容，就是描述该层应当如何构建。有了 Dockerfile，当我们需要定制自己额外的需求时，只需在 Dockerfile 上添加或者修改指令，重新生成 image 即可，省去了敲命令的麻烦。

## Dockerfile 文件格式

Dockerfile文件格式如下：

```
##  Dockerfile文件格式

# This dockerfile uses the ubuntu image
# VERSION 2 - EDITION 1
# Author: docker_user
# Command format: Instruction [arguments / command] ..
 
# 1、第一行必须指定 基础镜像信息
FROM ubuntu
 
# 2、维护者信息
MAINTAINER docker_user docker_user@email.com
 
# 3、镜像操作指令
RUN echo "deb http://archive.ubuntu.com/ubuntu/ raring main universe" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y nginx
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
 
# 4、容器启动执行指令
CMD /usr/sbin/nginx


```

Dockerfile 分为四部分：**基础镜像信息、维护者信息、镜像操作指令、容器启动执行指令**。一开始必须要指明所基于的镜像名称，接下来一般会说明维护者信息；后面则是镜像操作指令，例如 RUN 指令。每执行一条RUN 指令，镜像添加新的一层，并提交；最后是 CMD 指令，来指明运行容器时的操作命令。

## 构建镜像

docker build 命令会根据 Dockerfile 文件及上下文构建新 Docker 镜像。构建上下文是指 Dockerfile 所在的本地路径或一个URL（Git仓库地址）。构建上下文环境会被递归处理，所以构建所指定的路径还包括了子目录，而URL还包括了其中指定的子模块。

将当前目录做为构建上下文时，可以像下面这样使用docker build命令构建镜像：

```
docker build .
Sending build context to Docker daemon  6.51 MB
...


```

说明：构建会在 Docker 后台守护进程（daemon）中执行，而不是`CLI`中。构建前，构建进程会将全部内容（递归）发送到守护进程。大多情况下，应该将一个空目录作为构建上下文环境，并将 Dockerfile 文件放在该目录下。

在构建上下文中使用的 Dockerfile 文件，是一个构建指令文件。为了提高构建性能，可以通过`.dockerignore`文件排除上下文目录下不需要的文件和目录。

在 Docker 构建镜像的第一步，docker CLI 会先在上下文目录中寻找`.dockerignore`文件，根据`.dockerignore` 文件排除上下文目录中的部分文件和目录，然后把剩下的文件和目录传递给 Docker 服务。

Dockerfile 一般位于构建上下文的根目录下，也可以通过`-f`指定该文件的位置：

```
docker build -f /path/to/a/Dockerfile .


```

构建时，还可以通过`-t`参数指定构建成镜像的仓库、标签。

## 镜像标签

```
docker build -t nginx/v3 .


```

如果存在多个仓库下，或使用多个镜像标签，就可以使用多个`-t`参数：

```
docker build -t nginx/v3:1.0.2 -t nginx/v3:latest .


```

在 Docker 守护进程执行 Dockerfile 中的指令前，首先会对 Dockerfile 进行语法检查，有语法错误时会返回：

```
docker build -t nginx/v3 .
Sending build context to Docker daemon 2.048 kB
Error response from daemon: Unknown instruction: RUNCMD


```

## 缓存

Docker 守护进程会一条一条的执行 Dockerfile 中的指令，而且会在每一步提交并生成一个新镜像，最后会输出最终镜像的ID。生成完成后，Docker 守护进程会自动清理你发送的上下文。 Dockerfile文件中的每条指令会被独立执行，并会创建一个新镜像，RUN cd /tmp等命令不会对下条指令产生影响。 Docker 会重用已生成的中间镜像，以加速docker build的构建速度。以下是一个使用了缓存镜像的执行过程：

```
$ docker build -t svendowideit/ambassador .
Sending build context to Docker daemon 15.36 kB
Step 1/4 : FROM alpine:3.2
 ---> 31f630c65071
Step 2/4 : MAINTAINER SvenDowideit@home.org.au
 ---> Using cache
 ---> 2a1c91448f5f
Step 3/4 : RUN apk update &&      apk add socat &&        rm -r /var/cache/
 ---> Using cache
 ---> 21ed6e7fbb73
Step 4/4 : CMD env | grep _TCP= | (sed 's/.*_PORT_\([0-9]*\)_TCP=tcp:\/\/\(.*\):\(.*\)/socat -t 100000000 TCP4-LISTEN:\1,fork,reuseaddr TCP4:\2:\3 \&/' && echo wait) | sh
 ---> Using cache
 ---> 7ea8aef582cc
Successfully built 7ea8aef582cc


```

构建缓存仅会使用本地父生成链上的镜像，如果不想使用本地缓存的镜像，也可以通过`--cache-from`指定缓存。指定后将不再使用本地生成的镜像链，而是从镜像仓库中下载。

## 寻找缓存的逻辑

Docker 寻找缓存的逻辑其实就是树型结构根据 Dockerfile 指令遍历子节点的过程。下图可以说明这个逻辑。

```
     FROM base_image:version           Dockerfile:
           +----------+                FROM base_image:version
           |base image|                RUN cmd1  --> use cache because we found base image
           +-----X----+                RUN cmd11 --> use cache because we found cmd1
                / \
               /   \
       RUN cmd1     RUN cmd2           Dockerfile:
       +------+     +------+           FROM base_image:version
       |image1|     |image2|           RUN cmd2  --> use cache because we found base image
       +---X--+     +------+           RUN cmd21 --> not use cache because there's no child node
          / \                                        running cmd21, so we build a new image here
         /   \
RUN cmd11     RUN cmd12
+-------+     +-------+
|image11|     |image12|
+-------+     +-------+


```

大部分指令可以根据上述逻辑去寻找缓存，除了 ADD 和  。这两个指令会复制文件内容到镜像内，除了指令相同以外，Docker 还会检查每个文件内容校验(不包括最后修改时间和最后访问时间)，如果校验不一致，则不会使用缓存。

除了这两个命令，Docker 并不会去检查容器内的文件内容，比如 `RUN apt-get -y update`，每次执行时文件可能都不一样，但是 Docker 认为命令一致，会继续使用缓存。这样一来，以后构建时都不会再重新运行`apt-get -y update`。

如果 Docker 没有找到当前指令的缓存，则会构建一个新的镜像，并且之后的所有指令都不会再去寻找缓存。

## 简单示例

接下来用一个简单的示例来感受一下 Dockerfile 是如何用来构建镜像启动容器。我们以定制 nginx 镜像为例，在一个空白目录中，建立一个文本文件，并命名为 Dockerfile：

```
mkdir mynginx
cd mynginx
vi Dockerfile


```

构建一个 Dockerfile 文件内容为：

```
FROM nginx
RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
vi Dockerfile


```

这个 Dockerfile 很简单，一共就两行涉及到了两条指令：FROM 和 RUN，FROM 表示获取指定基础镜像，RUN 执行命令，在执行的过程中重写了 nginx 的默认页面信息，将信息替换为：Hello, Docker!。

在 Dockerfile 文件所在目录执行：

```
docker build -t nginx:v1 .


```

命令最后有一个. 表示当前目录

构建完成之后，使用 `docker images` 命令查看所有镜像，如果存在 REPOSITORY 为 nginx 和 TAG 是 v1 的信息，就表示构建成功。

```
docker images
REPOSITORY                      TAG                 IMAGE ID            CREATED             SIZE
nginx                           v1                  8c92471de2cc        6 minutes ago       108.6 MB


```

接下来使用 docker run 命令来启动容器

```
docker run  --name docker_nginx_v1   -d -p 80:80 nginx:v1


```

这条命令会用 nginx 镜像启动一个容器，命名为`docker_nginx_v1`，并且映射了 80 端口，这样我们可以用浏览器去访问这个 nginx 服务器：`http://192.168.0.54/`，页面返回信息：



img

这样一个简单使用 Dockerfile 构建镜像，运行容器的示例就完成了！

## 修改容器内容

容器启动后，需要对容器内的文件进行进一步的完善，可以使用`docker exec -it xx bash`命令再次进行修改，以上面的示例为基础，修改 nginx 启动页面内容：

```
docker exec -it docker_nginx_v1   bash
root@3729b97e8226:/# echo '<h1>Hello, Docker neo!</h1>' > /usr/share/nginx/html/index.html
root@3729b97e8226:/# exit
exit


```

以交互式终端方式进入 docker_nginx_v1 容器，并执行了 bash 命令，也就是获得一个可操作的 Shell。然后，我们用`<h1>Hello, Docker neo!</h1>`覆盖了 `/usr/share/nginx/html/index.html` 的内容。

再次刷新浏览器，会发现内容被改变。



img

修改了容器的文件，也就是改动了容器的存储层，可以通过 docker diff 命令看到具体的改动。

```
docker diff docker_nginx_v1 
... 


```

文章链接

# Docker知识扫盲

## Docker与传统虚拟机区别

容器和 `VM`（虚拟机）的主要区别是:

- 容器提供了基于进程的隔离，而虚拟机提供了资源的完全隔离。
- 虚拟机可能需要一分钟来启动，而容器只需要一秒钟或更短。
- 容器使用宿主操作系统的内核，而虚拟机使用独立的内核。

## Dokcer平台的基本构成

- 客户端：用户使用 `Docker` 提供的工具（`CLI` 以及 `API` 等）来构建，上传镜像并发布命令来创建和启动容器
- `Docker` 主机：从 `Docker registry` 上下载镜像并启动容器
- `Docker registry`：`Docker` 镜像仓库，用于保存镜像，并提供镜像上传和下载

## Docker容器的状态机

一个容器在某个时刻可能处于以下几种状态之一：

- `created`：已经被创建 （使用 docker ps -a 命令可以列出）但是还没有被启动 （使用 docker ps 命令还无法列出）
- `running`：运行中
- `paused`：容器的进程被暂停了
- `restarting`：容器的进程正在重启过程中
- `exited`：上图中的 stopped 状态，表示容器之前运行过但是现在处于停止状态（要区别于 `created` 状态，它是指一个新创出的尚未运行过的容器）。可以通过 `start` 命令使其重新进入 `running` 状态
- `destroyed`：容器被删除了，再也不存在了

## Dokcer命令

把`Docker`的命令大概分类。

### 镜像操作

```
build     Build an image from a Dockerfile
commit    Create a new image from a container's changes
images    List images
load      Load an image from a tar archive or STDIN
pull      Pull an image or a repository from a registry
push      Push an image or a repository to a registry
rmi       Remove one or more images
search    Search the Docker Hub for images
tag       Tag an image into a repository
save      Save one or more images to a tar archive 
history   显示某镜像的历史
inspect   获取镜像的详细信息


```

### 容器及其中应用的生命周期操作

```
create    创建一个容器
kill      Kill one or more running containers
inspect   Return low-level information on a container, image or task
pause     Pause all processes within one or more containers
ps        List containers
rm        删除一个或者多个容器
rename    Rename a container
restart   Restart a container
run       创建并启动一个容器
start     启动一个处于停止状态的容器
stats     显示容器实时的资源消耗信息
stop      停止一个处于运行状态的容器
top       Display the running processes of a container
unpause   Unpause all processes within one or more containers
update    Update configuration of one or more containers
wait      Block until a container stops, then print its exit code
attach    Attach to a running container
exec      Run a command in a running container
port      List port mappings or a specific mapping for the container
logs      获取容器的日志


```

### 容器文件系统操作

```
cp         files/folders between a container and the local filesystem
diff      Inspect changes on a container's filesystem
export    Export a container's filesystem as a tar archive
import    Import the contents from a tarball to create a filesystem image


```

### Docker registry操作

```
login     Log in to a Docker registry.
logout    Log out from a Docker registry.


```

### Volume操作

```
volume    Manage Docker volumes


```

### 网络操作

```
network   Manage Docker networks


```

### Swarm相关操作

```
swarm     Manage Docker Swarm
service   Manage Docker services
node      Manage Docker Swarm nodes


```

### 系统操作

```
version   Show the Docker version information
events    持续返回docker 事件
info      显示Docker 主机系统范围内的信息


```

### 容器相关

```
# 查看运行中的容器
docker ps

# 查看所有容器
docker ps -a

# 退出容器
按Ctrl+D 即可退出当前容器【但退出后会停止容器】

# 退出不停止容器：
组合键：Ctrl+P+Q

# 启动容器
docker start 容器名或ID

# 进入容器
docker attach 容器名或ID

# 停止容器
docker stop 容器名或ID

# 暂停容器
docker pause 容器名或ID

#继续容器
docker unpause 容器名或ID

# 删除容器
docker rm 容器名或ID

# 删除全部容器--慎用
docker stop $(docker ps -q) & docker rm $(docker ps -aq)

#保存容器，生成镜像
docker commit 容器ID 镜像名称

#从 host 拷贝文件到 container 里面
docker cp /home/soft centos:/webapp


```

## docker run 和start的区别

`docker run` 只在第一次运行时使用，将镜像放到容器中，以后再次启动这个容器时，只需要使用命令`docker start` 即可。

- `docker run`相当于执行了两步操作：将镜像放入容器中（`docker create`）,然后将容器启动，使之变成运行时容器（`docker start`）。
- `docker start`的作用是，重新启动已存在的镜像。也就是说，如果使用这个命令，我们必须事先知道这个容器的`ID`，或者这个容器的名字，我们可以使用`docker ps`找到这个容器的信息。

## docker配置

更改存储目录：

```
#复制docker存储目录
rsync -aXS /var/lib/docker/. /home/docker

#更改 docker 存储文件目录
ln -s  /home/docker  /var/lib/docker


```

获取ip：

```
docker inspect <container id>


```

要获取所有容器名称及其IP地址只需一个命令：

```
docker inspect -f '{{.Name}} - {{.NetworkSettings.IPAddress }}' $(docker ps -aq)

docker inspect --format='{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aq)


```

- https://www.cayzlh.com/post/3773573700/

# Dockerfile常用指令

## Dockerfile 指令详解

### 1 FROM 指定基础镜像

FROM 指令用于指定其后构建新镜像所使用的基础镜像。FROM 指令必是 Dockerfile 文件中的首条命令，启动构建流程后，Docker 将会基于该镜像构建新镜像，FROM 后的命令也会基于这个基础镜像。

FROM语法格式为：

```
FROM <image>


```

或

```
FROM <image>:<tag>


```

或

```
FROM <image>:<digest>


```

通过 FROM 指定的镜像，可以是任何有效的基础镜像。FROM 有以下限制：

- FROM 必须 是 Dockerfile 中第一条非注释命令
- 在一个 Dockerfile 文件中创建多个镜像时，FROM 可以多次出现。只需在每个新命令 FROM 之前，记录提交上次的镜像 ID。
- tag 或 digest 是可选的，如果不使用这两个值时，会使用 latest 版本的基础镜像

### 2 RUN 执行命令

在镜像的构建过程中执行特定的命令，并生成一个中间镜像。格式:

```
#shell格式
RUN <command>
#exec格式
RUN ["executable", "param1", "param2"]


```

- RUN 命令将在当前 image 中执行任意合法命令并提交执行结果。命令执行提交后，就会自动执行 Dockerfile 中的下一个指令。
- 层级 RUN 指令和生成提交是符合 Docker 核心理念的做法。它允许像版本控制那样，在任意一个点，对 image 镜像进行定制化构建。
- RUN 指令创建的中间镜像会被缓存，并会在下次构建中使用。如果不想使用这些缓存镜像，可以在构建时指定 `--no-cache` 参数，如：`docker build --no-cache`。

### 3  复制文件

格式：

```
 <源路径>... <目标路径>
 ["<源路径1>",... "<目标路径>"]


```

和 RUN 指令一样，也有两种格式，一种类似于命令行，一种类似于函数调用。 指令将从构建上下文目录中 <源路径> 的文件/目录复制到新的一层的镜像内的`<目标路径>`位置。比如：

```
 ../../../package.json /usr/src/app/


```

`<源路径>`可以是多个，甚至可以是通配符，其通配符规则要满足 Go 的 filepath.Match 规则，如：

```
 hom* /mydir/
 hom?.txt /mydir/


```

`<目标路径>`可以是容器内的绝对路径，也可以是相对于工作目录的相对路径（工作目录可以用 WORKDIR 指令来指定）。目标路径不需要事先创建，如果目录不存在会在复制文件前先行创建缺失目录。

此外，还需要注意一点，使用  指令，源文件的各种元数据都会保留。比如读、写、执行权限、文件变更时间等。这个特性对于镜像定制很有用。特别是构建相关文件都在使用 Git 进行管理的时候。

### 4 ADD 更高级的复制文件

ADD 指令和  的格式和性质基本一致。但是在  基础上增加了一些功能。比如`<源路径>`可以是一个 URL，这种情况下，Docker 引擎会试图去下载这个链接的文件放到`<目标路径>`去。

在构建镜像时，复制上下文中的文件到镜像内，格式：

```
ADD <源路径>... <目标路径>
ADD ["<源路径>",... "<目标路径>"]


```

**注意**
如果 docker 发现文件内容被改变，则接下来的指令都不会再使用缓存。关于复制文件时需要处理的/，基本跟正常的  一致

### 5 ENV 设置环境变量

格式有两种：

```
ENV <key> <value>
ENV <key1>=<value1> <key2>=<value2>...


```

这个指令很简单，就是设置环境变量而已，无论是后面的其它指令，如 RUN，还是运行时的应用，都可以直接使用这里定义的环境变量。

```
ENV VERSION=1.0 DEBUG=on \
    NAME="Happy Feet"


```

这个例子中演示了如何换行，以及对含有空格的值用双引号括起来的办法，这和 Shell 下的行为是一致的。

### 6 EXPOSE

为构建的镜像设置监听端口，使容器在运行时监听。格式：

```
EXPOSE <port> [<port>...]


```

EXPOSE 指令并不会让容器监听 host 的端口，如果需要，需要在 docker run 时使用 `-p`、`-P` 参数来发布容器端口到 host 的某个端口上。

### 7 VOLUME 定义匿名卷

VOLUME用于创建挂载点，即向基于所构建镜像创始的容器添加卷：

```
VOLUME ["/data"]


```

一个卷可以存在于一个或多个容器的指定目录，该目录可以绕过联合文件系统，并具有以下功能：

- 卷可以容器间共享和重用
- 容器并不一定要和其它容器共享卷
- 修改卷后会立即生效
- 对卷的修改不会对镜像产生影响
- 卷会一直存在，直到没有任何容器在使用它

VOLUME 让我们可以将源代码、数据或其它内容添加到镜像中，而又不并提交到镜像中，并使我们可以多个容器间共享这些内容。

### 8 WORKDIR 指定工作目录

WORKDIR用于在容器内设置一个工作目录：

```
WORKDIR /path/to/workdir


```

通过WORKDIR设置工作目录后，Dockerfile 中其后的命令 RUN、CMD、ENTRYPOINT、ADD、 等命令都会在该目录下执行。 如，使用WORKDIR设置工作目录：

```
WORKDIR /a
WORKDIR b
WORKDIR c
RUN pwd


```

在以上示例中，pwd 最终将会在 `/a/b/c` 目录中执行。在使用 docker run 运行容器时，可以通过`-w`参数覆盖构建时所设置的工作目录。

### 9 USER 指定当前用户

USER 用于指定运行镜像所使用的用户：

```
USER daemon


```

使用USER指定用户时，可以使用用户名、UID 或 GID，或是两者的组合。以下都是合法的指定试：

```
USER user
USER user:group
USER uid
USER uid:gid
USER user:gid
USER uid:group


```

使用USER指定用户后，Dockerfile 中其后的命令 RUN、CMD、ENTRYPOINT 都将使用该用户。镜像构建完成后，通过 docker run 运行容器时，可以通过 `-u` 参数来覆盖所指定的用户。

### 10 CMD

CMD用于指定在容器启动时所要执行的命令。CMD 有以下三种格式：

```
CMD ["executable","param1","param2"]
CMD ["param1","param2"]
CMD command param1 param2


```

省略可执行文件的 exec 格式，这种写法使 CMD 中的参数当做 ENTRYPOINT 的默认参数，此时 ENTRYPOINT 也应该是 exec 格式，具体与 ENTRYPOINT 的组合使用，参考 ENTRYPOINT。

**注意**
与 RUN 指令的区别：RUN 在构建的时候执行，并生成一个新的镜像，CMD 在容器运行的时候执行，在构建时不进行任何操作。

### 11 ENTRYPOINT

ENTRYPOINT 用于给容器配置一个可执行程序。也就是说，每次使用镜像创建容器时，通过 ENTRYPOINT 指定的程序都会被设置为默认程序。ENTRYPOINT 有以下两种形式：

```
ENTRYPOINT ["executable", "param1", "param2"]
ENTRYPOINT command param1 param2


```

ENTRYPOINT 与 CMD 非常类似，不同的是通过`docker run`执行的命令不会覆盖 ENTRYPOINT，而`docker run`命令中指定的任何参数，都会被当做参数再次传递给 ENTRYPOINT。Dockerfile 中只允许有一个 ENTRYPOINT 命令，多指定时会覆盖前面的设置，而只执行最后的 ENTRYPOINT 指令。

`docker run`运行容器时指定的参数都会被传递给 ENTRYPOINT ，且会覆盖 CMD 命令指定的参数。如，执行`docker run <image> -d`时，-d 参数将被传递给入口点。

也可以通过`docker run --entrypoint`重写 ENTRYPOINT 入口点。如：可以像下面这样指定一个容器执行程序：

```
ENTRYPOINT ["/usr/bin/nginx"]


```

完整构建代码：

```
# Version: 0.0.3
FROM ubuntu:16.04
MAINTAINER 何民三 "cn.liuht@gmail.com"
RUN apt-get update
RUN apt-get install -y nginx
RUN echo 'Hello World, 我是个容器' \ 
   > /var/www/html/index.html
ENTRYPOINT ["/usr/sbin/nginx"]
EXPOSE 80


```

使用docker build构建镜像，并将镜像指定为 itbilu/test：

```
docker build -t="itbilu/test" .


```

构建完成后，使用itbilu/test启动一个容器：

```
docker run -i -t  itbilu/test -g "daemon off;"


```

在运行容器时，我们使用了 `-g "daemon off;"`，这个参数将会被传递给 ENTRYPOINT，最终在容器中执行的命令为 `/usr/sbin/nginx -g "daemon off;"`。

### 12 LABEL

LABEL用于为镜像添加元数据，元数以键值对的形式指定：

```
LABEL <key>=<value> <key>=<value> <key>=<value> ...


```

使用LABEL指定元数据时，一条LABEL指定可以指定一或多条元数据，指定多条元数据时不同元数据之间通过空格分隔。推荐将所有的元数据通过一条LABEL指令指定，以免生成过多的中间镜像。 如，通过LABEL指定一些元数据：

```
LABEL version="1.0" description="这是一个Web服务器" by="IT笔录"


```

指定后可以通过docker inspect查看：

```
docker inspect itbilu/test
"Labels": {
    "version": "1.0",
    "description": "这是一个Web服务器",
    "by": "IT笔录"
},


```

### 13 ARG

ARG用于指定传递给构建运行时的变量：

```
ARG <name>[=<default value>]


```

如，通过ARG指定两个变量：

```
ARG site
ARG build_user=IT笔录


```

以上我们指定了 site 和 build_user 两个变量，其中 build_user 指定了默认值。在使用 docker build 构建镜像时，可以通过 `--build-arg <varname>=<value>` 参数来指定或重设置这些变量的值。

```
docker build --build-arg site=itiblu.com -t itbilu/test .


```

这样我们构建了 itbilu/test 镜像，其中site会被设置为 itbilu.com，由于没有指定 build_user，其值将是默认值 IT 笔录。

### 14 ONBUILD

ONBUILD用于设置镜像触发器：

```
ONBUILD [INSTRUCTION]


```

当所构建的镜像被用做其它镜像的基础镜像，该镜像中的触发器将会被钥触发。 如，当镜像被使用时，可能需要做一些处理：

```
[...]
ONBUILD ADD . /app/src
ONBUILD RUN /usr/local/bin/python-build --dir /app/src
[...]


```

### 15 STOPSIGNAL

STOPSIGNAL用于设置停止容器所要发送的系统调用信号：

```
STOPSIGNAL signal


```

所使用的信号必须是内核系统调用表中的合法的值，如：SIGKILL。

### 16 SHELL

SHELL用于设置执行命令（shell式）所使用的的默认 shell 类型：

```
SHELL ["executable", "parameters"]


```

SHELL在Windows环境下比较有用，Windows 下通常会有 cmd 和 powershell 两种 shell，可能还会有 sh。这时就可以通过 SHELL 来指定所使用的 shell 类型：

```
FROM microsoft/windowsservercore

# Executed as cmd /S /C echo default
RUN echo default

# Executed as cmd /S /C powershell -command Write-Host default
RUN powershell -command Write-Host default

# Executed as powershell -command Write-Host hello
SHELL ["powershell", "-command"]
RUN Write-Host hello

# Executed as cmd /S /C echo hello
SHELL ["cmd", "/S"", "/C"]
RUN echo hello


```

## Dockerfile 使用经验

### Dockerfile 示例

**构建Nginx运行环境**

```
# 指定基础镜像
FROM sameersbn/ubuntu:14.04.20161014

# 维护者信息
MAINTAINER sameer@damagehead.com

# 设置环境
ENV RTMP_VERSION=1.1.10 \
    NPS_VERSION=1.11.33.4 \
    LIBAV_VERSION=11.8 \
    NGINX_VERSION=1.10.1 \
    NGINX_USER=www-data \
    NGINX_SITECONF_DIR=/etc/nginx/sites-enabled \
    NGINX_LOG_DIR=/var/log/nginx \
    NGINX_TEMP_DIR=/var/lib/nginx \
    NGINX_SETUP_DIR=/var/cache/nginx

# 设置构建时变量，镜像建立完成后就失效
ARG BUILD_LIBAV=false
ARG WITH_DEBUG=false
ARG WITH_PAGESPEED=true
ARG WITH_RTMP=true

# 复制本地文件到容器目录中
 setup/ ${NGINX_SETUP_DIR}/
RUN bash ${NGINX_SETUP_DIR}/install.sh

# 复制本地配置文件到容器目录中
 nginx.conf /etc/nginx/nginx.conf
 entrypoint.sh /sbin/entrypoint.sh

# 运行指令
RUN chmod 755 /sbin/entrypoint.sh

# 允许指定的端口
EXPOSE 80/tcp 443/tcp 1935/tcp

# 指定网站目录挂载点
VOLUME ["${NGINX_SITECONF_DIR}"]

ENTRYPOINT ["/sbin/entrypoint.sh"]
CMD ["/usr/sbin/nginx"]


```

**构建tomcat 环境**

Dockerfile文件

```
# 指定基于的基础镜像
FROM ubuntu:13.10  

# 维护者信息
MAINTAINER zhangjiayang "zhangjiayang@sczq.com.cn"  
  
# 镜像的指令操作
# 获取APT更新的资源列表
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe"> /etc/apt/sources.list
# 更新软件
RUN apt-get update  
  
# Install curl  
RUN apt-get -y install curl  
  
# Install JDK 7  
RUN cd /tmp &&  curl -L 'http://download.oracle.com/otn-pub/java/jdk/7u65-b17/jdk-7u65-linux-x64.tar.gz' -H 'Cookie: oraclelicense=accept-securebackup-cookie; gpw_e24=Dockerfile' | tar -xz  
RUN mkdir -p /usr/lib/jvm  
RUN mv /tmp/jdk1.7.0_65/ /usr/lib/jvm/java-7-oracle/  
  
# Set Oracle JDK 7 as default Java  
RUN update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-7-oracle/bin/java 300     
RUN update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/java-7-oracle/bin/javac 300     

# 设置系统环境
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle/  
  
# Install tomcat7  
RUN cd /tmp && curl -L 'http://archive.apache.org/dist/tomcat/tomcat-7/v7.0.8/bin/apache-tomcat-7.0.8.tar.gz' | tar -xz  
RUN mv /tmp/apache-tomcat-7.0.8/ /opt/tomcat7/  
  
ENV CATALINA_HOME /opt/tomcat7  
ENV PATH $PATH:$CATALINA_HOME/bin  

# 复件tomcat7.sh到容器中的目录 
ADD tomcat7.sh /etc/init.d/tomcat7  
RUN chmod 755 /etc/init.d/tomcat7  
  
# Expose ports.  指定暴露的端口
EXPOSE 8080  
  
# Define default command.  
ENTRYPOINT service tomcat7 start && tail -f /opt/tomcat7/logs/catalina.out


```

`tomcat7.sh`命令文件

```
export JAVA_HOME=/usr/lib/jvm/java-7-oracle/  
export TOMCAT_HOME=/opt/tomcat7  
  
case $1 in  
start)  
  sh $TOMCAT_HOME/bin/startup.sh  
;;  
stop)  
  sh $TOMCAT_HOME/bin/shutdown.sh  
;;  
restart)  
  sh $TOMCAT_HOME/bin/shutdown.sh  
  sh $TOMCAT_HOME/bin/startup.sh  
;;  
esac  
exit 0


```

### 原则与建议

- 容器轻量化。从镜像中产生的容器应该尽量轻量化，能在足够短的时间内停止、销毁、重新生成并替换原来的容器。
- 使用 `.gitignore`。在大部分情况下，Dockerfile 会和构建所需的文件放在同一个目录中，为了提高构建的性能，应该使用 `.gitignore` 来过滤掉不需要的文件和目录。
- 为了减少镜像的大小，减少依赖，仅安装需要的软件包。
- 一个容器只做一件事。解耦复杂的应用，分成多个容器，而不是所有东西都放在一个容器内运行。如一个 Python Web 应用，可能需要 Server、DB、Cache、MQ、Log 等几个容器。一个更加极端的说法：One process per container。
- 减少镜像的图层。不要多个 Label、ENV 等标签。
- 对续行的参数按照字母表排序，特别是使用`apt-get install -y`安装包的时候。
- 使用构建缓存。如果不想使用缓存，可以在构建的时候使用参数`--no-cache=true`来强制重新生成中间镜像。