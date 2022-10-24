#resources
#http://superfluoussextant.com/generative-art-intro.html


import os
import random
import shutil

from datetime import datetime
from PIL import Image


#get date and use as directory to save to
save_dir = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
os.mkdir(save_dir)
shutil.copy(__file__, save_dir)

#size of image
image_size = (100,100)
#create new image
current_image = Image.new("RGB", image_size)
#get modifiable representation of image
pixels = current_image.load()


#initial setup (make each pixel a random color)
for x in range(0, image_size[0]):
    for y in range(0, image_size[1]):
        pixels[x,y] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))


def get_random_adjacent(location):
    '''get random adjacent pixel that isnt out of bounds'''
    x = location[0]
    y = location[1]
    
    adjacent_values = [(x, y+1), (x, y-1), (x+1, y), (x, y+1)]
    
    adjacent_x, adjacent_y = adjacent_values[random.randint(0,3)]
    
    #keeping x values in bounds
    if adjacent_x < 0:
        adjacent_x = image_size[0]-1
        
    elif adjacent_x > image_size[0]-1:
        adjacent_x = 0
    
    #keeping y values in bounds
    if adjacent_y < 0:
        adjacent_y = image_size[1]-1
    
    elif adjacent_y > image_size[1]-1:
        adjacent_y = 0
        
    return (adjacent_x, adjacent_y)
    
def determine_winner(one_pixel, other_pixel):
    '''pick a winning color given two colors'''
    return one_pixel if one_pixel[0] > other_pixel[0] else other_pixel
    
    
#iterations
max_iterations = 100

#main loop, alter image per iteration
for i in range(max_iterations):
    for x in random.sample(range(current_image.size[0]), current_image.size[0]):
        for y in random.sample(range(current_image.size[1]), current_image.size[1]):
            location = (x,y)
            opponent_location = get_random_adjacent(location)
            
            winner = determine_winner(pixels[location], pixels[opponent_location])
            
            #update pixels
            pixels[location] = winner
            pixels[opponent_location] = winner

        #save image
        current_image.save(f"{save_dir}/{i}.png")

        #progress counter
        print(f"Iteration {i}") if i % 10 == 0 else None
        


def gifit(image_location, gif_name, fps=60):
    '''
    creates gif using all images in providied location
    '''

    import glob
    import moviepy.editor as mpy

    os.chdir(image_location)
    file_list = glob.glob('*.png')
    list.sort(file_list, key=lambda x: int(x.split('.png')[0]))
    clip = mpy.ImageSequenceClip(file_list, fps=fps)
    clip.write_gif(f'{gif_name}.gif',fps=fps)
    
    
gifit(save_dir, 'final')
    
