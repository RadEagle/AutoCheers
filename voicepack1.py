import os
import random
import math
import pyglet

# Select character
character = 'nia'

# Let pyglet access all files inside directory
pyglet.options['search_local_libs'] = True
audio_dir = os.listdir(character)

# Initialize a history list
file_path = '{}/history.txt'.format(character)
try:
    history_file = open(file_path, 'r+')
    history_list = history_file.read().split("\n")
except FileNotFoundError:
    history_file = open(file_path, 'w')
    history_list = []

# Get .wav files
waves = []
for filename in audio_dir:
    if '.wav' in filename:
        waves.append(filename)

# Get a random value
x = random.choice(waves)
while x in history_list:
    x = random.choice(waves)

# Append x to history_list
# This ensures the 35% recent clips won't be played again
restriction = math.ceil(len(waves) * 0.35)
history_list.append(x)
if len(history_list) > restriction:
    history_list.pop(0)

# Print to history file
history_file.seek(0)
history_file.write('\n'.join(history_list))
history_file.truncate()
history_file.close()

# Load media
audio_file = '{}/{}'.format(character, x)
audio = pyglet.media.load(audio_file)
player = pyglet.media.Player()
player.queue(audio)
player.play()

# Run once, then stop
player.on_eos = pyglet.app.exit
pyglet.app.run()
