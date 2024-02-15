# CSS 垂直居中



## padding

适用于 parent 的高度不确定的情况

```
.parent {
  padding: 20px 0;
}

.child {}

复制代码
```

## flex

```
.parent {
  display: flex;
  justify-content: center;
  align-items: center;
}

.child {}

复制代码
```

## absolute margin auto

```
.parent {
  position: relative;
}

.child {
  position: absolute;
  margin: auto;
  width: 300px;
  height: 200px;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}

复制代码
```

注意：

1. child 的宽高都必须是确定值
2. 可用 `inset: 0` 代替 `top: 0; bottom: 0; left: 0; right: 0;`

## absolute translate

```
.parent {
  position: relative;
}

.child {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
}

复制代码
```

## grid

```
.parent {
  display: grid;
}

.child {
  place-self: center;
}

复制代码
```

参考资料

- [七种方式实现垂直居中](https://www.yuque.com/u202856/gbe1wh/dq4yge?)