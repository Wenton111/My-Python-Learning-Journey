import random

def number_bomb():
    bomb = random.randint(1, 100)  # 生成炸弹数字 
    start, end = 1, 100  # 初始范围1~100
    guess_count = 0  # 猜测次数
    
    print("数字炸弹游戏开始！")
    print("炸弹在1到100之间的某个数字")
    
    while True:
        try:
            guess = int(input(f"\n请输入1-100 之间的整数："))
            guess_count += 1
            
            if guess < start or guess > end:
                print(f"请输入 {start} 到 {end} 之间的数字！")
                continue
                
            if guess == bomb:
                print(f"恭喜你猜中了炸弹数字 {bomb}")
                print(f"你总共猜了 {guess_count} 次")
                break
            elif guess > bomb:
                print(f"太大了！炸弹数字比 {guess} 小")
                end = guess - 1  # 缩小上限范围
            else:
                print(f"太小了！炸弹数字比 {guess} 大")
                start = guess + 1  # 缩小下限范围
                
            print(f"当前范围：{start} - {end}")
            
        except ValueError:
            print("输入无效，请输入整数！")

if __name__ == "__main__":
    number_bomb()
