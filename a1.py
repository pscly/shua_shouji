# -*- encoding=utf8 -*-
C__author__ = "pscly"


from airtest.core.api import *
from airtest.cli.parser import cli_setup


if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/decc8da3?cap_method=MINICAP_STREAM&&ori_method=MINICAPORI&&touch_method=MINITOUCH",
    ])


# script content
print("start...")
print("冲冲冲!")
print("-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=")
print("-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=")
print("-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=")


import random
def get_ranint(ji=0):
    if ji:  # 手在上面时
        return (random.randint(350,700),random.randint(600, 700))

    return (random.randint(350,700), random.randint(1400, 1800))




class ShouJi1:

    def __init__(self):
        # wake()  # 启动手机(手机依然黑屏， 后台价值)
        self.run_douyin = 0
        self.run_kuaishou = 0


    def qidongdouyin(self):
        '''  启动抖音  '''
        wake()  # 启动手机(手机依然黑屏， 后台价值)
        start_app("com.ss.android.ugc.aweme.lite")
        self.run_douyin = 1

    def qidongkuaishou(self):
        '''  启动快手  '''
        wake()
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
        unlock()


dy = Dy()
dy.shua(1)

    







print("-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=")
print("-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=")
print("-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=")

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)







