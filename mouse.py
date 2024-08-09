import math
import random
import time
import pyautogui


def bezierCurve(control_points, t):
    n = len(control_points) - 1
    result = (0, 0)
    for i in range(n + 1):
        binomial_coeff = 1
        for j in range(i):
            binomial_coeff *= (n - j) / (j + 1)
        factor = binomial_coeff * pow(t, i) * pow(1 - t, n - i)
        result = (
            result[0] + int(factor * control_points[i][0]),
            result[1] + int(factor * control_points[i][1])
        )
    return result


def mouseMoveTo(targetPos):
    pyautogui.moveTo(targetPos[0], targetPos[1])


def randomOne():
    return (random.randint(0, 20)) / 10


def randomTwo():
    return random.randint(-10, 10) / 10


def simulateMouseMove(startPos, targetPos):
    onMoving = False
    controlPoints = []
    currentStep = 0
    lastTime = int(time.time_ns() / 1000000)
    defaultInterval = 7
    length = math.sqrt((targetPos[0] - startPos[0]) ** 2 + (targetPos[1] - startPos[1]) ** 2)
    print("=====", length)
    # 控制点基本量 和移动长度有关系 长度1000的时候为100
    controlRange = int(100 * length / 1000)
    # 步数 和移动长度有关系 长度1000的时候为100
    steps = int(100 * length / 1000)

    while True:
        # 移动时间间隔
        Interval = defaultInterval + randomTwo() * 2

        # 移动到指定位置后则不做移动
        start_x, start_y = pyautogui.position()
        distanceToTarget = math.sqrt((start_x - targetPos[0]) ** 2 + (start_y - targetPos[1]) ** 2)

        if distanceToTarget < 5.0:
            onMoving = False
            break

        if not onMoving:
            onMoving = True

            if startPos[0] - targetPos[0] > 0:
                control_1_x = startPos[0] - randomOne() * controlRange
            else:
                control_1_x = startPos[0] + randomOne() * controlRange

            if startPos[1] - targetPos[1] > 0:
                control_1_y = startPos[1] - randomOne() * controlRange
            else:
                control_1_y = startPos[1] + randomOne() * controlRange

            control_2_x = targetPos[0] + randomTwo() * controlRange
            control_2_y = targetPos[1] + randomTwo() * controlRange
            controlPoints = [startPos, (control_1_x, control_1_y), (control_2_x, control_2_y), targetPos]

            currentStep = 0
            lastTime = int(time.time_ns() / 1000000)
        else:
            now = int(time.time_ns() / 1000000)
            if (now - lastTime) >= Interval:
                # 利用总步数和当前步数计算t进度
                t = currentStep / steps
                # 计算下个移动坐标进行间隔计算，用于鼠标相对移动
                nextPos = bezierCurve(controlPoints, t)
                mouseMoveTo(nextPos)
                currentStep = currentStep + 1
                lastTime = int(time.time_ns() / 1000000)
            if currentStep > steps:
                controlPoints = [controlPoints[3],
                                 (controlPoints[3][0] + randomTwo() * controlRange,
                                  controlPoints[3][1] + randomOne() * controlRange * 2),
                                 (targetPos[0] + randomTwo() * controlRange,
                                  targetPos[1] + randomOne() * controlRange * 2),
                                 targetPos]
                currentStep = 0


time.sleep(2)
start_x, start_y = pyautogui.position()
simulateMouseMove((start_x, start_y), (500, 500))
