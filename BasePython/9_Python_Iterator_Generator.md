## 2022-11-12 迭代器和生成器

### 一、什么是迭代协议?  

```python
可迭代类型 和 迭代器 

迭代器是什么? 
迭代器是访问集合内元素的一种方式,一般用来遍历数据;
迭代器不可下标返回, 不支持切片, 迭代器不能返回的, 提供惰性方式获取数据.

for collections.abc import Iterable, Iterator 

Iterable: 可迭代类型 
Iterator: 迭代器 

Iterator 继承 Iterable   
 - __next__ 
 - __iter__

i = [1, 2]
iterator_eg = iter(i)

class School:
    def __init__(self, students):
        self.students = students 
        
    def __iter__(self):
        return SchoolIterator(self.students)

# 迭代器 
class SchoolIterator(Iterator): 
    def __init__(self, students):
        self.students = students 
        self.index = 0
    
    def __next__(self):
        # 返回迭代值
        try:
        	student = self.students[self.index]
        except IndexError:
            raise StopIteration 
        self.index += 1 
        return student

if __name__ == '__main__':
    school = School(['a', 'b', 'c'])
    itor = iter(school)
    next(itor)
    for item in school:
        print(item)
```

### 二、生成器 

```python
# 生成器函数-yield关键字
def genator_func():
	yield 1  # 返回生成器对象
    yield 2 
    yield 3 

def func():
	return 1 

if __name__ == '__main__':
    # 生成器对象, python 编译字节码的时产生
    
```

### 三、生成器原理 

```python
1.函数工作原理 
def func():
    func1() 

def func1():
    pass 
PyEval_EvalFramEx(c函数)执行函数,首先会创建一个栈帧(stack frame) 
"""
一切皆对象, 创建栈帧对象, 运行字节码对象
当func调用子函数func1, 再创建栈帧, 所有的栈帧都分配在堆内存上, 决定栈帧可以独立于调用者存在.
"""
import dis 
print(dis.dis(func))
```

### 四、生成器原理

```python
class company:
    
    @abstractmethod 
    def __getitem__(self, index):
         raise IndexError 
    
	def __iter__(self):
        i = 0 
        try:
            while True:
                v = self[i]
                yield v 
                i += 1 
            except IndexError: 
                return 
    

from collections import Userlist 


```

### 五、生成器应用 

```python
# 1T 数据, 只有一行 

def read_lines(f, new_line):
    buf = ""
    while True:
        while new_line in buf:
            pos = buf.index(new_line)
            yield buf[:pos]
            buf = buf[pos + len(new_line)]
         chunk = f.read(1024 * 20)
         if not chunk:
          	yield buf 
            break 
         buf += chunk 
        
with open('temp.txt') as f:
    for line in read_lines(f, '$'):
        print(line)
```

