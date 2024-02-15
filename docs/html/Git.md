# Git简介

`Git` 是一种分布式版本控制系统，它可以不受网络连接的限制，加上其它众多优点，目前已经成为程序开发人员做项目版本管理时的首选，非开发人员也可以用 `Git` 来做自己的文档版本管理工具。

大概是大二的时候开始接触和使用Git，从一开始的零接触到现在的重度依赖，真是感叹 `Git` 的强大。

`Git` 的api很多，但其实平时项目中90%的需求都只需要用到几个基本的功能即可，所以本文将从 `实用主义` 和 `深入探索` 2个方面去谈谈如何在项目中使用 `Git`，一般来说，看完 `实用主义` 这一节就可以开始在项目中动手用。

> “
>
> 说明：本文的操作都是基于 Mac 系统

# 实用主义

## 准备阶段

进入 Git官网 下载合适你的安装包，安装好 `Git` 后，打开命令行工具，进入工作文件夹（*为了便于理解我们在系统桌面上演示*），创建一个新的demo文件夹。

![图片](data:image/png;base64,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AC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgACtACAAC0AIEALAAjQAgDCKazQRwBA8cHeKfQRAFBsvMPeLvQhAFBsvM2OFPoQACg2jrBh9KIA0HhnmI1DcwGAxpFxrPq4twp9FAAUE28dV81qEil4AYDNW6lEDauoTZx4BOMLAATvHDkxUVvBKipqq+uGj7z9jnEKAJHGeOftI8N11bUVFf8Pj6nRAHr36FYAAAAASUVORK5CYII=)

进入 Github网站 注册一个账号并登录，进入 我的博客，点击 `Clone or download` ，再点击 `Use HTTPS` ，复制项目地址 `https://github.com/gafish/gafish.github.com.git` 备用。

再回到命令行工具，一切就绪，接下来进入本文的重点。

## 常用操作

所谓实用主义，就是掌握了以下知识就可以玩转 `Git`，轻松应对90%以上的需求。以下是实用主义型的Git命令列表，先大致看一下

- `git clone`
- `git config`
- `git branch`
- `git checkout`
- `git status`
- `git add`
- `git commit`
- `git push`
- `git pull`
- `git log`
- `git tag`

接下来，将通过对 我的博客 仓库进行实例操作，讲解如何使用 `Git` 拉取代码到提交代码的整个流程。

### git clone

> “
>
> 从git服务器拉取代码

```
git clone https://github.com/gafish/gafish.github.com.git
```

代码下载完成后在当前文件夹中会有一个 `gafish.github.com` 的目录，通过 `cd gafish.github.com` 命令进入目录。

### git config

> “
>
> 配置开发者用户名和邮箱

```
git config user.name gafish
git config user.email gafish@qqqq.com
```

每次代码提交的时候都会生成一条提交记录，其中会包含当前配置的用户名和邮箱。

### git branch

> “
>
> 创建、重命名、查看、删除项目分支，通过 `Git` 做项目开发时，一般都是在开发分支中进行，开发完成后合并分支到主干。

```
git branch daily/0.0.0
```

创建一个名为 `daily/0.0.0` 的日常开发分支，分支名只要不包括特殊字符即可。

```
git branch -m daily/0.0.0 daily/0.0.1
```

如果觉得之前的分支名不合适，可以为新建的分支重命名，重命名分支名为 `daily/0.0.1`

```
git branch
```

通过不带参数的branch命令可以查看当前项目分支列表

```
git branch -d daily/0.0.1
```

如果分支已经完成使命则可以通过 `-d` 参数将分支删除，这里为了继续下一步操作，暂不执行删除操作

### git checkout

> “
>
> 切换分支

```
git checkout daily/0.0.1
```

切换到 `daily/0.0.1` 分支，后续的操作将在这个分支上进行

### git status

> “
>
> 查看文件变动状态

通过任何你喜欢的编辑器对项目中的 `README.md` 文件做一些改动，保存。

```
git status
```

通过 `git status` 命令可以看到文件当前状态 `Changes not staged for commit:` （*改动文件未提交到暂存区*）

```
On branch daily/0.0.1
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)
    modified:   README.md
no changes added to commit (use "git add" and/or "git commit -a")
```

### git add

> “
>
> 添加文件变动到暂存区

```
git add README.md
```

通过指定文件名 `README.md` 可以将该文件添加到暂存区，如果想添加所有文件可用 `git add .` 命令，这时候可通过 `git status` 看到文件当前状态 `Changes to be committed:` （*文件已提交到暂存区*）

```
On branch daily/0.0.1
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
    modified:   README.md
```

### git commit

> “
>
> 提交文件变动到版本库

```
git commit -m '这里写提交原因'
```

通过 `-m` 参数可直接在命令行里输入提交描述文本

### git push

> “
>
> 将本地的代码改动推送到服务器

```
git push origin daily/0.0.1
```

`origin` 指代的是当前的git服务器地址，这行命令的意思是把 `daily/0.0.1` 分支推送到服务器，当看到命令行返回如下字符表示推送成功了。

```
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 267 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local objects.
To https://github.com/gafish/gafish.github.com.git
 * [new branch]      daily/0.0.1 -> daily/0.0.1
```

现在我们回到Github网站的项目首页，点击 `Branch:master` 下拉按钮，就会看到刚才推送的 `daily/00.1` 分支了

### git pull

> “
>
> 将服务器上的最新代码拉取到本地

```
git pull origin daily/0.0.1
```

如果其它项目成员对项目做了改动并推送到服务器，我们需要将最新的改动更新到本地，这里我们来模拟一下这种情况。

进入Github网站的项目首页，再进入 `daily/0.0.1` 分支，在线对 `README.md` 文件做一些修改并保存，然后在命令中执行以上命令，它将把刚才在线修改的部分拉取到本地，用编辑器打开 `README.md` ，你会发现文件已经跟线上的内容同步了。

*如果线上代码做了变动，而你本地的代码也有变动，拉取的代码就有可能会跟你本地的改动冲突，一般情况下 `Git` 会自动处理这种冲突合并，但如果改动的是同一行，那就需要手动来合并代码，编辑文件，保存最新的改动，再通过 `git add .` 和 `git commit -m 'xxx'` 来提交合并。*

### git log

> “
>
> 查看版本提交记录

```
git log
```

通过以上命令，我们可以查看整个项目的版本提交记录，它里面包含了`提交人`、`日期`、`提交原因`等信息，得到的结果如下：

```
commit c334730f8dba5096c54c8ac04fdc2b31ede7107a
Author: gafish <gafish@qqqq.com>
Date:   Wed Jan 11 09:44:13 2017 +0800
    Update README.md
commit ba6e3d21fcb1c87a718d2a73cdd11261eb672b2a
Author: gafish <gafish@qqqq.com>
Date:   Wed Jan 11 09:31:33 2017 +0800
    test
.....
```

提交记录可能会非常多，按 `J` 键往下翻，按 `K` 键往上翻，按 `Q` 键退出查看

### git tag

> “
>
> 为项目标记里程碑

```
git tag publish/0.0.1
git push origin publish/0.0.1
```

当我们完成某个功能需求准备发布上线时，应该将此次完整的项目代码做个标记，并将这个标记好的版本发布到线上，这里我们以 `publish/0.0.1` 为标记名并发布，当看到命令行返回如下内容则表示发布成功了

```
Total 0 (delta 0), reused 0 (delta 0)
To https://github.com/gafish/gafish.github.com.git
 * [new tag]         publish/0.0.1 -> publish/0.0.1
```

### .gitignore

> “
>
> 设置哪些内容不需要推送到服务器，这是一个配置文件

```
touch .gitignore
```

`.gitignore` 不是 `Git` 命令，而在项目中的一个文件，通过设置 `.gitignore` 的内容告诉 `Git` 哪些文件应该被忽略不需要推送到服务器，通过以上命令可以创建一个 `.gitignore` 文件，并在编辑器中打开文件，每一行代表一个要忽略的文件或目录，如：

```
demo.html
build/
```

以上内容的意思是 `Git` 将忽略 `demo.html` 文件 和 `build/` 目录，这些内容不会被推送到服务器上

### 小结

通过掌握以上这些基本命令就可以在项目中开始用起来了，如果追求实用，那关于 `Git` 的学习就可以到此结束了，偶尔遇到的问题也基本上通过 `Google` 也能找到答案，如果想深入探索 `Git` 的高阶功能，那就继续往下看 `深入探索` 部分。

# 深入探索

## 基本概念

### 工作区（*Working Directory*）

就是你在电脑里能看到的目录，比如上文中的 `gafish.github.com` 文件夹就是一个工作区

### 本地版本库（*Local Repository*）

工作区有一个隐藏目录 `.git`，这个不算工作区，而是 `Git` 的版本库。



### 暂存区（*stage*）

本地版本库里存了很多东西，其中最重要的就是称为 `stage`（或者叫index）的暂存区，还有 `Git` 为我们自动创建的第一个分支 `master`，以及指向 `master` 的一个指针叫 `HEAD`。

### 远程版本库（*Remote Repository*）

一般指的是 `Git` 服务器上所对应的仓库，本文的示例所在的`github`仓库就是一个远程版本库

### 以上概念之间的关系

`工作区`、`暂存区`、`本地版本库`、`远程版本库`之间几个常用的 `Git` 操作流程如下图所示：



### 分支（*Branch*）

分支是为了将修改记录的整个流程分开存储，让分开的分支不受其它分支的影响，所以在同一个数据库里可以同时进行多个不同的修改



### 主分支（*Master*）

前面提到过 `master` 是 `Git` 为我们自动创建的第一个分支，也叫主分支，其它分支开发完成后都要合并到 `master`





### 标签（*Tag*）

标签是用于标记特定的点或提交的历史，通常会用来标记发布版本的名称或版本号（如：`publish/0.0.1`），虽然标签看起来有点像分支，但打上标签的提交是固定的，不能随意的改动，参见上图中的`1.0` / `2.0` / `3.0`

### HEAD

`HEAD` 指向的就是当前分支的最新提交



> “
>
> 以上概念了解的差不多，那就可以继续往下看，下面将以具体的操作类型来讲解 `Git` 的高阶用法

## 操作文件

### git add

> “
>
> 添加文件到暂存区

```
git add -i
```

通过此命令将打开交互式子命令系统，你将看到如下子命令

```
***Commands***
  1: status      2: update      3: revert      4: add untracked
  5: patch      6: diff      7: quit      8: help
```

通过输入序列号或首字母可以选择相应的功能，具体的功能解释如下：

- `status`：功能上和 `git add -i` 相似，没什么鸟用
- `update`：详见下方 `git add -u`
- `revert`：把已经添加到暂存区的文件从暂存区剔除，其操作方式和 `update` 类似
- `add untracked`：可以把新增的文件添加到暂存区，其操作方式和 `update` 类似
- `patch`：详见下方 `git add -p`
- `diff`：比较暂存区文件和本地版本库的差异，其操作方式和 `update` 类似
- `quit`：退出 `git add -i` 命令系统
- `help`：查看帮助信息

```
git add -p
```

直接进入交互命令中最有用的 `patch` 模式

这是交互命令中最有用的模式，其操作方式和 `update` 类似，选择后 `Git` 会显示这些文件的当前内容与本地版本库中的差异，然后您可以自己决定是否添加这些修改到暂存区，在命令行 `Stage deletion [y,n,q,a,d,/,?]?` 后输入 `y,n,q,a,d,/,?` 其中一项选择操作方式，具体功能解释如下：

- y：接受修改
- n：忽略修改
- q：退出当前命令
- a：添加修改
- d：放弃修改
- /：通过正则表达式匹配修改内容
- ?：查看帮助信息

```
git add -u
```

直接进入交互命令中的 `update` 模式

它会先列出工作区 `修改` 或 `删除` 的文件列表，`新增` 的文件不会被显示，在命令行 `Update>>` 后输入相应的列表序列号表示选中该项，回车继续选择，如果已选好，直接回车回到命令主界面

```
git add --ignore-removal .
```

添加工作区 `修改` 或 `新增` 的文件列表， `删除` 的文件不会被添加

### git commit

> “
>
> 把暂存区的文件提交到本地版本库

```
git commit -m '第一行提交原因'  -m '第二行提交原因'
```

不打开编辑器，直接在命令行中输入多行提交原因

```
git commit -am '提交原因'
```

将工作区 `修改` 或 `删除` 的文件提交到本地版本库， `新增` 的文件不会被提交

```
git commit --amend -m '提交原因'
```

修改最新一条提交记录的提交原因

```
git commit -C HEAD
```

将当前文件改动提交到 `HEAD` 或当前分支的历史ID

### git mv

> “
>
> 移动或重命名文件、目录

```
git mv a.md b.md -f
```

将 `a.md` 重命名为 `b.md` ，同时添加变动到暂存区，加 `-f` 参数可以强制重命名，相比用 `mv a.md b.md` 命令省去了 `git add` 操作

### git rm

> “
>
> 从工作区和暂存区移除文件

```
git rm b.md
```

从工作区和暂存区移除文件 `b.md` ，同时添加变动到暂存区，相比用 `rm b.md` 命令省去了 `git add` 操作

```
git rm src/ -r
```

允许从工作区和暂存区移除目录

### git status

```
git status -s
```

以简短方式查看工作区和暂存区文件状态，示例如下：

```
 M demo.html
?? test.html
git status --ignored
```

查看工作区和暂存区文件状态，包括被忽略的文件

## 操作分支

### git branch

> “
>
> 查看、创建、删除分支

```
git branch -a
```

查看本地版本库和远程版本库上的分支列表

```
git branch -r
```

查看远程版本库上的分支列表，加上 `-d` 参数可以删除远程版本库上的分支

```
git branch -D
```

分支未提交到本地版本库前强制删除分支

```
git branch -vv
```

查看带有最后提交id、最近提交原因等信息的本地版本库分支列表



### git merge

> “
>
> 将其它分支合并到当前分支

```
git merge --squash
```

将待合并分支上的 `commit` 合并成一个新的 `commit` 放入当前分支，适用于待合并分支的提交记录不需要保留的情况

```
git merge --no-ff
```

默认情况下，`Git` 执行"`快进式合并`"（fast-farward merge），会直接将 `Master` 分支指向 `Develop` 分支，使用 `--no-ff` 参数后，会执行正常合并，在 `Master` 分支上生成一个新节点，保证版本演进更清晰。



```
git merge --no-edit
```

在没有冲突的情况下合并，不想手动编辑提交原因，而是用 `Git` 自动生成的类似 `Merge branch 'test'` 的文字直接提交

### git checkout

> “
>
> 切换分支

```
git checkout -b daily/0.0.1
```

创建 `daily/0.0.1` 分支，同时切换到这个新创建的分支

```
git checkout HEAD demo.html
```

从本地版本库的 `HEAD`（也可以是提交ID、分支名、Tag名） 历史中检出 `demo.html` 覆盖当前工作区的文件，如果省略 `HEAD` 则是从暂存区检出

```
git checkout --orphan new_branch
```

这个命令会创建一个全新的，完全没有历史记录的新分支，但当前源分支上所有的最新文件都还在，真是强迫症患者的福音，但这个新分支必须做一次 `git commit` 操作后才会真正成为一个新分支。

```
git checkout -p other_branch
```

这个命令主要用来比较两个分支间的差异内容，并提供交互式的界面来选择进一步的操作，这个命令不仅可以比较两个分支间的差异，还可以比较单个文件的差异。

### git stash

> “
>
> 在 `Git` 的栈中保存当前修改或删除的工作进度，当你在一个分支里做某项功能开发时，接到通知把昨天已经测试完没问题的代码发布到线上，但这时你已经在这个分支里加入了其它未提交的代码，这个时候就可以把这些未提交的代码存到栈里。

```
git stash
```

将未提交的文件保存到Git栈中

```
git stash list
```

查看栈中保存的列表

```
git stash show stash@{0}
```

显示栈中其中一条记录

```
git stash drop stash@{0}
```

移除栈中其中一条记录

```
git stash pop
```

从Git栈中检出最新保存的一条记录，并将它从栈中移除

```
git stash apply stash@{0}
```

从Git栈中检出其中一条记录，但不从栈中移除

```
git stash branch new_banch
```

把当前栈中最近一次记录检出并创建一个新分支

```
git stash clear
```

清空栈里的所有记录

```
git stash create
```

为当前修改或删除的文件创建一个自定义的栈并返回一个ID，此时并未真正存储到栈里

```
git stash store xxxxxx
```

将 `create` 方法里返回的ID放到 `store` 后面，此时在栈里真正创建了一个记录，但当前修改或删除的文件并未从工作区移除

```
$ git stash create
09eb9a97ad632d0825be1ece361936d1d0bdb5c7
$ git stash store 09eb9a97ad632d0825be1ece361936d1d0bdb5c7
$ git stash list
stash@{0}: Created via "git stash store".
```

## 操作历史

### git log

> “
>
> 显示提交历史记录

```
git log -p
```

显示带提交差异对比的历史记录

```
git log demo.html
```

显示 `demo.html` 文件的历史记录

```
git log --since="2 weeks ago"
```

显示2周前开始到现在的历史记录，其它时间可以类推

```
git log --before="2 weeks ago"
```

显示截止到2周前的历史记录，其它时间可以类推

```
git log -10
```

显示最近10条历史记录

```
git log f5f630a..HEAD
```

显示从提交ID `f5f630a` 到 `HEAD` 之间的记录，`HEAD` 可以为空或其它提交ID

```
git log --pretty=oneline
```

在一行中输出简短的历史记录

```
git log --pretty=format:"%h"
```

格式化输出历史记录

`Git` 用各种 `placeholder` 来决定各种显示内容，我挑几个常用的显示如下：

- %H: commit hash
- %h: 缩短的commit hash
- %T: tree hash
- %t: 缩短的 tree hash
- %P: parent hashes
- %p: 缩短的 parent hashes
- %an: 作者名字
- %aN: mailmap的作者名
- %ae: 作者邮箱
- %ad: 日期 (--date= 制定的格式)
- %ar: 日期, 相对格式(1 day ago)
- %cn: 提交者名字
- %ce: 提交者 email
- %cd: 提交日期 (--date= 制定的格式)
- %cr: 提交日期, 相对格式(1 day ago)
- %d: ref名称
- %s: commit信息标题
- %b: commit信息内容
- %n: 换行

### git cherry-pick

> “
>
> 合并分支的一条或几条提交记录到当前分支末梢

```
git cherry-pick 170a305
```

合并提交ID `170a305` 到当前分支末梢

### git reset

> “
>
> 将当前的分支重设（reset）到指定的 `<commit>` 或者 `HEAD`

```
git reset --mixed <commit>
```

`--mixed` 是不带参数时的默认参数，它退回到某个版本，保留文件内容，回退提交历史

```
git reset --soft <commit>
```

暂存区和工作区中的内容不作任何改变，仅仅把 `HEAD` 指向 `<commit>`

```
git reset --hard <commit>
```

自从 `<commit>` 以来在工作区中的任何改变都被丢弃，并把 `HEAD` 指向 `<commit>`

### git rebase

> “
>
> 重新定义分支的版本库状态

```
git rebase branch_name
```

合并分支，这跟 `merge` 很像，但还是有本质区别，看下图：



合并过程中可能需要先解决冲突，然后执行 `git rebase --continue`

```
git rebase -i HEAD~~
```

打开文本编辑器，将看到从 `HEAD` 到 `HEAD~~` 的提交如下

```
pick 9a54fd4 添加commit的说明
pick 0d4a808 添加pull的说明
# Rebase 326fc9f..0d4a808 onto d286baa
#
# Commands:
#  p, pick = use commit
#  r, reword = use commit, but edit the commit message
#  e, edit = use commit, but stop for amending
#  s, squash = use commit, but meld into previous commit
#  f, fixup = like "squash", but discard this commit's log message
#  x, exec = run command (the rest of the line) using shell
#
```

将第一行的 `pick` 改成 `Commands` 中所列出来的命令，然后保存并退出，所对应的修改将会生效。如果移动提交记录的顺序，将改变历史记录中的排序。

### git revert

> “
>
> 撤销某次操作，此次操作之前和之后的 `commit` 和 `history` 都会保留，并且把这次撤销作为一次最新的提交

```
git revert HEAD
```

撤销前一次提交操作

```
git revert HEAD --no-edit
```

撤销前一次提交操作，并以默认的 `Revert "xxx"` 为提交原因

```
git revert -n HEAD
```

需要撤销多次操作的时候加 `-n` 参数，这样不会每次撤销操作都提交，而是等所有撤销都完成后一起提交

### git diff

> “
>
> 查看工作区、暂存区、本地版本库之间的文件差异，用一张图来解释



```
git diff --stat
```

通过 `--stat` 参数可以查看变更统计数据

```
 test.md | 1 -
 1 file changed, 1 deletion(-)
```

### git reflog

`reflog` 可以查看所有分支的所有操作记录（包括commit和reset的操作、已经被删除的commit记录，跟 `git log` 的区别在于它不能查看已经删除了的commit记录

## 远程版本库连接

如果在GitHub项目初始化之前，文件已经存在于本地目录中，那可以在本地初始化本地版本库，再将本地版本库跟远程版本库连接起来

### git init

> “
>
> 在本地目录内部会生成.git文件夹

### git remote

```
git remote -v
```

不带参数，列出已经存在的远程分支，加上 `-v` 列出详细信息，在每一个名字后面列出其远程url

```
git remote add origin https://github.com/gafish/gafish.github.com.git
```

添加一个新的远程仓库，指定一个名字，以便引用后面带的URL

### git fetch

> “
>
> 将远程版本库的更新取回到本地版本库

```
git fetch origin daily/0.0.1
```

默认情况下，`git fetch` 取回所有分支的更新。如果只想取回特定分支的更新，可以指定分支名。

## 问题排查

### git blame

> “
>
> 查看文件每行代码块的历史信息

```
git blame -L 1,10 demo.html
```

截取 `demo.html` 文件1-10行历史信息

### git bisect

> “
>
> 二分查找历史记录，排查BUG

```
git bisect start
```

开始二分查找

```
git bisect bad
```

标记当前二分提交ID为有问题的点

```
git bisect good
```

标记当前二分提交ID为没问题的点

```
git bisect reset
```

查到有问题的提交ID后回到原分支

## 更多操作

### git submodule

> “
>
> 通过 Git 子模块可以跟踪外部版本库，它允许在某一版本库中再存储另一版本库，并且能够保持2个版本库完全独立

```
git submodule add https://github.com/gafish/demo.git demo
```

将 `demo` 仓库添加为子模块

```
git submodule update demo
```

更新子模块 `demo`

### git gc

> “
>
> 运行Git的垃圾回收功能，清理冗余的历史快照

### git archive

> “
>
> 将加了tag的某个版本打包提取

```
git archive -v --format=zip v0.1 > v0.1.zip
```

`--format` 表示打包的格式，如 `zip`，`-v` 表示对应的tag名，后面跟的是tag名，如 `v0.1`。