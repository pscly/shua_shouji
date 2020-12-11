# -*- encoding=utf8 -*-
__author__ = "pscly"

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from my_func import *

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/12101d3d?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MINITOUCH",
    ], project_root="C:/Users/pscly/Desktop/my/Airtest/py1")


# script content    
print("冲冲冲===================")
sj1 = ShouJi1()
wake()
sj1.qidongkuaishou()
sj1.shua()






# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
