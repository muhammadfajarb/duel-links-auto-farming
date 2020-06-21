from imagesearch import *
import pyautogui as pa

folder = "./image/"
# character = "yugi"
character = "weevil"

# total_duel = 30

# for i in range(total_duel):
while True:
    # Find gate button
    pos = imagesearch_loop(folder+"gate.png", 0.5)
    print("Gate button found : ", pos[0], pos[1])

    # Click gate button
    if pos[0] != -1:
        click_image(folder+"gate.png", pos, "left", 1)
    print("Gate button clicked")

    # Find duel button #1
    pos = imagesearch_loop(folder+"duel.png", 0.3)
    print("Duel button found : ", pos[0], pos[1])

    # Click duel button #1
    if pos[0] != -1:
        click_image(folder+"duel.png", pos, "left", 0.5)
    print("Duel button clicked")

    # # Dialog box
    # time.sleep(0.2)
    # pos = imagesearch(folder+"yes.png")
    # if pos[0] > -1:
    #     # Click to confirm
    #     pos = imagesearch(folder+"yes.png")
    #     if pos[0] > -1:
    #         click_image(folder+"yes.png", pos, "left", 0.1)

    # Find character (Example : Aster Phoenix)
    pos = imagesearch_loop(folder+"char_"+character+".png", 0.3)
    print("Character found : ", pos[0], pos[1])

    # Click character
    if pos[0] != -1:
        click_image(folder+"char_"+character+".png", pos, "left", 1.5)
        click_image(folder+"char_"+character+".png", pos, "left", 0.1)
    print("Character clicked")

    # Find duel button #2
    pos = imagesearch_loop(folder+"duel.png", 0.3)
    print("Duel button found : ", pos[0], pos[1])

    # Click duel button #2
    if pos[0] != -1:
        click_image(folder+"duel.png", pos, "left", 0.3)
    print("Duel button clicked")

    search = True
    while search:
        pos = imagesearch(folder+"menu.png")
        if pos[0] != -1:
            search = False
        for i in range(7):
            pa.click(x=960, y=832)
            time.sleep(0.01)
        time.sleep(0.1)
    print("Duel standby")

    # Summon monster
    monster_count = 0

    # Loop starts here
    finished = False

    # Timeout in second
    timeout = 0

    while not finished:
        # Speed up loading animation by clicking mouse until "Your main phase" text shown
        
        # pos = imagesearch(folder+"main_phase.png")
        # if (pos[0] == -1):
        #     print("Your draw phase")
        #     time.sleep(7)
        #     search = True
        #     while search:
        #         pos = imagesearch(folder+"draw_phase.png")
        #         if (pos[0] != -1):
        #             for i in range(7):
        #                 pa.click(x=960, y=832)
        #                 time.sleep(0.01)
        #         else:
        #             search = False
        #         time.sleep(0.1)

        # pos = imagesearch(folder+"first_turn.png")
        # if pos[0] > -1:
        #     timeout = 1.0
        # else:
        #     timeout = 20.0
            
        # pos = imagesearch_loop_timeout(folder+"draw_phase.png", 0.1, timeout)
        # if (pos[0] > -1):
        #     time.sleep(1)
        #     for i in range(7):
        #         pa.click(x=960, y=832)
        #         time.sleep(0.05)
        #     time.sleep(1)
        #     for i in range(3):
        #         pa.click(x=960, y=832)
        #         time.sleep(0.1)
        
        while True:
            pa.click(x=620, y=820)
            pos = imagesearch(folder+"action.png")
            if pos[0] > -1:
                break
            time.sleep(0.05)
        
        print("Your main phase")
        # imagesearch_loop(folder+"action.png", 0.1)
        time.sleep(1)

        # search = True
        # while search:
        #     pos = imagesearch(folder+"main_phase.png")
        #     if pos[0] != -1:
        #         search = False
        #     # for i in range(3):
        #     #     pa.click(x=960, y=832)
        #         # time.sleep(0.1)
        #     time.sleep(0.1)

        # imagesearch_loop(folder+"main_phase.png", 0.1)
        # time.sleep(1)

        if monster_count < 2:
        # if monster_count < 3:
            # Click monster on hand
            pa.click(x=953, y=1035)

            # Find normal summon button
            pos = imagesearch_loop(folder+"normal_summon.png", 0.1)
            print("Normal summon button found : ", pos[0], pos[1])

            # Click normal summon button
            if pos[0] != -1:
                click_image(folder+"normal_summon.png", pos, "left", 0.1)
            print("Normal summon button clicked")

            # Increment monster count
            monster_count += 1

        # Find action button
        pos = imagesearch_loop(folder+"action.png", 0.1)
        print("Action button found : ", pos[0], pos[1])

        # Click action button
        if pos[0] != -1:
            click_image(folder+"action.png", pos, "left", 0.15)
        print("Action button clicked")

        # Find battle phase button
        time.sleep(0.5)
        pos = imagesearch(folder+"battle_phase.png")
        if pos[0] != -1:
            print("Battle phase button found : ", pos[0], pos[1])
            # Click battle phase button
            click_image(folder+"battle_phase.png", pos, "left", 0.1)
            print("Battle phase button clicked")
        else:
            # You can't attack if you get the first turn
            pos = imagesearch_loop(folder+"end_phase.png", 0.1)
            # Click end phase button
            if pos[0] != -1:
                click_image(folder+"end_phase.png", pos, "left", 0.1)
            print("End phase button clicked")

            # Skip battle phase
            continue
        
        imagesearch_loop(folder+"action.png", 0.1)

        if monster_count >= 1:
            # Monster #1 attack
            # Find monster #1 location
            time.sleep(0.5)
            pa.click(x=958, y=667)
            # Find attack #1 button
            pos = imagesearch_loop(folder+"attack.png", 0.1)
            print("Attack #1 button found : ", pos[0], pos[1])

            # Click attack #1 button
            if pos[0] != -1:
                click_image(folder+"attack.png", pos, "left", 0.1)
            print("Attack #1 button clicked")

            # Check if finished
            time.sleep(3)
            pos = imagesearch(folder+"battle_phase_status.png")
            if pos[0] == -1:
                break
        
        imagesearch_loop(folder+"action.png", 0.1)

        if monster_count >= 2:
            # Monster #2 attack
            # Find monster #2 location
            # time.sleep(3)
            pa.click(x=1086, y=667)
            # Find attack #2 button
            pos = imagesearch_loop(folder+"attack.png", 0.1)
            print("Attack #2 button found : ", pos[0], pos[1])

            # Click attack #2 button
            if pos[0] != -1:
                click_image(folder+"attack.png", pos, "left", 0.1)
            print("Attack #2 button clicked")

            # Check if finished
            time.sleep(3)
            pos = imagesearch(folder+"battle_phase_status.png")
            if pos[0] == -1:
                break

        # if monster_count >= 3:
        #     # Monster #3 attack
        #     # Find monster #3 location
        #     pa.click(x=833, y=671)
        #     # Find attack #3 button
        #     pos = imagesearch_loop(folder+"attack.png", 0.1)
        #     print("Attack #3 button found : ", pos[0], pos[1])

        #     # Click attack #3 button
        #     if pos[0] != -1:
        #         click_image(folder+"attack.png", pos, "left", 0.1)
        #     print("Attack #3 button clicked")

        #     # Check if finished
        #     time.sleep(2.5)
        #     pos = imagesearch(folder+"battle_phase_status.png")
        #     if pos[0] == -1:
        #         break

        if not finished:
            pos = imagesearch_loop(folder+"action.png", 0.1)
            print("Action button found : ", pos[0], pos[1])

            # Click action button
            if pos[0] != -1:
                click_image(folder+"action.png", pos, "left", 0.1)
            print("Action button clicked")

            # Find end phase button
            pos = imagesearch_loop(folder+"end_phase.png", 0.1)
            print("End phase button found : ", pos[0], pos[1])

            # Click end phase button
            if pos[0] != -1:
                click_image(folder+"end_phase.png", pos, "left", 0.1)
            print("End phase button clicked")
        
    # Wait ok button
    search = True
    while search:
        pos = imagesearch(folder+"ok.png")
        if pos[0] != -1:
            search = False
        for i in range(3):
            pa.click(x=960, y=832)
            time.sleep(0.1)
        time.sleep(0.2)
    print("OK button found")

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
            pa.click(x=960, y=119)
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


    # # Mission circuit / Duel Quiz

    # # Click
    # for i in range(5):
    #     pa.click(x=960, y=119)
    #     time.sleep(0.1)
    
    # time.sleep(5)
    
    # # Wait ok button
    # search = True
    # while search:
    #     pos = imagesearch(folder+"ok.png")
    #     if pos[0] != -1:
    #         search = False
    #     for i in range(3):
    #         # pa.click(x=960, y=832)
    #         pa.click(x=960, y=119)
    #         time.sleep(0.1)
    #     time.sleep(0.3)
    # print("Ok button found")

    # # Click ok button
    # if pos[0] != -1:
    #     click_image(folder+"ok.png", pos, "left", 0.5)
    # print("Ok button clicked")

    # # Click Ok button
    # for i in range(5):
    #     pa.click(x=960, y=119)
    #     time.sleep(0.1)

    # Find character
    pos = imagesearch_loop(folder+"char_"+character+".png", 0.5)
    print("Character found : ", pos[0], pos[1])

    # Click character
    if pos[0] != -1:
        click_image(folder+"char_"+character+".png", pos, "left", 1.5)
    print("Character clicked")