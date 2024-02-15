# C++ 的 vector 容器

## 前言

- vector 的数据结构是单端数组
- vector 类似于数组，但与数组不同的是，可以动态扩展
- vector 的数据结构是尾部插入，尾部弹出



## 引入头文件

```cpp
#include <vector>
```

## 构造

### 空构造

```cpp
vector<T> v;
```

### 拷贝构造

```cpp
vector<T> v(v);
```

### 拷贝部分元素

- 将 `[<iterator_start>, <iterator_end>)` 区间内的元素拷贝

> `<iterator_start>`：开始位置迭代器
> `<iterator_end>`：结束位置迭代器

```cpp
vector<T> v(<iterator_start>, <iterator_end>);
```

### 将多个相同元素赋值

> `<num>`：元素的个数
> `<element>`：需要存放的元素

```cpp
vector<T> v(<num>, <element>);
```

## 迭代器

### 定义迭代器

#### 第一个元素的前一个位置

```cpp
verctor<T>::iterator it = v.rend();
```

#### 第一个元素的位置

```cpp
verctor<T>::iterator it = v.begin();
```

#### 最后一个元素的位置

```cpp
verctor<T>::iterator it = v.rbegin();
```

#### 最后一个元素的后一个位置

```cpp
verctor<T>::iterator it = v.end();
```

### 迭代器递增

> `<step>`：访问的步数

```cpp
it += <step>;
it -= <step>;

it++;
it--;
```

### 通过迭代器遍历

```cpp
for (vector<T>::iterator it = v.begin(); it != v.end(); it++)
{
    cout << *it << endl;
}
```

#### 使迭代器只读

- 当一个函数传递的 vector 是常量时，需要将 iterator 改为 const_iterator

```cpp
void print(const vector<T> & v)
{
    for (vector<T>::const_iterator it = v.begin(); it != v.end(); it++)
    {
        cout << *it << endl;
    }
}
```

## 赋值

### 利用运算符重载赋值

```cpp
v = v;
```

### 利用 assign 函数赋值

#### 利用区间的方式赋值

> `<iterator_start>`：开始位置迭代器
> `<iterator_end>`：结束位置迭代器

```cpp
v.assign(<iterator_start>, <iterator_end>);
```

#### 将多个相同元素赋值

> `<num>`：元素的个数
> `<element>`：需要存放的元素

```cpp
v.assign(<num>, <element>);
```

## 容量和大小的操作

### 判断容器是否为空

```cpp
v.empty();
```

### 获取容器的容量

```cpp
v.capacity();
```

### 获取元素的个数

```cpp
v.size();
```

### 重新指定容量

- 如果扩容，会以默认值填充新的位置
- 如果缩容，末尾的数据会被删除

> `<num>`：新的容量

```cpp
v.resize(<num>);
```

#### 以指定元素填充新的位置

> `<element>`：填充的元素

```cpp
v.resize(<num>, <element>);
```

## 增

### 向尾部添加元素

> `<element>`：元素

```cpp
v.push_back(<element>);
```

### 在迭代器指向的位置添加元素

> `<iterator>`：迭代器
> `<element>`：元素

```cpp
v.insert(<iterator>, <element>);
```

#### 添加多个相同的元素

> `<iterator>`：迭代器
> `<num>`：插入元素的个数
> `<element>`：元素

```cpp
v.insert(<iterator>, <num>, <element>);
```

## 删

### 删除尾部的元素

```cpp
v.pop_back();
```

### 删除迭代器指向的元素

- 返回下一个元素的位置

> `<iterator>`：迭代器

```cpp
v.erase(<iterator>);
```

#### 删除一组元素

- 返回下一个元素的位置

> `<iterator_start>`：开始位置迭代器
> `<iterator_end>`：结束位置迭代器

```cpp
v.erase(<iterator_start>, <iterator_end>);
```

### 删除容器中所有的元素

```cpp
v.clear();
```

## 改

### 通过迭代器

> `<value>`：修改后的值

```cpp
*it = <value>;
```

### 通过运算符修改指定下标的元素

> `<index>`：需要读写的元素下标
> `<value>`：修改后的值

```cpp
v[<index>] = <value>;
```

### 通过 at 函数修改指定下标的元素

> `<index>`：需要读写的元素下标
> `<value>`：修改后的值

```cpp
v.at(<index>) = <value>;
```

## 查

### 通过迭代器

```cpp
*it;
```

### 获取容器中第一个元素

```cpp
v.front();
```

### 获取容器中最后一个元素

```cpp
v.back();
```

### 查询指定位置的元素

#### 通过运算符重载

> `<index>`：需要读写的元素下标

```cpp
v[<index>];
```

#### 通过 at 函数

```cpp
v.at(<index>);
```

## 排序

### 利用内置算法

- 利用内置算法，实现升序排序

> `<iterator_start>`：开始位置迭代器
> `<iterator_end>`：结束位置迭代器

```cpp
#include <algorithm>

sort(<iterator_start>, <iterator_end>);
```

### 利用自定义算法

- 利用[二元谓词](https://loli.fj.cn/zh-CN/2022/09/10/C-的函数对象/#二元谓词)，实现降序排序

```cpp
class Cla
{
public:
    bool operator()(T t1, T t2)
    {
        return t1 > t2;
    }
};

sort(v.begin(), v.end(), Cla());
```

## 交换

- 容器内数据的互换

```cpp
v.swap(v);
```

### 利用 swap 函数实现收缩容器的空间

```cpp
vector<T>(v).swap(v);
```

## 预留空间

- 当自动扩容的操作过多时，如果提前知道容器应该分配的容量，可以通过预留空间节省扩容的次数，从而节省资源

> `<num>`：开辟的空间大小

```cpp
v.reserve(<num>);
```

## 查找

### 查找指定元素是否存在

- 利用[一元谓词](https://loli.fj.cn/zh-CN/2022/09/10/C-的函数对象/#一元谓词)查找指定条件的元素是否存在。如果存在，就返回找到的元素的迭代器；如果不存在，就返回尾部迭代器

```cpp
class Cla
{
public:
    bool operator()(T t)
    {
        return false;
    }
};

vector<T t>::iterator it = find_if(v.begin(), v.end(), Cla());
```