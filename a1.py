# -*- encoding=utf8 -*-
__author__ = "pscly"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
# from douyin import *

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





wake()  # 启动手机
start_app("com.ss.android.ugc.aweme.lite")

hua = 0
滑动方向 = 0 
while 1:
    hua += 1
    滑动方向 += 1
    
    if hua == 10:
        touch(Template(r"tpl1607564875731.png", record_pos=(-0.404, -0.67), resolution=(1079, 2340)))

    sleep(5)
    swipe((484, 1711),(531,709))

    







print("-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=")
print("-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=")
print("-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=")

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)

