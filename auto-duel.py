from imagesearch import *
import pyautogui as pa

folder = "./duel-links/"
character = "aster"

total_duel = 3

for i in range(total_duel):

    # Find gate button
    pos = imagesearch_loop(folder+"gate.png", 0.5)
    print("Gate button found : ", pos[0], pos[1])

    # Click gate button
    if pos[0] != -1:
        click_image(folder+"gate.png", pos, "left", 2)
    print("Gate button clicked")

    # Find duel button #1
    pos = imagesearch_loop(folder+"duel.png", 0.5)
    print("Duel button found : ", pos[0], pos[1])

    # Click duel button #1
    if pos[0] != -1:
        click_image(folder+"duel.png", pos, "left", 1)
    print("Duel button clicked")

    # Find character (Example : Aster Phoenix)
    pos = imagesearch_loop(folder+"char_"+character+".png", 0.5)
    print("Character found : ", pos[0], pos[1])

    # Click character
    if pos[0] != -1:
        click_image(folder+"char_"+character+".png", pos, "left", 1.5)
    print("Character clicked")

    # Find duel button #2
    pos = imagesearch_loop(folder+"duel.png", 0.5)
    print("Duel button found : ", pos[0], pos[1])

    # Click duel button #2
    if pos[0] != -1:
        click_image(folder+"duel.png", pos, "left", 1)
    print("Duel button clicked")

    # Summon monster
    monster_count = 0

    # Loop starts here
    finished = False

    while not finished:
        # Speed up loading animation by clicking mouse until "Your main phase" text shown
        search = True
        while search:
            pos = imagesearch(folder+"main_phase.png")
            if pos[0] != -1:
                search = False
            for i in range(3):
                pa.click(x=960, y=832)
                time.sleep(0.1)
            time.sleep(0.2)
        print("Your main phase")

        time.sleep(0.2)
        if monster_count < 3:
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
            click_image(folder+"action.png", pos, "left", 0.2)
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

        if monster_count >= 1:
            # Monster #1 attack
            # Find monster #1 location
            time.sleep(0.2)
            pa.click(x=958, y=667)
            # Find attack #1 button
            pos = imagesearch_loop(folder+"attack.png", 0.1)
            print("Attack #1 button found : ", pos[0], pos[1])

            # Click attack #1 button
            if pos[0] != -1:
                click_image(folder+"attack.png", pos, "left", 0.1)
            print("Attack #1 button clicked")

            # Check if finished
            time.sleep(2.5)
            pos = imagesearch(folder+"battle_phase_status.png")
            if pos[0] == -1:
                break

        if monster_count >= 2:
            # Monster #2 attack
            # Find monster #2 location
            pa.click(x=1086, y=667)
            # Find attack #2 button
            pos = imagesearch_loop(folder+"attack.png", 0.1)
            print("Attack #2 button found : ", pos[0], pos[1])

            # Click attack #2 button
            if pos[0] != -1:
                click_image(folder+"attack.png", pos, "left", 0.1)
            print("Attack #2 button clicked")

            # Check if finished
            time.sleep(2.5)
            pos = imagesearch(folder+"battle_phase_status.png")
            if pos[0] == -1:
                break

        if monster_count >= 3:
            # Monster #3 attack
            # Find monster #3 location
            pa.click(x=833, y=671)
            # Find attack #3 button
            pos = imagesearch_loop(folder+"attack.png", 0.1)
            print("Attack #3 button found : ", pos[0], pos[1])

            # Click attack #3 button
            if pos[0] != -1:
                click_image(folder+"attack.png", pos, "left", 0.1)
            print("Attack #3 button clicked")

            # Check if finished
            time.sleep(2.5)
            pos = imagesearch(folder+"battle_phase_status.png")
            if pos[0] == -1:
                break

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
            pa.click(x=960, y=832)
            time.sleep(0.1)
        time.sleep(0.2)
    print("Next button found")

    # Click next button
    if pos[0] != -1:
        click_image(folder+"next.png", pos, "left", 0.1)
    print("Next button clicked")

    # Wait next button
    search = True
    while search:
        pos = imagesearch(folder+"next.png")
        if pos[0] != -1:
            search = False
        for i in range(3):
            pa.click(x=960, y=832)
            time.sleep(0.1)
        time.sleep(0.2)
    print("Next button found")

    # Click next button
    if pos[0] != -1:
        click_image(folder+"next.png", pos, "left", 0.5)
    print("Next button clicked")

    # Find character (Example : Aster Phoenix)
    pos = imagesearch_loop(folder+"char_"+character+".png", 0.5)
    print("Character found : ", pos[0], pos[1])

    # Click character
    if pos[0] != -1:
        click_image(folder+"char_"+character+".png", pos, "left", 1.5)
    print("Character clicked")