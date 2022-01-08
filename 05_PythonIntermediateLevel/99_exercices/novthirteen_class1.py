import numpy as np
from PIL import Image

img = Image.open('librarybookszoom.jpg')
arr =  np.array((img))



print(arr)