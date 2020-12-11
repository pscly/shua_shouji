# coding:utf-8

# import sys,os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import random

def get_ranint(ji=0):
    if ji:  # 手在上面时
        return (random.randint(350, 700), random.randint(600, 700))

    return (random.randint(350, 700), random.randint(1400, 1800))

    # swipe((484, 1711),    # 1800 是下面
    # (531, 709))           # 330 是上面
class ShouJi1:

    def __init__(self):
        # wake()  # 启动手机(手机依然黑屏， 后台价值)
        self.run_douyin = 0
        self.run_kuaishou = 0


    def qidongdouyin(self):
        '''  启动抖音  '''
        # wake()  # 启动手机(手机依然黑屏， 后台价值)
        start_app("com.ss.android.ugc.aweme.lite")
        self.run_douyin = 1

    def qidongkuaishou(self):
        '''  启动快手  '''
        # wake()
        start_app("com.kuaishou.nebula")
        self.run_kuaishou = 1

    def shua(self, sleep_num=5):
        if not self.run_douyin:
            self.qidongdouyin()

        hua = 0

        while 1:
            hua += 1

            if hua == 6:
                double_click(random.randint(350,700),random.randint(800, 1200))  # 点赞
                touch(Template(r"tpl1607564875731.png", record_pos=(-0.404, -0.67), resolution=(1079, 2340)))


            sleep(sleep_num)
            #             swipe((484, 1711), (531, 709))
            swipe(get_ranint(), get_ranint(1),duration=0.2,steps=2)

    def kai(self):
        wake()

if __name__ == '__main__':
    print(get_ranint())
    print(get_ranint(1))



