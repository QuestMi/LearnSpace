# 2022-10-03 Effective Python 

### 1、PEP8规范

1. 模块级别常量,所有字母都大写,单词之间下划线相连(ALL_CAPS);
2. 类实例方法,第一个参数命名为: self, 表示对象本身;
3. 类方法, 第一个参数命名为: cls, 表示这个类本身;

```python
# 表达式规范 
# 1.行内否定
if a is not b (no: if not a is b)

# 2.判断容器、序列是否为空
if not somelist (no: if len(somelist) == 0)
if somelist

```

4. 引入相关依赖 

```python
1. 首先引入标准库里的模块;
2. 然后引入第三方模块;
3. 最后引入自己的模块;
同一部分的import语句按字母顺序排列 
工具: pylint
```

### 2、bytes、Str

1. bytes实例包含的是原始数据,即8位无符号值;
2. str实例包含的是Unicode码点;

```python
unicode -> 二进制数据: str.encode方法
二进制   -> unicode:   bytes.decode方法
```

