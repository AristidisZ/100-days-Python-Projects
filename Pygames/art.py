import random

import colorgram

# Extract 6 colors from an image.
# colors = colorgram.extract('damien.jpg', 30)
# print(type(colors))
# rgb_colors = []
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = r, g, b
#     rgb_colors.append(new_color)
#
# print("list ", rgb_colors)

import turtle as t
import random

color_list = [(229, 222, 210), (223, 159, 80), (39, 107, 149), (118, 164, 192), (150, 63, 88), (207, 134, 157),
              (180, 160, 35), (28, 133, 96), (213, 86, 59), (120, 181, 152), (164, 80, 52), (200, 84, 111),
              (208, 225, 215), (143, 31, 40), (54, 167, 135), (232, 198, 110), (201, 219, 227), (229, 206, 214),
              (6, 109, 90), (41, 160, 185), (117, 114, 163), (238, 159, 174), (30, 62, 112), (153, 211, 199),
              (235, 169, 158), (26, 64, 57), (125, 38, 35), (28, 58, 84), (150, 208, 217), (69, 39, 50)]

window = t.Screen()
window.setup(600, 500)

t.pensize(3)
t.hideturtle()
t.speed(0)
t.colormode(255)


def random_rgb():
    random_color = random.choice(color_list)
    r = random_color[0]
    g = random_color[1]
    b = random_color[2]
    x = (r, g, b)
    return x


print(random_rgb())
pp = -160
for i in range(10):
    t.penup()
    t.setpos(-200, pp)
    for j in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)
    t.setpos(200, pp)
    pp += 40

window.exitonclick()
