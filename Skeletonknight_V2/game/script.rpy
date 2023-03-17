define s = Character("Slayer", color="#19090c")
default question_tally = 0

label start:
    scene bg sky

show slayer

label question:
    show slayer at right
    
    s "Are you ready to fight?"
    
    menu:
        "Yes":
            show slayer at center with pixellate
            
            s "Of course lets get ready"
            jump fight_scene
        "No":
            "..."
            jump question_selector

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

label fight_scene:
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
    $ enemy_hp = 6

    while player_hp > 0:
        hide skeleton_attack
        show skeleton_idle
        # Player Turn
        menu:
            "Attack":
                hide slayer_idle
                show slayer_lightattack:
                    pos (577, 235) zpos 0.2 yzoom 1.0 zoom 6.31 
                    
                hide skeleton_idle
                show skeleton_hit:
                    pos (873, 244) zpos 0.2 rotate -2.0 zoom 7.0 
                $ enemy_hp -= 2
                "That's a strong hit!  Enemy has [enemy_hp] hp!" 
                hide slayer_lightattack
                show slayer_idle:
                    pos (586, 265) zpos 0.2 zoom 6.41 
                hide skeleton_hit
                show skeleton_idle:
                    pos (873, 244) zpos 0.2 rotate -2.0 zoom 7.0 
                if enemy_hp <= 0:
                    hide skeleton_idle
                    hide skeleton_hit
                    show skeleton_dead:
                        pos (1040, 284) zpos 0.2 yzoom 1.0 zoom 7.0 
                    hide slayer_hit
                    show slayer_victory:
                        pos (541, 276) zpos 0.2 zoom 6.51 
                    "You win the combat encounter!"
                    jump victory_menu
            "Heavy Attack":                                                  #Heavy attack 
                hide slayer_idle
                show slayer_heavyattack:                                 
                    pos (665, 277) zpos 0.2 yzoom 1.0 zoom 6.31 
                hide skeleton_idle
                show skeleton_hit:
                    pos (873, 244) zpos 0.2 rotate -2.0 zoom 7.0 
                $ enemy_hp -= 4
                "That's a heavy hit!  Enemy has [enemy_hp] hp!"
                hide slayer_heavyattack
                show slayer_idle:
                    pos (586, 265) zpos 0.2 zoom 6.41 
                hide skeleton_hit
                show skeleton_idle:
                    pos (873, 244) zpos 0.2 rotate -2.0 zoom 7.0 
                if enemy_hp <= 0:
                    hide skeleton_idle
                    hide skeleton_hit
                    show skeleton_dead:
                        pos (1040, 284) zpos 0.2 yzoom 1.0 zoom 7.0 
                    hide slayer_hit
                    show slayer_victory:
                        pos (541, 276) zpos 0.2 zoom 6.51 
                    "You win the combat encounter!"
                    jump victory_menu
            "Dodge":
                jump dodge
            "Don't Attack":
                "You don't attack..."

        # Enemy Turn
        $ player_hp -= 2
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
        hide slayer_lightattack
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

label dodge:
        show skeleton_attack:
            subpixel True pos (835, 235) zpos 0.2 yzoom 1.0 zoom 6.91 
        hide skeleton_idle
        hide slayer_idle
        show slayer_dodge:
            pos (347, -37) zoom 6.69 

 

        $ dodge_chance = renpy.random.randint(1, 3)
        if dodge_chance == 1:
            "You successfully dodged the enemy's attack!"
            hide slayer_dodge
            hide skeleton_attack
            show slayer_idle:
                pos (586, 265) zpos 0.2 zoom 6.41 
            show skeleton_idle:
                pos (873, 244) zpos 0.2 rotate -2.0 zoom 7.0 
            jump fightmenu
        else:
            hide slayer_dodge
            show slayer_idle:
                pos (586, 265) zpos 0.2 zoom 6.41 
            $ player_hp -= 2
            hide skeleton_idle
            show skeleton_attack:
                subpixel True pos (835, 235) zpos 0.2 yzoom 1.0 zoom 6.91 
            hide slayer_idle
            show slayer_hit:
                subpixel True pos (495, 59) zpos 0.2 zoom 5.61 
            "The Enemy made an attack, reducing you to [player_hp] hp!"
            hide slayer_hit
            show slayer_idle:
                pos (586, 265) zpos 0.2 zoom 6.41 
            hide skeleton_attack
            show skeleton_idle:
                pos (873, 244) zpos 0.2 rotate -2.0 zoom 7.0 
            jump fightmenu