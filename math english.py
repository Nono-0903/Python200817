math = float(input("請輸入數學成績:"))
english = float(input("請輸入英文成績:"))

if math >= 0 and english >= 0 and math <= 100 and english <= 100:
    if math >= 90 and english >= 90:
        print("有獎品!!")
    elif math <= 60 and english <= 60:
        print("受罰")
    elif math <= 60 or english <= 60:
        print("加油!!")

    
else:
    print("輸入錯誤!!!!!")