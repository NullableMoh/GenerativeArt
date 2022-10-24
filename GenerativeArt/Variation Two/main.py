import os
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

#iterations
max_iterations = 100

#main loop, alter image per iteration
for i in range(max_iterations):
    #save image
    current_image.save(f"{save_dir}/{i}.png")

    #progress counter
    print(f"Iteration {i}") if i % 10 == 0 else None
    


def gifit(image_location, gif_name, fps=24):
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
    
