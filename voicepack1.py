import os
import random
import pyglet

# Let pyglet access all files inside directory
pyglet.options['search_local_libs'] = True
audio_dir = os.listdir('keqing')

# Initialize a history list
try:
    history_file = open('history1.txt', 'r+')
    history_list = history_file.read().split("\n")
except FileNotFoundError:
    history_file = open('history1.txt', 'w')
    history_list = []

# Get .wav file count
waves = []
for filename in audio_dir:
    if '.wav' in filename:
        waves.append(filename)

# Get a random value
x = random.choice(waves)
while x in history_list:
    x = random.choice(waves)

# Append x to history_list
# This ensures the 3 recent clips won't be played again
history_list.append(x)
if len(history_list) > 3:
    history_list.pop(0)

# Print to history file
history_file.seek(0)
history_file.write('\n'.join(history_list))
history_file.truncate()
history_file.close()

# Load media
audio_file = 'keqing/{}'.format(x)
audio = pyglet.media.load(audio_file)
player = pyglet.media.Player()
player.queue(audio)
player.play()

# Run once, then stop
player.on_eos = pyglet.app.exit
pyglet.app.run()
