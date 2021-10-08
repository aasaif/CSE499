

from keras.preprocessing.image import ImageDataGenerator
from skimage import io

# Construct an instance of the ImageDataGenerator class
# Pass the augmentation parameters through the constructor. 

datagen = ImageDataGenerator(
        rotation_range=45,     #Random rotation between 0 and 45
        width_shift_range=0.0,   #% shift
        height_shift_range=0.0,
        shear_range=0.0,
        zoom_range=0.0,
        horizontal_flip=True,
        vertical_flip=True,
        fill_mode='constant', cval=0)    #Also try nearest, constant, reflect, wrap


#####################################################################
#Multiclass. Read dirctly from the folder structure using flow_from_directory

i = 0
for batch in datagen.flow_from_directory(directory='C:/Users/hp/Desktop/Retina/Research Lab/Drive/', 
                                         batch_size=16,  
                                         target_size=(512, 512),
                                         color_mode="rgb",
                                         save_to_dir='C:/Users/hp/Desktop/Retina/Research Lab/Rafid', 
                                         save_prefix='aug', 
                                         save_format='jpg'):
    i += 1
    if i > 50:
        break 












