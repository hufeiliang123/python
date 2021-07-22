import re


def main():
    tel = input("请输入手机号:")
    # ret = re.match(r"1[35678]\d{9}", tel)
    # 由于手机号位数大于11位也能匹配成功，所以修改如下：
    ret = re.match(r"^1[35678]\d{9}$", tel)

    if ret:
        print("匹配成功")
    else:
        print("匹配失败")


if __name__ == "__main__":
    main()