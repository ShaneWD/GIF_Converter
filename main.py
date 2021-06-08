import os

video_name = input("""
What is the video name? 
Make sure to include the format as well
ex: the video.mp4

>""")

new_name = input("""
What is the new file name?
Make sure to add the ".gif" at the end
ex: the video.gif 

>""")

os.system(f""" ffmpeg -i "{video_name}"  -vf scale=1920:-1 -r 60 -filter:v "setpts=0.35*PTS" "{new_name}" """)
# the "setpts" adjust how fast the gif will play
# "setpts=0.35*PTS" plays the gif basically at normal speed, however, adjust if necessary
# 1920 is the scale, adjust if necessary
# 60 is the FPS, adjust if necessary
