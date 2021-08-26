# a=[1,2,3,4,5]
# print(a[-1::-1])
# import os
#
# passwd = {'admin':123456,'user1':123321}
# username = input('请输入用户名：')
# a=1
# while a<4:
#     if username == '' or username not in passwd.keys():
#         username = input('用户名不正确!\n请输入正确的用户名:')
#     else:
#         password = int(input('请输入密码：'))
#         if passwd[username] == password:
#             print('登录成功')
#             break
#         else:
#             a += 1
#             if a != 4:
#                 print('密码错误!,您还有{}次机会!'.format(4-a))
#             else:
#                 print('密码错误!')

# def test_args(*args):
#     print(*args)


# test_args('1X','2X','3a')
import os

# def test_browser():
#     browser = os.getenv("browser")
#     if browser == '123':
#         print(123)
#         print(os.getenv("path"))
def test_1():
    browser = os.getenv("browser")
    if browser == 'edag':
        print('我是edag的驱动')
            # self.driver = webdriver.Edge()


