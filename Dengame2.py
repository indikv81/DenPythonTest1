import math
import time
import pygame, sys
from pygame.locals import *
pygame.init()
(windows_width, windows_height, windows_title) = (600, 400, "Simple Figure")
screen = pygame.display.set_mode((windows_width,windows_height),0,32)
pygame.display.set_caption(windows_title)
windows_bgcolor = (255,255,255)
mainLoop = True
#initial data here
rect_1_color = (255,0,255)
rect_1_rect = Rect((10,10),(100,100))
rect_1_width = 0
rect_2_color = (0, 0, 255)
rect_2_rect = Rect((150,150),(300,100))
rect_2_width = 4
poligon_color = (255, 0, 0)
poligon_points = [(200,200),(300,300),(400,150)]
poligon_width = 0
circle_color = (0,0,255)
circle_pos = (100,300)
circle_radius = 75
circle_width = 0
ellipse_color = (0,255,0)
ellipse_rect = Rect((200,10),(350,150))
ellipse_width = 0
arc_color = (0,0,0)
arc_rect = Rect((200,250),(300,100))
arc_start_angle = math.pi
arc_end_angle = math.pi * 0.5
line_start_pos = (100,100)
line_end_pos = (300,300)
aaline_start_pos = (110,100)
aaline_end_pos = (310,300)
lines_color = (0,0,0)
lines_points = [(40,50),(300,90),(70,300),(400, 232),(245,100)]
lines_closed = False
lines_width = 8
while mainLoop:
  for event in pygame.event.get():
    print(event)
    if event.type != QUIT:
      #mainLoop = False
      screen.fill(windows_bgcolor)
      #create frame here
      pygame.draw.rect(screen, rect_1_color, rect_1_rect, rect_1_width)
      pygame.draw.rect(screen, rect_2_color, rect_2_rect, rect_2_width)
      pygame.draw.polygon(screen, poligon_color, poligon_points, poligon_width)
      pygame.draw.circle(screen, circle_color, circle_pos, circle_radius, circle_width)
      pygame.draw.ellipse(screen, ellipse_color, ellipse_rect, ellipse_width)
      pygame.draw.arc(screen, arc_color, arc_rect, arc_start_angle, arc_end_angle)
      pygame.draw.line(screen, lines_color, line_start_pos, line_end_pos)
      pygame.draw.aaline(screen, lines_color, aaline_start_pos, aaline_end_pos, 0)
      pygame.draw.lines(screen, lines_color, lines_closed,lines_points,lines_width)
      pygame.display.update()
time.sleep(5)
  #pygame.quit()
#destroy data here
