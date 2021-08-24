init:
    find label remy2cont:
        search say "Hungry already, I take it?"
        callto label dwtd_remy2_before_shirtlift
        search menu
        branch "[[Lift your shirt]":
            search say "I pulled up my shirt and exposed my belly to the dragon's gaze. My hands stroked it in a circular motion, caressing the skin, hair and body fat beneath."
            link dwtd_remy2_before_shirtlift_end
            search say "He shooed me out of his apartment after that, and not wanting to make a scene, I left. I'm still not sure what exactly went wrong that evening, but somehow I didn't think he would want to meet with me again."
            callto label dwtd_remy2_shirtlift

label dwtd_remy2_before_shirtlift:
    if not dwtd.check_keypoint():
        menu:
            "[[Lift your shirt]":
                $ renpy.pop_call()
                label dwtd_remy2_before_shirtlift_end:
                    pass
    return

label dwtd_remy2_shirtlift:
    $ dwtd.will_die()
    $ renpy.pop_call()
    
    $ renpy.pause(0.5)
    
    play sound "fx/system3.wav"
    
    s "I'm sorry, but choosing this option was so damn stupid from you, that I'm just gonna kill your character for no reason."
    s "Just be less of an idiot next time, thank you."
    
    call dwtd_deathsound(3)
    show dwtd_youdied_text at Position(xpos = 0.5, ypos = 0.3) with dissolveslow3
    $ renpy.pause(3.0)
    call dwtd_youdied("You died because of being an idiot.")
