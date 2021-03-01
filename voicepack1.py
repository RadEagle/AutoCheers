import os
import numpy as np
import pyglet

# Let pyglet access all files inside directory
pyglet.options['search_local_libs'] = True

# Get a random value
file_count = len(os.listdir('keqing'))
x = np.random.randint(1, file_count)

# Load media
audio_file = 'keqing/{}.wav'.format(x)
audio = pyglet.media.load(audio_file)
player = pyglet.media.Player()
player.queue(audio)
player.play()

# Run once, then stop
player.on_eos = pyglet.app.exit
pyglet.app.run()
