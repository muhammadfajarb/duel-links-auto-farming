from imagesearch import *
import pyautogui as pa

folder = "./image/event-dd-castle/"

while True:

    pos = imagesearch_loop(folder+"auto_duel.png", 0.1)
    if pos[0] > -1:
        click_image(folder+"auto_duel.png", pos, "left", 0.5)

    pos = imagesearch_loop(folder+"ok.png", 0.1)
    if pos[0] > -1:
        click_image(folder+"ok.png", pos, "left", 0.5)

    pos = imagesearch_loop(folder+"ok.png", 0.1)
    if pos[0] > -1:
        for i in range(7):
            pa.click(x=960, y=119)
            time.sleep(0.3)
        # time.sleep(3)
        click_image(folder+"ok.png", pos, "left", 0.5)

    # pos = imagesearch_loop(folder+"ok.png", 0.1)
    # if pos[0] > -1:
    #     for i in range(10):
    #         pa.click(x=960, y=119)
    #         time.sleep(0.1)
    #     time.sleep(7)
    #     click_image(folder+"ok.png", pos, "left", 0.5)
    
    pos = imagesearch_loop(folder+"ok.png", 0.1)
    if pos[0] > -1:
        for i in range(5):
            pa.click(x=960, y=119)
            time.sleep(0.1)
        # click_image(folder+"ok.png", pos, "left", 0.5)