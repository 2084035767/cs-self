# C++ 的常用算法

## 前言

C++ 的 STL 常用算法学习笔记



## 引入头文件

```cpp
#include <algorithm>
#include <functional>
#include <numeric>
```

## 遍历算法

### for_each 遍历容器

#### 通过普通函数

```cpp
vector<T> v;

void method(T t)
{
    cout << t << " ";
}

for_each(v.begin(), v.end(), method);
```

#### 通过匿名函数对象

```cpp
vector<T> v;

class Cla
{
public:
    void operator()(T t)
    {
        cout << t << " ";
    }
};

for_each(v.begin(), v.end(), Cla());
```

### transform 搬运迭代器内容

```cpp
vector<T> v_old;
vector<T> v_new;
v_new.resize(v_old.size());

class Cla
{
public:
    T operator()(T t)
    {
        return t;
    }
};

transform(v_old.begin(), v_old.end(), v_new.begin(), Cla());
```

## 查找算法

### find 在容器内查找元素

- 在容器内查找指定元素。如果存在，返回指定元素迭代器；如果不存在，返回迭代器 end

#### 查找内置数据类型

```cpp
vector<T> v;

vector<T>::iterator it = find(v.begin(), v.end(), <element>);
```

#### 查找自定义数据类型

- 查找自定义数据类型的元素需要在类中进行 `==` 的运算符重载

```cpp
vector<T> v;

class Persion
{
public:
    int id;
    
    bool operator==(const Persion& p)
    {
        return this->id == p.id;
    }
};

vector<Persion>::iterator it = find(v.begin(), v.end(), <element>);
```

### find_if 根据条件在容器内查找元素

- 在容器内根据条件查找指定元素。如果存在，返回指定元素迭代器；如果不存在，返回迭代器 end

#### 查找内置数据类型

```cpp
vector<T> v;

class Cla
{
public:
    bool operator()(T t)
    {
        return false;
    }
};

vector<T>::iterator it = find_if(v.begin(), v.end(), Cla());
```

#### 查找自定义数据类型

```cpp
vector<T> v;

class Persion
{
public:
    int id;
};

class Cla
{
public:
    bool operator()(Persion& p)
    {
        return false;
    }
};

vector<Persion>::iterator it = find(v.begin(), v.end(), Cla());
```

### adjacent_find 在容器内查找相邻重复元素

- 在容器内查找相邻重复元素。如果存在，返回第一次出现重复元素的迭代器；如果不存在，返回迭代器 end

```cpp
vector<T> v;

vector<T>::iterator it = adjacent_find(v.begin(), v.end());
```

### binary_search 二分查找法在容器内查找元素

- 在容器内查找指定元素。如果存在，返回 true；如果不存在，返回 false
- 在无序序列不可以用这种方法

```cpp
vector<T> v;

bool result = binary_find(v.begin(), v.end(), <element>);
```

### count 在容器内统计元素个数

#### 统计内置数据类型

```cpp
vector<T> v;

int result = count(v.begin(), v.end(), <element>);
```

#### 统计自定义数据类型

```cpp
vector<T> v;

class Persion
{
public:
    id;
    
    bool operator==(const Persion& p)
    {
        return this->id == p.id;
    }
};

int result = count(v.begin(), v.end(), <element>);
```

### count_if 在容器内按条件统计元素个数

#### 统计内置数据类型

```cpp
vector<T> v;

class Cla
{
public:
    bool operator()(T t)
    {
        return false;
    }
};

int result = count_if(v.begin(), v.end(), Cla());
```

#### 统计自定义数据类型

```cpp
vector<T> v;

class Persion
{
public:
    id;
};

class Cla
{
public:
    bool operator(const Persion& p)
    {
        return false;
    }
};

int result = count_if(v.begin(), v.end(), Cla());
```

## 排序算法

### sort 对容器内元素排序

#### 默认排序规则

- 默认排序规则为升序

```cpp
vector<T> v;

sort(v.begin(), v.end());
```

#### 内置的排序规则

- 改为降序

```cpp
vector<T> v;

sort(v.begin(), v.end(), greater<T>());
```

#### 自定义排序规则

- 手动改为降序

```cpp
vector<T> v;

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

### random_shuffle 对容器指定范围的元素洗牌

- 打乱容器内指定范围元素的位置

```cpp
# include <ctime>

// 为了随机的更真实，定义随机种子
srand((unsigned int) time(NULL));

vector<T> v;

random_shuffle(v.begin(), v.end());
```

### merge 合并元两个容器内的元素

- 合并两个容器内的元素，并存放到新的容器内
- 合并前的两个序列必须是有序的
- 合并后的序列也是有序的

```cpp
// 准备两组有序的序列
vector<T> v_old_1;
sort(v_old_1.begin(), v_old_1.end());
vector<T> v_old_2;
sort(v_old_2.begin(), v_old_2.end());
// 准备新空序列，并开辟空间
vector<T> v_new;
v_new.resize(v_old_1.size + v_old_2.size);

merge(v_old_1.begin(), v_old_1.end(), v_old_2.begin(), v_old_2.end(), v_new.begin());
```

### reverse 反转容器内指定范围的元素

```cpp
vector<T> v;

reverse(v.begin(), v.end());
```

## 拷贝和替换算法

### copy 拷贝容器内指定范围的元素到新容器

```cpp
vector<T> v_old;
vector<T> v_new;
v_new.resize(v_old.size());

copy(v_old.begin(), v_old.end(), v_new.begin());
```

### replace 将指定范围内的旧元素替换成新元素

> `<value_old>`：替换前的值
> `<value_new>`：替换后的值

```cpp
vector<T> v;

copy(v.begin(), v.end(), <value_old>, <value_new>);
```

### replace_if 根据条件将指定范围内的旧元素替换成新元素

> `<value_new>`：替换后的值

```cpp
vector<T> v;

class Cla
{
public:
    bool operator()(T t)
    {
        return false;
    }
};

copy(v.begin(), v.end(), Cla(), <value_new>);
```

### swap 交换两个容器内的元素

- 交换两个同种容器内的元素

```cpp
vector<T> v1;
vector<T> v2;

swap(v1, v2);
```

## 算数生成算法

### accumulate 计算容器指定范围内元素总和

> `0 `：定义求和的起始值

```cpp
vector<int> v;

int value = accumulate(v.begin(), v.end(), 0)
```

### fill 将数据填充到容器指定范围

> `<value>`：填充的值

```cpp
vector<T> v;

fill(v.begin(), v.end(), <value>);
```

## 集合算法

### set_intersection 求两个容器的交集

```cpp
vector<T> v_old_1;
vector<T> v_old_2;
vector<T> v_new;
// 将新容器的容量设置为两个旧容器最小的容量
v_new.resize(min(v_old_1.size(), v_old_2.size()));

set_intersection(v_old_1.begin(), v_old_1.end(), v_old_2.begin(), v_old_2.end(), v_new.begin());
```

### set_union 求两个容器的并集

```cpp
vector<T> v_old_1;
vector<T> v_old_2;
vector<T> v_new;
v_new.resize(v_old_1.size() + v_old_2.size());

set_union(v_old_1.begin(), v_old_1.end(), v_old_2.begin(), v_old_2.end(), v_new.begin());
```

### set_difference 求两个容器的差集

- 两个容器的差集 = 容器前者 - 容器后者

```cpp
vector<T> v_old_1;
vector<T> v_old_2;
vector<T> v_new;
v_new.resize(max(v_old_1.size(), v_old_2.size()));

set_difference(v_old_1.begin(), v_old_1.end(), v_old_2.begin(), v_old_2.end(), v_new.begin());
```cpp