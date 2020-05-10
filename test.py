from imagesearch import *

folder = "./image/"

pos = imagesearch(folder+"first_turn.png")
if pos[0] > -1:
    print('Found')
