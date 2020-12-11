## 运行方式

> airtest run untitled.air --device Android:///手机设备号 --log log/ 
>
> python -m airtest run untitled.air --device Android:///手机设备号 --log log/



```python
# 要添加一下文件目录，不然不能import 同目录下的文件
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

```



## 各个包名

抖音 ：com.ss.android.ugc.aweme.lite

快手：com.kuaishou.nebula

打开软件     start_app('包名')

关闭软件     



- [ ] 滑动速度改为随机

- [ ] 间隔改为随机
- [ ] 自动点赞