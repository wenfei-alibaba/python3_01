# 练习2: 定义两个整数变量 python_score、c_score，编写代码判断成绩
python_score = int(input("请输入python考试成绩:"))
c_score = int(input("请输入C考试成绩:"))
if python_score > 60 or c_score > 60:
    print("考试通过")
else:
    print("考试失败,继续努力")
