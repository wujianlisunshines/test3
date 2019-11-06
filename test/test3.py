'''
name='as  asd'
print("妈妈给丽丽加油"+name.title())
print(name.lower())
print(name.upper())
print("a\nname\nname\tname")
'''
# 删除空格
name1=" 妈妈我爱你 "

#整数
print(name1.rstrip())
print(2+3)
print(2-3)
print(3**2)
print(3**3)
print(10**6)
print(2+3*4)
print((2+3)*4)
#浮点数
print(2*0.1)
print(0.1+0.6)

#函数str
age=26
daxingxing="大猩猩今年"+str(age)
print(daxingxing)

#除数
print(3/2)

#列表
fruit=["苹果","香蕉","芒果","a bc"]
print(fruit)
print(fruit[0])
print(fruit[3].title())
#通过将索引指定为-1，不知道列表的长度可以访问最后一个元素
print(fruit[-1])
print("今天吃"+fruit[0])

daxingxing="大猩猩"
lili="丽丽"

#修改列表元素
fruit[0]="菠萝蜜"
print(fruit)

#添加元素1
fruit.append("哈密瓜")
print(fruit)

#添加元素2  可以先创建空列表，再赋值
fruit=[]
fruit.append("窗外")
fruit.append("蝴蝶")
print(fruit)

#在列表中插入元素
fruit.insert(0,"水果")
print(fruit)

#删除元素
del fruit[0]
print(fruit)

#删除元素pop（）可以删除列表末尾的元素，并且可以访问/使用被删除元素的值
some=["星星","月亮"]
print(some)
some1=some.pop()
print(some)
print(some1)

some3=some.pop(0)
print(some3+'.')

lili=["li","丽丽"]
lili.remove("li")
print(lili)


num=6
if num<7:
    print('香蕉')
else:
    print('葡萄')



# a=["b","c"]
# a[0]="新值";  append,insert();  del,pop(),remove();  访问删除的元素 b=a.pop(0)
#
# 勤学勤练习=
# 能达到效果的方法就是好方法