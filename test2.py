from imagesearch import *
import pyautogui as pa

folder = "./image/"
search = True

    main_phase_status = True
    battle_phase_status = False
    monster_exist = True

    while search:

        # Find if any card to activate (chain)
        pos = imagesearch(folder+"activate_disabled.png")
        if pos[0] > -1:
            # Click card to activate
            pa.click(x=667, y=793) 
            pos = imagesearch(folder+"activate_enabled.png")
            if pos[0] > -1:
                click_image(folder+"activate_enabled.png", pos, "left", 0.1)
        
        init_x = 760
        init_y = 1034
        new_pos = 0
        counter = 0
        max_counter = 5
        
        if main_phase_status:
            pos = imagesearch_loop_timeout(folder+"action.png", 0.1, 2.0)
            if pos[0] > -1:
                while True:
                    pa.click(x=init_x + new_pos, y=init_y)
                    new_pos += 45
                    counter += 1

                    pos = imagesearch_loop_timeout(folder+"special_summon.png", 0.1, 1)
                    if (pos[0] > -1):
                        click_image(folder+"special_summon.png", pos, "left", 0.1)
                        counter = 0
                        max_counter -= 1
                        monster_exist = True
                        # Confirm to special summon monster
                        pos = imagesearch_loop_timeout(folder+"confirm_disabled.png", 0.1, 1)
                        if pos[0] > -1:
                            # Click card to activate
                            pa.click(x=835, y=556) 
                            pos = imagesearch(folder+"confirm_enabled.png")
                            if pos[0] > -1:
                                click_image(folder+"confirm_enabled.png", pos, "left", 0.1)
                    
                    pos = imagesearch_loop_timeout(folder+"normal_summon.png", 0.1, 1)
                    if (pos[0] > -1):
                        click_image(folder+"normal_summon.png", pos, "left", 0.1)
                        counter = 0
                        max_counter -= 1
                        monster_exist = True
                        
                    pos = imagesearch_loop_timeout(folder+"activate.png", 0.1, 1)
                    if (pos[0] > -1):
                        if monster_exist:
                            click_image(folder+"activate.png", pos, "left", 0.1)
                            counter = 0
                            max_counter -= 1
                            # Confirm to select monster
                            pos = imagesearch_loop_timeout(folder+"confirm_disabled.png", 0.1, 5)
                            if pos[0] > -1:
                                # Click card to activate
                                pa.click(x=667, y=793) 
                                pos = imagesearch(folder+"confirm_enabled.png")
                                if pos[0] > -1:
                                    click_image(folder+"confirm_enabled.png", pos, "left", 0.1)
                            
                    pos = imagesearch_loop_timeout(folder+"set.png", 0.1, 1)
                    if (pos[0] > -1):
                        pos2 = imagesearch_loop_timeout(folder+"equip.png", 0.1, 1.0)
                        if pos2[0] == -1:
                            click_image(folder+"set.png", pos, "left", 0.1)
                            counter = 0
                            max_counter -= 1
                        else:
                            max_counter += 1
        
                    if counter >= max_counter:
                        main_phase_status = False
                        if monster_exist:
                            battle_phase_status = True
                            
                        pa.click(x=620, y=820)
                        break

        if battle_phase_status:
            battle_phase_status = False
            # Find and click action button
            pos = imagesearch_loop_timeout(folder+"action.png", 0.1, 5.0)
            print("Action button found : ", pos[0], pos[1])
            # Click action button
            if pos[0] > -1:
                click_image(folder+"action.png", pos, "left", 0.1)
                print("Action button clicked")
                # Battle
                # Find Battle button
                pos = imagesearch_loop_timeout(folder+"battle_phase.png", 0.1, 5.0)
                print("Battle button found : ", pos[0], pos[1])
                # Click Battle button
                if pos[0] > -1:
                    click_image(folder+"battle_phase.png", pos, "left", 0.1)
                    print("Battle button clicked")

                    # Attack
                    monster = [958, 1084, 834]
                    monster_pos_y = 663

                    for monster_pos in monster:
                        pos = imagesearch_loop_timeout(folder+"action.png", 0.1, 30.0, 0.9)
                        if pos[0] > -1:
                            pa.click(x=monster_pos, y=monster_pos_y)
                            pos = imagesearch_loop_timeout(folder+"change_to_attack_position.png", 0.1, 2.0)
                            if pos[0] > -1:
                                click_image(folder+"change_to_attack_position.png", pos, "left", 0.1)
                                time.sleep(2)
                                pa.click(x=monster_pos, y=monster_pos_y)
                            pos = imagesearch_loop_timeout(folder+"attack.png", 0.1, 2)
                            if pos[0] > -1:
                                click_image(folder+"attack.png", pos, "left", 0.1)
                                # Confirm attack if there is more than 1 monster
                                pos = imagesearch_loop_timeout(folder+"confirm_disabled.png", 0.1, 2.0)
                                if pos[0] > -1:
                                    # Click card to activate
                                    pa.click(x=667, y=793) 
                                    pos = imagesearch(folder+"confirm_enabled.png")
                                    if pos[0] > -1:
                                        click_image(folder+"confirm_enabled.png", pos, "left", 0.1)
            else:
                # Find end phase button
                pos = imagesearch_loop_timeout(folder+"end_phase.png", 0.1, 2)
                print("End phase button found : ", pos[0], pos[1])
                # Click end phase button
                if pos[0] > -1:
                    click_image(folder+"end_phase.png", pos, "left", 0.1)
                    print("End phase button clicked")
            
                main_phase_status = True

        if not main_phase_status and not battle_phase_status:
            main_phase_status = True
            pos = imagesearch_loop_timeout(folder+"action.png", 0.1, 5.0)
            print("Action button found : ", pos[0], pos[1])
            # Click action button
            if pos[0] > -1:
                click_image(folder+"action.png", pos, "left", 0.1)
                main_phase_status = True
                # Find end phase button
                pos = imagesearch_loop_timeout(folder+"end_phase.png", 0.1, 2)
                print("End phase button found : ", pos[0], pos[1])
                # Click end phase button
                if pos[0] > -1:
                    click_image(folder+"end_phase.png", pos, "left", 0.1)
                    print("End phase button clicked")
            
        # Check if duel finished
        pos = imagesearch(folder+"ok.png")
        if pos[0] > -1:
            # duel_counter += 1
            break