import pyglet

sound = pyglet.resource.media('drop.wav', streaming=False)
sound.play()