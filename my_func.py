import random

def get_ranint(ji=0):
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
        滑动方向 = 0

        while 1:
            hua += 1
            滑动方向 += 1

            if hua == 6:
                touch(Template(r"tpl1607564875731.png", record_pos=(-0.404, -0.67), resolution=(1079, 2340)))

            sleep(sleep_num)
            # swipe((484, 1711), (531, 709))
            swipe(get_ranint(), get_ranint(1))

if __name__ == '__main__':
    print(get_ranint())
    print(get_ranint(1))


