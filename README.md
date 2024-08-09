# BezierMouseMove
借助贝塞尔函数实现拟人化的鼠标移动轨迹
Using Bessel algorithm to achieve personification of mouse movement trajectory

## 问题点

### 1.鼠标所走的路径

人类移动鼠标很少直线移动，而是方向变化很大。 

一个简单的测试方法是打开一些画图，选择一个宽度为 1px 的画笔，然后以中等速度绘制一些线条。
![image](https://github.com/user-attachments/assets/c780353c-6eda-4f83-bd01-76d3315ab9bb)
市面上常用的鼠标控制API，类似pyautogui等，鼠标的移动都可以轻而易举的判断非人类。一个网页都可以判断鼠标行为是否人类，游戏想判断此类行为也是轻而易举。

### 2.鼠标移动速度

鼠标移动速度应该是 慢-快-慢 的一个过程,即加速度先为正,快到目标点时陡然变为很大的负加速度.

## 方案

结合以上两点,采用贝塞斯二阶曲线的轨迹来模拟人操作鼠标的轨迹

## 效果
![mouse_move](https://github.com/user-attachments/assets/3b560a88-4458-40f6-91b2-077b814b08e0)
![image](https://github.com/user-attachments/assets/77940c07-7c05-418a-a2ae-0cb6b5b2a7ac)

1. 随机性强，轨迹随机、移动速度随机
2. 可自主调节参数，用于进行轨迹移动规划。
3. 平滑运行轨迹移动，可中断操作后继续移动。
4. 可迁移性高，可迁移到多种鼠标移动方式场景

## 感谢
如果该脚本对您有帮助,可以请作者喝瓶矿泉水
[图片]
[图片]
