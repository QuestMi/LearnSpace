##  2022-11-18 Python 依赖管理 Poetry 小技巧

Poetry官网: https://python-poetry.org/docs/ 

### 1.修改poetry镜像源

```python
"""
豆瓣 https://pypi.doubanio.com/simple/
网易 https://mirrors.163.com/pypi/simple/
阿里云 https://mirrors.aliyun.com/pypi/simple/
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
"""

[[tool.poetry.source]]
name = "aliyun"
url = "http://mirrors.aliyun.com/pypi/simple"
default = true
```

### 2.通过requirements.txt安装依赖 

```python
poetry add $( cat requirements.txt )

# or 

cat requirements.txt | xargs poetry add
```

###  3.查看安装过程 

```python
poetry add 包名 -vvv
```

