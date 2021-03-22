# num = 10
gl_num = 1000
gl_title = "徐文飞"
gl_name = "中天控股"


def demo():
    # 如果局部变量的名字和全局变量的名字相同
    # pycharm会在局部变量下方显示一个灰色的虚线
    num = 99
    print("%d" % num)
    print("%s" % gl_title)
    print("%s" % gl_name)


# # 再定义一个全局变量
# title = "黑马程序员"
demo()
