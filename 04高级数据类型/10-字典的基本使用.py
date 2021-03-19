xiaoming_dict={"name":"小明"}
# 1. 取值
print(xiaoming_dict["name"])
# 在取值的时候，如果指定的key不存在，程序会报错！
# print(xiaoming_dict["name123"])

# 2. 增加/修改
# 如果key不存在，会新增键值对
xiaoming_dict["age"]=22
print(xiaoming_dict)
xiaoming_dict["name"]="徐文飞"
print(xiaoming_dict)
# 删除
xiaoming_dict.pop("name")
print(xiaoming_dict)
