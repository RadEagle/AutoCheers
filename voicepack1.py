import os
import random
import pyglet

# Let pyglet access all files inside directory
pyglet.options['search_local_libs'] = True
audio_dir = os.listdir('keqing')

# Get .wav file count
waves = []
for filename in audio_dir:
    if '.wav' in filename:
        waves.append(filename)

# Get a random value
x = random.choice(waves)

# Load media
audio_file = 'keqing/{}'.format(x)
audio = pyglet.media.load(audio_file)
player = pyglet.media.Player()
player.queue(audio)
player.play()

# Run once, then stop
player.on_eos = pyglet.app.exit
pyglet.app.run()
