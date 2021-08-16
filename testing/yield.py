# yield + 函数 == 生成器
import time
# from datetime import time


def provider():
    for i in range(5):
        print('before')
        yield i # 生成器 ：return i
        print('after')

p = provider()
print(next(p))
print(next(p))
print(next(p))

print(time.localtime())
print(time.time())
print(time.strftime('%Y:%m:%d',time.localtime()))
