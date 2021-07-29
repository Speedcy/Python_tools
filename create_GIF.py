# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 15:52:06 2021

@author: cypri
"""

from PIL import Image


nb_image=29
# Create the frames
frames = []
for i in range(nb_image):
    new_frame = Image.open('img/Tension'+str(i)+'.png')
    frames.append(new_frame)
    if i==2 or i==27 or i==28:
        frames.append(new_frame)
        frames.append(new_frame)
        frames.append(new_frame)
        frames.append(new_frame)
        frames.append(new_frame)
        frames.append(new_frame)
            
        
 
# Save into a GIF file that loops forever
frames[0].save('png_to_gif.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=300, loop=0)