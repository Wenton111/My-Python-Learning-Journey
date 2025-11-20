import random
def luckydog_draw(names):
    luckydogs=random.sample(names,2)
    return{"请回答第一个问题":luckydogs[0],"请回答第二个问题":luckydogs[1]}
names=[]

print("将抽取两个迟到的同学上台回答问题")
print("你迟到了，请输入你的姓名，最后一名同学输入‘开始’进行抽签")
while True:
    name=input("请输入你的姓名:")
    if name=="开始":
        break
    if name.strip()=="":
       print("不可以空着！重新输入")
       continue
    names.append(name)
if len(names)<2:
    print("别看了，只有你要上台回答问题")
else:
     result=luckydog_draw(names)
     print("\n抽签结果来喽")
     for question,luckydog in result.items():
         print(f"{question}:{luckydog}" )
     print("下次不许再迟到了！！！！")
