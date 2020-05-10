from imagesearch import *
import pyautogui as pa

folder = "./image/event-tag-duel/"

elements = ['ok', 'tag_duel', 'hard_level']
total_duel = 100
duel_count = 0
while duel_count < total_duel:
    for i in range(7):
        pa.click(x=960, y=119)
        time.sleep(0.05)

    pos = imagesearch(folder+"event_flow.png")
    if pos[0] > -1:
        # Scroll to DM cup
        pa.moveTo(x=1126, y=746)
        for i in range(7):
            pa.scroll(-10)
        pos = imagesearch(folder+"DM_cup.png")
        if (pos[0] > -1):
            click_image(folder+"DM_cup.png", pos, "left", 0.1)

    for element in elements:
        pos = imagesearch(folder+element+".png")
        if pos[0] != -1:
            click_image(folder+element+".png", pos, "left", 0.1)
            # print(element+".png duel clicked")

    pos = imagesearch(folder+"auto_duel.png")
    if pos[0] != -1:
        if duel_count > 0:
            print("Duel done : "+str(duel_count))
        click_image(folder+"auto_duel.png", pos, "left", 0.2)
        duel_count += 1
        # print("auto_duel.png clicked")

    pos = imagesearch(folder+"logo_tag_duel.png")
    if pos[0] != -1:
        for i in range(7):
            pa.click(x=960, y=119)
            time.sleep(0.05)

print("Duel done : "+str(duel_count))