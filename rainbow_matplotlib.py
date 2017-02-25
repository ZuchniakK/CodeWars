import numpy as np
import matplotlib.pyplot as plt
import math, colorsys
from BaseConversion import convert
from PIL import Image, ImageDraw
# from colorsys import hsv_to_rgb
#   https://docs.python.org/2/library/colorsys.html

def hsv_to_rgb(h, s, v):
    if s == 0.0: v *= 255; return [v, v, v]
    i = int(h * 6.)  # XXX assume int() truncates!
    f = (h * 6.) - i
    p, q, t = int(255 * (v * (1. - s))), int(255 * (v * (1. - s * f))), int(255 * (v * (1. - s * (1. - f))))
    v *= 255
    i %= 6
    if i == 0: return [v, t, p]
    if i == 1: return [q, v, p]
    if i == 2: return [p, v, t]
    if i == 3: return [p, q, v]
    if i == 4: return [t, p, v]
    if i == 5: return [v, p, q]

import colorsys
test_color = colorsys.hsv_to_rgb(359/360.0, 1, 1)
i_list = []
r_list = []
g_list = []
b_list = []
arg = 0
for i in range(30000):
    [r,g,b] = colorsys.hsv_to_rgb(i/3600.0, 1, 1)
    i_list.append(i)
    r_list.append(r)
    g_list.append(g)
    b_list.append(b)
    # print(int(r*256))
    R, G, B = int(255 * r), int(255 * g), int(255 * b)
    # print(R)
    # print
    dec = '0123456789'
    hexy = '0123456789abcdef'
    # Rh = convert(str(R), dec, hexy)
    # Gh = convert(str(G), dec, hexy)
    # Bh = convert(str(B), dec, hexy)
    Rh = str(hex(R))
    Gh = str(hex(G))
    Bh = str(hex(B))
    print('hexy', Rh, Gh, Bh)
    print(R)
    print(str(hex(R))[2:])
    print(Rh)
    # print(Rh, type(Rh))
    if len(Rh) == 1:
        Rh = '0' + Rh
    if len(Bh) == 1:
        Bh = '0' + Bh
    if len(Gh) == 1:
        Gh = '0' + Gh
    color_rgb = '#' + Rh + Gh + Bh
    # r = i / 60000
    # arg += 1/100/(r+0.001)
    #
    # x = np.sin(arg)*r
    # y = np.cos(arg)*r
    x = i/30000
    y =np.sin(i/50)
    print(color_rgb)
    plt.plot(x,y,'o', color = color_rgb, linestyle='-')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.show()



