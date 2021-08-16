import time
import threading

def func1():
    for i in range(5):
        time.sleep(1)
        print('-----正在做事情1-----')

def func2():
    for i in range(6):
        time.sleep(1)
        print('-----正在做事情2-----')

def main():
    # 创建一个线程去执行 事情1
    t1 = threading.Thread(target=func1)
    # 创建一个线程去执行 事情2
    t2 = threading.Thread(target=func2)
    s_time = time.time()
    # 开始执行线程1
    t1.start()
    # 开始执行线程2
    t2.start()
    # 让主线程等待子线程执行完了之后再继续往下执行
    t1.join()
    # t2.join()

    e_time = time.time()
    print('耗时：', e_time - s_time)

if __name__=='__main__':
    main()