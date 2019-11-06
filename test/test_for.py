
qinrens=['爸爸','妈妈','弟弟','妹妹','parent']
for qinren in qinrens:
  print(qinren.title()+'一起玩\n')  #title()，每个单词首字母大写

#输出结果为1-5，因为函数range()让python从指定的第一个值开始数，到达第二个值后停止，需加1/减1
for value in range(1,6):
  print(value)

#使用range()创建数字列表
numbers=list(range(1,6))
print(numbers)

#指定步长,打印1-10内的偶数
even_numbers=list(range(2,11,2))
print(even_numbers)

#两个**代表乘方运算
squares=[]
for value in range(1,11):
  squares.append(value**2)
print(squares)

digits=[1,2,3,4,5,6,7,8,9]
print(max(digits))
print(min(digits))
print(sum(digits))

#列表解析
squares=[value**2 for value in range(1,11)]
print(squares)

#复制列表
my_food=['土豆','西红柿','洋葱']
#friend_food=my_food
friend_food=my_food[:]
my_food[0]=1
print(my_food)
print(friend_food)

my_food=['土豆','西红柿','洋葱']
friend_food=my_food
#friend_food=my_food[:]
my_food[0]=1
print(my_food)
print(friend_food)












# fruits=['苹果','香蕉','哈密瓜']
# for fruit in fruits:
#   print(fruit.title()+"，真好吃")
#   print("丽丽下次还要吃"+fruit.title()+".\n")
# print("水果真好吃") # 没有缩进的代码只执行一次
print('提交测试乱码')