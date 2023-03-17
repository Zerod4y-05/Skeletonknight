# some code snippets from: https://github.com/VimislikArt/rpg_fight/blob/main/rpg_fight.rpy
# Commented by OpenAI

define s = Character("Slayer", color="#19090c")
default question_tally = 0                    #A character called Slayer is created and a tally of questions asked is set to 0 used in question_selection.                     

label start:
    scene bg sky                                      
    

show slayer                                   #The scene is set to a sky background and Slayer appears.

label question:                                     
        show slayer at right
        
        s "Are you ready to fight?"           #The player is asked if they are ready to fight and given a menu option to select either yes or no.


        menu:                                               
            "Yes":                                
                show slayer at center with pixellate
               
                s "Of course lets get ready"
                jump fight_scene
            "No":                                 
                "..."
                jump question_selector        #If no is chosen, loop the question

label question_selector:
    if question_tally == 0:
        s "Do you really want to give up now?"
        menu:
            "Yes":
                s "Coward..."
                $ renpy.full_restart()
            "No":
                s "Good! Let's go!"
                $ question_tally += 1
                jump fight_scene
    

label fight_scene:                              #The fight scene is set with a black background, castle background, Slayer idle, and skeleton idle.
show bg_black:
        pos (-129, -272) zpos 0.0 zoom 4.29 


show bg_castle:
        pos (141, 26) zpos 0.1 zoom 4.14 


show slayer_idle:
        pos (586, 265) zpos 0.2 zoom 6.41 



show skeleton_idle:
        pos (873, 244) zpos 0.2 rotate -2.0 zoom 7.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 

    
camera:
        pos (-132, -297) rotate 0.0 

label fightmenu:
    $ player_hp = 10
    $ enemy_hp = 6                  #The player's health and enemy health are both set to 10 and 6 respectively. 

    while player_hp > 0:            #A while loop is initiated and while the player's health is greater than 0, they can choose to either attack or not attack.
        hide skeleton_attack
        show skeleton_idle
        # Player Turn

        menu:
            "Attack":                               
                hide slayer_idle
                show slayer_attack:
                    pos (665, 277) zpos 0.2 yzoom 1.0 zoom 6.31 
                hide skeleton_idle
                show skeleton_hit:
                    pos (873, 244) zpos 0.2 rotate -2.0 zoom 7.0 

                $ enemy_hp -= 2                                             #Enemy health is reduced by 2 if the player chooses to attack.
                "That's a strong hit!  Enemy has [enemy_hp] hp!"
                hide slayer_attack
                show slayer_idle:
                    pos (586, 265) zpos 0.2 zoom 6.41 
                hide skeleton_hit
                show skeleton_idle:
                    pos (873, 244) zpos 0.2 rotate -2.0 zoom 7.0 
                if enemy_hp <= 0:                                           #If the enemy's health reaches 0, the player is declared as the winner and given a victory menu to either replay the level or go back to the main menu.
                    hide skeleton_idle
                    hide skeleton_hit
                    show skeleton_dead:
                        pos (1040, 284) zpos 0.2 yzoom 1.0 zoom 7.0 
                    hide slayer_hit
                    show slayer_victory:
                        pos (541, 276) zpos 0.2 zoom 6.51 
                    "You win the combat encounter!"
                    jump victory_menu
            "Don't Attack":
                "You don't attack..."

        # Enemy Turn
        $ player_hp -= 2                #The enemy makes an attack, reducing the player's health by 2. 
        hide skeleton_idle
        show skeleton_attack:
            subpixel True pos (835, 235) zpos 0.2 yzoom 1.0 zoom 6.91 
        hide slayer_idle
        show slayer_hit:
            subpixel True pos (495, 59) zpos 0.2 zoom 5.61 



        "The Enemy makes an attack, reducing you to [player_hp] hp!"
        hide slayer_hit
        show slayer_idle:
            pos (586, 265) zpos 0.2 zoom 6.41 
        hide skeleton_attack
        show skeleton_idle:
            pos (873, 244) zpos 0.2 rotate -2.0 zoom 7.0 
    hide slayer_attack
    hide slayer_idle
    hide slayer_hit
    
    show slayer_death:          
        pos (608, 373) yzoom 1.0 zoom 5.5 
    "You died..."

    menu victory_menu:
        "Play this level again?":
            hide skeleton_dead
            show skeleton_idle:
                pos (873, 244) zpos 0.2 rotate -2.0 zoom 7.0 
            hide slayer_victory
            show slayer_idle:
                pos (586, 265) zpos 0.2 zoom 6.41
            jump fightmenu
        "Back to Main Menu":
            $ renpy.full_restart()