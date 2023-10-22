import turtle as t
import random

# import colorgram
# colors = colorgram.extract('copia.jpg', 30)
# color_list = []
#
# for x in range(30):
#     r = colors[x].rgb.r
#     g = colors[x].rgb.g
#     b = colors[x].rgb.b
#     color_value = (r, g, b)
#     color_list.append(color_value)
#
# print(color_list)

color_list = [(202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138), (53, 93, 124),
 (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41),
 (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72),
 (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212)]

ponto = t.Turtle()
t.colormode(255)
ponto.pensize(20)
ponto.pu()
posicao_coluna = -250
posicao_linha = -250
ponto.setpos(posicao_linha, posicao_coluna)

#print(color_list.__len__())

def select_color():
    color = random.choice(color_list)
    return color


for coluna in range (10):

 for linha in range (10):
  ponto.dot(26, select_color())
  ponto.forward(60)

 posicao_coluna += 60
 #ponto.sety(coluna)
 ponto.setpos(posicao_linha, posicao_coluna)

screen = t.Screen()
screen.exitonclick()