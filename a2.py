# -*- encoding=utf8 -*-
__author__ = "pscly"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
# from my_func import *

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/12101d3d?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MINITOUCH",
    ], project_root="C:/Users/pscly/Desktop/a11")


# script content
print("start...")










def get_ranint(ji=0):
    import random
    if ji:  # 手在上面时
        return (random.randint(350,700),random.randint(600, 700))

    return (random.randint(350,700), random.randint(1400, 1800))

    # swipe((484, 1711),    # 1800 是下面
    # (531, 709))           # 330 是上面

class Dy:

    def __init__(self):
        # wake()  # 启动手机(手机依然黑屏， 后台价值)
        self.run_douyin = 0
        pass

    def qidongdouyin(self):
        wake()  # 启动手机(手机依然黑屏， 后台价值)
        start_app("com.ss.android.ugc.aweme.lite")
        self.run_douyin = 1

    def shua(self, sleep_num=5):
        if not self.run_douyin:
            self.qidongdouyin()

        hua = 0

        while 1:
            hua += 1


            if hua > 6:
                print("00000")
                
            sleep(sleep_num)
#             swipe((484, 1711), (531, 709))
            swipe(get_ranint(), get_ranint(1),duration=0.2,steps=2)

    def kai(self):
        unlock()










dy = Dy()
dy.shua(1)


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)