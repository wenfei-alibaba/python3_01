has_ticket = False
knife_length = 20
if has_ticket:
    print("车票检查通过 准备开始安检")
    if knife_length > 20:
        print("您携带的到太长了 有 %d 公分长！" % knife_length)
        print("不允许上车")
    else:
        print("检查通过 请允许上车")
else:
    print("大哥 请先买票")
