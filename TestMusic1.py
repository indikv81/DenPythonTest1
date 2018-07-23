import pygame as pg
from playsound import playsound

#playsound("c:/test/music.mp3")

''' pg_playmp3f.py
play MP3 music files using Python module pygame
pygame is free from: http://www.pygame.org
(does not create a GUI frame in this case)
'''

def play_music(music_file, volume=0.8):
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''
    # set up the mixer
    freq = 44100  # audio CD quality
    bitsize = -16  # unsigned 16 bit
    channels = 2  # 1 is mono, 2 is stereo
    buffer = 2048  # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)
    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    tt = 1
    try:
        pg.mixer.music.load(music_file)
        print("Музыкальный файл {} загружен!".format(music_file))
    except pg.error:
        print("Файл {} не найден ({})".format(music_file, pg.get_error()))
        return
    pg.mixer.music.play()
    n = 0
    while pg.mixer.music.get_busy():
        # check if playback has finished
        print(n, end=' ', flush=True)
        n += 1
        clock.tick(1)


# pick a MP3 music file you have in the working folder
# otherwise give the full file path
# (try other sound file formats too)
music_file = "c:/test/music.mp3"
# optional volume 0 to 1.0
volume = 1.0
play_music(music_file, volume)