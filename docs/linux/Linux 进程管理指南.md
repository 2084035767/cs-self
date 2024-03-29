Linux 进程是操作系统中运行的程序的实例。每个进程都有自己的内存空间和执行环境，它们彼此隔离，以确保安全性和稳定性。在 Linux 中管理进程是非常重要的，下面我将详细教你如何处理 Linux 进程。
### 1、查看进程
要查看正在运行的进程，你可以使用以下命令：
**ps** 命令：显示当前终端中的进程。
```
ps
```
**top** 命令：实时显示系统中正在运行的进程，按 CPU 和内存使用情况排序。
```
top
```
### 2、启动进程
要启动一个新进程，只需在终端中输入要运行的命令。例如：
```
ls
```
上述命令将启动一个新的进程来列出当前目录的文件和子目录。
### 3、后台运行进程
如果你希望将进程放入后台运行，可以使用 **&** 符号：
```
command &
```
例如，要在后台运行一个名为 **myapp** 的应用程序：
```
./myapp &
```
### 4. 暂停和恢复进程
要暂停一个正在运行的进程，可以使用 **Ctrl+Z** 键盘组合。然后，可以使用 **bg** 命令将其放入后台运行：
```
bg
```
要恢复一个在后台运行的进程，可以使用 **fg** 命令：
```
fg
```
### 5. 终止进程
使用 **kill** 命令终止进程，将 **PID** 替换为实际的进程 PID：
```
kill PID
```
如果需要强制终止一个进程，可以使用 **-9** 选项：
```
kill -9 PID
```
### 6. 查找进程信息
要查找有关特定进程的更多信息，可以使用 **ps** 命令，并提供进程的 PID：
```
ps -p PID
```
