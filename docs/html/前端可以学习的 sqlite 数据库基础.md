# sqlite

## 一、简介

> SQLite（Structured Query Language Lite）是一种嵌入式数据库引擎，它是一款轻量级的、自包含的数据库管理系统。SQLite 的设计目标是提供一个简单、高效、可嵌入到各种应用程序中的关系型数据库解决方案。

| 特性       | 描述                                                         |
| ---------- | ------------------------------------------------------------ |
| 数据库类型 | 嵌入式数据库引擎                                             |
| 大小       | 核心库通常只有几百KB                                         |
| SQL支持    | 是，支持标准SQL查询语言                                      |
| 多用户访问 | 否，单用户数据库引擎                                         |
| 事务支持   | 是，支持原子性操作                                           |
| 跨平台性   | 是，可在多种操作系统上运行，包括Windows、macOS、Linux和Android等 |
| 开源       | 是，在开源许可证下发布                                       |
| 性能       | 高性能，尤其适用于读取频繁的应用场景                         |

## 二、安装

### 2.1）mac/linux

```arduino
arduino复制代码sh
复制代码
// linux
sudo apt-get install sqlite3
sudo yum install sqlite
sudo pacman -S sqlite
// mac
brew install sqlite
```

### 2.2）windows

- [SQLite](https://link.juejin.cn/?target=https%3A%2F%2Fwww.sqlite.org%2Fdownload.html) 寻找 windows 相关的二进制文件
- 带有 dll 后缀的文件
- 带有 tool 文件
- 在 window 中搜索环境变量
- 进入 `系统属性`
- 进入环境变量
- 找到系统变量，并进入
- 在系统变量中找到 Path
- 编辑系统变量中的环境变量
- 添加环境变量到路径
- 安装完成

## 三、命令

### 3.1) **数据操作命令** ：

- `SELECT`：用于从数据库中检索数据。
- `INSERT`：用于将新数据插入到数据库表中。
- `UPDATE`：用于更新数据库表中的现有数据。
- `DELETE`：用于从数据库表中删除数据。

### 3.2) **表操作命令** ：

- `CREATE TABLE`：用于创建新的数据库表。
- `ALTER TABLE`：用于修改数据库表的结构，例如添加、修改或删除列。
- `DROP TABLE`：用于删除数据库表。

### 3.3) **索引操作命令** ：

- `CREATE INDEX`：用于创建索引以提高查询性能。
- `DROP INDEX`：用于删除索引。

### 3.4) **事务控制命令** ：

- `BEGIN TRANSACTION`：用于开始事务。
- `COMMIT`：用于提交事务。
- `ROLLBACK`：用于回滚事务。

### 3.5) **约束操作命令** ：

- `PRIMARY KEY`：用于定义主键约束。
- `UNIQUE`：用于定义唯一性约束。
- `CHECK`：用于定义检查约束。
- `FOREIGN KEY`：用于定义外键约束。

### 3.6) **数据定义命令** ：

- `CREATE DATABASE`：用于创建新的数据库。
- `ALTER DATABASE`：用于修改数据库属性。
- `DROP DATABASE`：用于删除数据库。

### 3.7) **视图操作命令** ：

- `CREATE VIEW`：用于创建虚拟表，即视图。
- `ALTER VIEW`：用于修改视图的定义。
- `DROP VIEW`：用于删除视图。

### 3.8) **用户和权限管理命令** ：

- `CREATE USER`：用于创建新用户。
- `ALTER USER`：用于修改用户属性。
- `DROP USER`：用于删除用户。
- `GRANT`：用于授予用户权限。
- `REVOKE`：用于收回用户权限。

### 3.9) **信息查询命令** ：

- `PRAGMA`：用于查询和设置SQLite的运行时参数和配置选项。
- `SHOW`：用于显示数据库对象的信息。

## 四、语法

| 类别       | 语法         | 示例                                                         |
| ---------- | ------------ | ------------------------------------------------------------ |
| 数据库操作 | 创建数据库   | `CREATE DATABASE database_name;`                             |
|            | 删除数据库   | `DROP DATABASE database_name;`                               |
|            | 连接到数据库 | `.open database_name;`                                       |
| 表操作     | 创建表       | `CREATE TABLE table_name (column1 datatype, column2 datatype, ...);` |
|            | 删除表       | `DROP TABLE table_name;`                                     |
|            | 重命名表     | `ALTER TABLE old_table_name RENAME TO new_table_name;`       |
| 数据操作   | 插入数据     | `INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);` |
|            | 更新数据     | `UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;` |
|            | 删除数据     | `DELETE FROM table_name WHERE condition;`                    |
| 查询数据   | 查询所有数据 | `SELECT * FROM table_name;`                                  |
|            | 条件查询     | `SELECT * FROM table_name WHERE condition;`                  |
|            | 指定列查询   | `SELECT column1, column2 FROM table_name;`                   |
|            | 排序数据     | `SELECT * FROM table_name ORDER BY column_name ASC/DESC;`    |
|            | 连接表       | `SELECT * FROM table1 INNER JOIN table2 ON table1.column_name = table2.column_name;` |
|            | 聚合函数     | `SELECT COUNT(column_name) FROM table_name;`                 |
|            | 分组数据     | `SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name;` |
|            | 子查询       | `SELECT column_name FROM table_name WHERE column_name IN (SELECT column_name FROM another_table);` |
| 索引操作   | 创建索引     | `CREATE INDEX index_name ON table_name (column1, column2, ...);` |
|            | 删除索引     | `DROP INDEX index_name;`                                     |

## 五、数据类型

| 数据类型      | 描述                                                         | 示例                |
| ------------- | ------------------------------------------------------------ | ------------------- |
| INTEGER       | 整数类型，通常用于存储整数数据。                             | `INTEGER`           |
| REAL          | 浮点数类型，用于存储浮点数数据。                             | `REAL`              |
| TEXT          | 文本类型，用于存储字符串数据。                               | `TEXT`              |
| BLOB          | 二进制大对象类型，用于存储二进制数据。                       | `BLOB`              |
| NULL          | 表示缺少值或空值。                                           | `NULL`              |
| DATE          | 日期类型，用于存储日期值。                                   | `DATE`              |
| TIME          | 时间类型，用于存储时间值。                                   | `TIME`              |
| DATETIME      | 日期和时间类型，用于存储日期和时间组合值。                   | `DATETIME`          |
| BOOLEAN       | 布尔类型，通常用0表示假，1表示真。                           | `BOOLEAN` 或 `BOOL` |
| CHAR(n)       | 固定长度的字符类型，最多包含n个字符。                        | `CHAR(10)`          |
| VARCHAR(n)    | 可变长度的字符类型，最多包含n个字符。                        | `VARCHAR(255)`      |
| DECIMAL(p, s) | 十进制类型，用于精确存储小数值，p表示总位数，s表示小数位数。 | `DECIMAL(10, 2)`    |
| NUMERIC(p, s) | 数值类型，类似于DECIMAL，用于精确存储小数值。                | `NUMERIC(8, 4)`     |
| BIT           | 位类型，通常用于存储位字段。                                 | `BIT`               |
| UUID          | 通用唯一标识符类型，用于存储UUID值。                         | `UUID`              |
| NCHAR(n)      | 国际化字符类型，用于存储Unicode字符，固定长度。              | `NCHAR(20)`         |
| NVARCHAR(n)   | 国际化字符类型，用于存储Unicode字符，可变长度。              | `NVARCHAR(100)`     |

## 六、数据库

### 6.1) **创建内存型数据库**

```sql
sql
复制代码ATTACH ':memory:' AS memdb;
```

### 6.2) **创建磁盘型数据库**

```sql
sql
复制代码ATTACH 'mydatabase.db' AS diskdb;
```

## 七、表

### 7.1) 创建表

```sql
sql复制代码CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Age INTEGER
);
```

### 7.2) 删除表

```sql
sql
复制代码DROP TABLE Students;
```

### 7.3) 修改表结构

```sql
sql复制代码ALTER TABLE Students
ADD COLUMN Email TEXT;
```

## 八、常用操作

### 8.1) **INSERT**

> 用于向表中插入新的数据记录。

```sql
sql复制代码INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

### 8.1) **SELECT**

> 用于从表中检索数据记录。

```sql
sql复制代码SELECT column1, column2, ...
FROM table_name;
```

### 8.1) **WHERE**

> 用于指定检索条件，过滤所需的数据记录。

```sql
sql复制代码SELECT *
FROM table_name
WHERE condition;
```

### 8.1) **AND/OR**

> 用于在WHERE子句中组合多个条件。

```sql
sql复制代码SELECT *
FROM table_name
WHERE condition1 AND condition2;
```

### 8.1) **UPDATE**

> 用于更新表中的数据记录。

```sql
sql复制代码UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

### 8.1) **DELETE**

> 用于从表中删除数据记录。

```sql
sql复制代码DELETE FROM table_name
WHERE condition;
```

### 8.1) **LIKE**

> 用于在WHERE子句中进行模糊匹配。

```sql
sql复制代码SELECT *
FROM table_name
WHERE column_name LIKE pattern;
```

### 8.1) **GLOB**

> 用于在WHERE子句中进行基于通配符的匹配。

```sql
sql复制代码SELECT *
FROM table_name
WHERE column_name GLOB pattern;
```

### 8.1) **LIMIT**

> 用于限制检索结果的行数。

```sql
sql复制代码SELECT *
FROM table_name
LIMIT number_of_rows;
```

### 8.1) **GROUP BY**

> 用于将数据分组并应用聚合函数。

```sql
sql复制代码SELECT column1, COUNT(*)
FROM table_name
GROUP BY column1;
```

### 8.1) **HAVING**

> 用于在GROUP BY后过滤分组的结果。

```sql
sql复制代码SELECT column1, COUNT(*)
FROM table_name
GROUP BY column1
HAVING COUNT(*) > 1;
```

### 8.1) **DISTINCT**

> 用于返回不重复的结果集。

```sql
sql复制代码SELECT DISTINCT column1, column2
FROM table_name;
```

## 九、运算

SQLite 中支持各种运算符，包括算术运算符、比较运算符、逻辑运算符和位运算符。以下是这些运算符的一些示例：

### 9.1) **算术运算符**：

| 符号 | 操作 | 描述                   |
| ---- | ---- | ---------------------- |
| +    | 加法 | 将两个数相加           |
| -    | 减法 | 将一个数减去另一个数   |
| *    | 乘法 | 将两个数相乘           |
| /    | 除法 | 将一个数除以另一个数   |
| %    | 取模 | 返回两个数相除后的余数 |

```sql
sql复制代码SELECT 10 + 5; -- 结果为 15
SELECT 20 - 8; -- 结果为 12
SELECT 4 * 6;  -- 结果为 24
SELECT 15 / 3; -- 结果为 5
SELECT 17 % 4; -- 结果为 1
```

### 9.1) **比较运算符**：

| 符号 | 操作     | 描述                             |
| ---- | -------- | -------------------------------- |
| `=`  | 等于     | 检查两个值是否相等               |
| `!=` | 或 `<>`  | 检查两个值是否不相等             |
| `<`  | 小于     | 检查一个值是否小于另一个值       |
| `>`  | 大于     | 检查一个值是否大于另一个值       |
| `<=` | 小于等于 | 检查一个值是否小于或等于另一个值 |
| `>=` | 大于等于 | 检查一个值是否大于或等于另一个值 |

```sql
sql复制代码SELECT 5 = 5;   -- 结果为 1（真）
SELECT 10 <> 7; -- 结果为 1（真）
SELECT 3 < 8;   -- 结果为 1（真）
SELECT 12 > 20; -- 结果为 0（假）
SELECT 15 <= 15; -- 结果为 1（真）
SELECT 25 >= 30; -- 结果为 0（假）
```

### 9.3) **逻辑运算符**：

| 运算符 | 操作   | 描述                                                         |
| ------ | ------ | ------------------------------------------------------------ |
| `AND`  | 逻辑与 | 将多个条件组合成一个逻辑与条件，只有当所有条件都为真时结果为真 |
| `OR`   | 逻辑或 | 将多个条件组合成一个逻辑或条件，只要至少有一个条件为真，结果就为真 |
| `NOT`  | 逻辑非 | 取反一个条件的真假值                                         |

```sql
sql复制代码SELECT (5 > 3) AND (10 < 20); -- 结果为 1（真）
SELECT (5 > 3) OR (10 > 20);  -- 结果为 1（真）
SELECT NOT (5 > 3);           -- 结果为 0（假）
```

### 9.4) **位运算符**：

SQLite 也支持位运算符，如按位与 `&`、按位或 `|`、按位取反 `~` 等，通常用于处理整数值的二进制位。

```sql
sql复制代码SELECT 5 & 3;  -- 结果为 1（二进制 0101 & 0011 = 0001）
SELECT 5 | 3;  -- 结果为 7（二进制 0101 | 0011 = 0111）
SELECT ~5;     -- 结果为 -6（二进制 ~0101 = 11111111111111111111111111111010，负数表示方式）
```

## 十、表达式

### 10.1) **布尔表达式**：

布尔表达式通常用于评估条件的真假。它们返回布尔值（真或假），常用于`WHERE`子句中，用于过滤数据。

```sql
sql
复制代码SELECT * FROM Students WHERE Age > 18; -- 返回年龄大于18的学生记录
```

### 10.2) **数值表达式**：

数值表达式用于执行数学运算，返回数值结果。

```sql
sql复制代码SELECT 10 + 5;       -- 返回 15
SELECT Salary * 1.1; -- 返回薪水增加10%后的值
```

### 10.3) **日期表达式**：

日期表达式用于处理日期和时间数据。SQLite支持各种日期和时间函数，如`DATE()`, `TIME()`, `DATETIME()`, `strftime()`等，用于操作日期和时间值。

```sql
sql复制代码SELECT DATE('2023-10-04');              -- 返回日期 '2023-10-04'
SELECT TIME('15:30:00');                -- 返回时间 '15:30:00'
SELECT DATETIME('2023-10-04 15:30:00'); -- 返回日期时间 '2023-10-04 15:30:00'
SELECT strftime('%Y-%m-%d', 'now');     -- 返回当前日期，例如 '2023-10-04'
```

## 小结

本文输入 sqlite 的入门文章，内容较多，主要在于梳理 sqlite 的基础内容思路，更加适合初学者。本质上还是 sql 需要大量的实践练习，sqlite 小而轻量更接近企业主流的数据库。也非常适合学习 sqlite 数据库，因为它不需要启动额外的服务。

## 其他关联文章

- [前端可以学习的 sqlite 数据库入门](https://juejin.cn/post/7284881709045088315)