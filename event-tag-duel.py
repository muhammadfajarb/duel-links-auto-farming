from imagesearch import *
import pyautogui as pa

folder = "./image/event-tag-duel/"

while True:
    print('Search tag duel button')
    # Click tag duel button
    for i in range(10):
        pa.click(x=960, y=119)
        time.sleep(0.05)
    search = True
    while search:
        for i in range(10):
            pa.click(x=960, y=119)
            time.sleep(0.05)
        # time.sleep(7)
        pos = imagesearch_loop_timeout(folder+"tag_duel.png", 0.1, 2)
        # pos = imagesearch(folder+"tag_duel.png")
        if pos[0] > -1:
            search = False
            click_image(folder+"tag_duel.png", pos, "left", 0.1)
        else:
            pos2 = imagesearch_loop_timeout(folder+"event_flow.png", 0.1, 2)
            if pos2[0] > -1:
                # Scroll to DM cup
                pa.moveTo(x=1126, y=746)
                for i in range(7):
                    pa.scroll(-10)
                pos2 = imagesearch_loop(folder+"DM_cup.png", 0.1)
                if (pos2[0] > -1):
                    click_image(folder+"DM_cup.png", pos2, "left", 0.1)

    print('Search hard level')
    # Click hard level
    search = True
    while search:
        pos = imagesearch(folder+"hard_level.png")
        if pos[0] > -1:
            search = False
        for i in range(3):
            pa.click(x=960, y=119)
            time.sleep(0.1)
        time.sleep(0.1)

    click_image(folder+"hard_level.png", pos, "left", 0.5)

    # Click auto duel
    search = True
    while search:
        pos = imagesearch(folder+"auto_duel.png")
        if pos[0] > -1:
            search = False
        for i in range(3):
            pa.click(x=960, y=119)
            time.sleep(0.1)
        time.sleep(0.1)

    click_image(folder+"auto_duel.png", pos, "left", 0.1)

    # Click OK
    time.sleep(20)
    search = True
    while search:
        pos = imagesearch(folder+"ok.png")
        if pos[0] > -1:
            search = False
        for i in range(3):
            pa.click(x=960, y=119)
            time.sleep(0.01)
        time.sleep(0.1)

    click_image(folder+"ok.png", pos, "left", 0.1)

    search = True
    while search:
        pos = imagesearch(folder+"ok.png")
        if pos[0] > -1:
            search = False
        for i in range(3):
            pa.click(x=960, y=119)
            time.sleep(0.01)
        time.sleep(0.1)

    click_image(folder+"ok.png", pos, "left", 0.1)

    search = True
    while search:
        pos = imagesearch(folder+"ok.png")
        if pos[0] > -1:
            search = False
        for i in range(3):
            pa.click(x=960, y=119)
            time.sleep(0.01)
        time.sleep(0.1)

    click_image(folder+"ok.png", pos, "left", 0.1)