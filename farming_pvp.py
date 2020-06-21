from imagesearch import *
import pyautogui as pa

folder = "./image/"
duel_counter = 0

while True:

    # Find duel button #1
    pos = imagesearch_loop(folder+"duel_pvp.png", 0.3)
    print("Duel button found : ", pos[0], pos[1])

    # Click duel button #1
    if pos[0] != -1:
        click_image(folder+"duel_pvp.png", pos, "left", 0.5)
    print("Duel button clicked")

    pos = imagesearch_loop_timeout(folder+"menu.png", 0.1, 120.0)
    if pos[0] > -1:
        for i in range(7):
            pa.click(x=964, y=549)
            time.sleep(0.1)
    else:
        break
    print("Duel standby")

    # imagesearch_loop_timeout(folder+"main_phase.png", 0.1)
    # print("Your main phase")

    search = True

    while search:

        # Special summon Lava Golem
        pos = imagesearch(folder+"special_summon.png")
        # pos = imagesearch_loop_timeout(folder+"special_summon.png", 0.1, 1)
        if (pos[0] > -1):
            click_image(folder+"special_summon.png", pos, "left", 0.1)
            counter = 0
            max_counter -= 1
            monster_exist = True
            # Confirm to special summon monster
            pos = imagesearch_loop_timeout(folder+"confirm_ss_disabled.png", 0.1, 5.0)
            if pos[0] > -1:
                # Click card to activate
                time.sleep(1)
                pa.click(x=836, y=559)
                pos = imagesearch_loop_timeout(folder+"confirm_ss_enabled.png", 0.1, 5.0)
                if pos[0] > -1:
                    click_image(folder+"confirm_ss_enabled.png", pos, "left", 0.1)
        
        # Dialog box
        pos = imagesearch_loop_timeout(folder+"yes.png", 0.1, 1.0)
        if pos[0] > -1:
            # Click to confirm
            pa.click(x=667, y=793) 
            pos = imagesearch(folder+"yes.png")
            if pos[0] > -1:
                click_image(folder+"yes.png", pos, "left", 0.1)

        # Find if any card to activate
        pos = imagesearch(folder+"activate_disabled.png")
        if pos[0] > -1:
            # Click card to activate
            pa.click(x=667, y=793) 
            pos = imagesearch(folder+"activate_enabled.png")
            if pos[0] > -1:
                click_image(folder+"activate_enabled.png", pos, "left", 0.1)
        
        # Find if any card to confirm
        pos = imagesearch(folder+"confirm_disabled.png")
        if pos[0] > -1:
            # Click card to confirm
            pa.click(x=667, y=793) 
            pos = imagesearch(folder+"confirm_enabled.png")
            if pos[0] > -1:
                click_image(folder+"confirm_enabled.png", pos, "left", 0.1)

        # Activate cards
        while True:
            pos = imagesearch_loop_timeout(folder+"action.png", 0.1, 9.0, 0.9)
            if pos[0] > -1:
                pa.click(x=958, y=1034)
                pos1 = imagesearch_loop_timeout(folder+"activate.png", 0.1, 3)
                if (pos1[0] > -1):
                    click_image(folder+"activate.png", pos1, "left", 0.1)
                else:
                    pos2 = imagesearch_loop_timeout(folder+"set.png", 0.1, 3)
                    if (pos2[0] > -1):
                        click_image(folder+"set.png", pos2, "left", 0.1)
                    else:
                        pa.click(x=611, y=819)
                        time.sleep(0.5)
                        # Find and click action button
                        pos = imagesearch(folder+"action.png", 0.9)
                        print("Action button found : ", pos[0], pos[1])
                        # Click action button
                        if pos[0] > -1:
                            click_image(folder+"action.png", pos, "left", 0.1)
                            print("Action button clicked")

                            # Find end phase button
                            pos = imagesearch_loop_timeout(folder+"end_phase.png", 0.1, 2)
                            print("End phase button found : ", pos[0], pos[1])

                            # Click end phase button
                            if pos[0] > -1:
                                click_image(folder+"end_phase.png", pos, "left", 0.1)
                            print("End phase button clicked")
                        break
            else:
                pa.click(x=611, y=819)
                break
                
        # # Find and click action button
        # pos = imagesearch(folder+"action.png", 0.9)
        # print("Action button found : ", pos[0], pos[1])
        # # Click action button
        # if pos[0] > -1:
        #     click_image(folder+"action.png", pos, "left", 0.1)
        #     print("Action button clicked")

        #     # Find end phase button
        #     pos = imagesearch_loop_timeout(folder+"end_phase.png", 0.1, 2)
        #     print("End phase button found : ", pos[0], pos[1])

        #     # Click end phase button
        #     if pos[0] > -1:
        #         click_image(folder+"end_phase.png", pos, "left", 0.1)
        #     print("End phase button clicked")
        
        # for i in range(7):
        #     pa.click(x=964, y=549)
        #     time.sleep(0.1)
            
        # Check if duel finished
        pos = imagesearch(folder+"ok.png")
        if pos[0] > -1:
            duel_counter += 1
            break
   
    for i in range(3):
        pa.click(x=960, y=832)
        time.sleep(0.1)
    time.sleep(0.2)
    print("Duel Finished : "+str(duel_counter))

    # Click ok button
    if pos[0] != -1:
        click_image(folder+"ok.png", pos, "left", 0.1)
    print("OK button clicked")

    # Wait next button
    search = True
    while search:
        pos = imagesearch(folder+"next.png")
        if pos[0] != -1:
            search = False
        for i in range(3):
            # pa.click(x=960, y=832)
            pa.click(x=964, y=549)
            time.sleep(0.3)
        time.sleep(0.3)
    print("Next button found")

    # Click next button
    if pos[0] != -1:
        click_image(folder+"next.png", pos, "left", 0.5)
    print("Next button clicked")

    # Wait next button
    search = True
    while search:
        pos = imagesearch(folder+"next.png")
        if pos[0] != -1:
            search = False
        for i in range(3):
            # pa.click(x=960, y=832)
            pa.click(x=960, y=119)
            time.sleep(0.1)
        time.sleep(0.3)
    print("Next button found")

    # Click next button
    if pos[0] != -1:
        click_image(folder+"next.png", pos, "left", 0.5)
    print("Next button clicked")