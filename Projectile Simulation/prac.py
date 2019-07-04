# import pyglet

# music = pyglet.resource.media('drop.mp3')
# music.play()

# pyglet.app.run()

import pygame

pygame.mixer.init()
pygame.mixer.music.load("drop.wav")
pygame.mixer.music.play()
