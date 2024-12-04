# Author: Gavin
# Time_Created: 12/4/24
# Description:
import math
r = input('The radius of the cycle is (unit:m):')
r = float(r)
area = math.pi * r * r
circum = 2 * math.pi * r
print('该圆的面积是：',area,'平方米','周长是：',circum,'米')