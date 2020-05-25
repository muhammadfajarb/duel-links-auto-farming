from imagesearch import *
import pyautogui as pa

folder = "./image/event-dimensional-disaster/"

elements = ['ok', 'next']
# total_duel = 300
duel_count = 0

# while duel_count < total_duel:
while True:
    
    pos = imagesearch(folder+"dimension_duel_ex.png")
    if pos[0] > -1:
        click_image(folder+"dimension_duel_ex.png", pos, "left", 0.1)
    else:
        pos = imagesearch(folder+"dimension_duel.png")
        if pos[0] > -1:
            click_image(folder+"dimension_duel.png", pos, "left", 0.1)

    pos = imagesearch(folder+"assist_duel_none.png")
    if pos[0] > -1:
        click_image(folder+"assist_duel_none.png", pos, "left", 0.1)
    else:
        pos = imagesearch(folder+"assist_other_duelists.png")
        if pos[0] > -1:
            click_image(folder+"assist_other_duelists.png", pos, "left", 0.1)
            for i in range(15):
                pa.scroll(-10)
            pos = imagesearch(folder+"assist_duel_none.png")
            if pos[0] != -1:
                new_x = pos[0] - 230
                pa.click(x=new_x, y=pos[1])
        else:
            pos = imagesearch(folder+"assist_duel.png")
            if pos[0] > -1:
                click_image(folder+"assist_duel.png", pos, "left", 0.1)


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
    
    # Skip animation handler
    pa.click(x=620, y=720)

    # pos = imagesearch(folder+"assisting.png")
    # if pos[0] > -1:
    #     pa.scroll(10)
    # pa.click(x=960, y=119)
    # time.sleep(0.2)

# print("Duel done : "+str(duel_count))