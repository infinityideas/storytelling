# The script of the game goes in this file.
#BBN CLASS EXAMPLE 1



# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define pov = Character("[povname]")
#default povname = "Pat Smith"

default music_preference = False
define scale_factor_markus = .21

define m = Character("Markus", image = "markus")
# color="#c8ffc8", what_text_align=1.0)
define a = Character("Alice", image = "alice")
#color ="#63B2C6")


#image alice:
#    "FWH neutral01.png"
#    xzoom 0.45 yzoom 0.45
#image alice happy:
#    "FWH smile01.png"
#   xzoom 0.45 yzoom 0.45

image alice = im.FactorScale("FWH neutral01.png", 0.5, bilinear = True)
image alice happy = im.FactorScale("FWH smile01.png", 0.5, bilinear = True)

image bg school: 
    "class1.jpg"
    on show:
        ease 10 zoom 0.75




image markus:
    "boy a_casual_normal.png"
    xzoom scale_factor_markus yzoom scale_factor_markus
image markus happy:
    "boy a_casual_happy.png"
    xzoom scale_factor_markus yzoom scale_factor_markus
image markus angry:
    "boy a_casual_angry.png"
    xzoom scale_factor_markus yzoom scale_factor_markus
image markus shocked:
     "boy a_casual_shocked.png"
     xzoom scale_factor_markus yzoom scale_factor_markus
#image markus fluster:
    #"boy a_casual_flustered.png"
    #xzoom scale_factor_markus yzoom scale_factor_markus
image markus fluster = im.FactorScale("boy a_casual_flustered.png", scale_factor_markus, bilinear = True)

default play_music = False

#image sparkle_animation:
 #   "boy a_casual_normal.png"
 #   xzoom scale_factor_normal yzoom scale_factor_markus
 #   0.1
 #   "boy a_casual_happy.png"
 #   xzoom scale_factor_normal yzoom scale_factor_markus
 #   0.1
 #   "boy a_casual_shocked.png"
 #   xzoom scale_factor_markus yzoom scale_factor_markus
 #   0.1
 #   "boy a_casual_angry.png"
 #   xzoom scale_factor_markus yzoom scale_factor_markus
 #   repeat

#image alice rising:
#    on show:
#        "FWH neutral01.png"
#        xzoom 0.45 yzoom 0.45
#        xalign 0.0 yalign -0.5
#        linear 10.0 xalign 0.0 yalign 0.5
 #   repeat


transform down_to_up:
    on show:
        xalign 0.0 yalign -5.0
        linear 3.0 xalign 0.0 yalign 0.5

transform slowly_right:
    linear 3.0 xalign 1.0 yalign 0.5

transform scaled:
    on show:
        xzoom 0.2 yzoom 0.2

screen voice_toggle:
    vbox:
        textbutton "Mute Markus" action ToggleVoiceMute("Markus")
        textbutton "Mute Alice" action ToggleVoiceMute("Alice")



#image side markus:
   # Image("boy a_casual_normal.png", yalign=1.0, xalign=0.0)
    #xzoom 0.1 yzoom 0.1
#image side markus happy:
    # "boy a_casual_happy.png"
     #xzoom 0.05 yzoom 0.05
#image side markus angry:
    #"boy a_casual_angry.png"
    #xzoom 0.05 yzoom 0.05
#image side markus shocked:
        #"boy a_casual_shocked.png"
        #xzoom 0.05 yzoom 0.05

#define flash = Fade(0.1, 0.0, 0.5, color="#fff")

#init python:
 #   define.move_transitions("ease", 3.0)

# The game starts here.

label start:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # DEFINITION scene : deletes all visuals on screen
    # and displays background image
    #play music "01town1.ogg"
    scene bg school 
    

    #show screen voice_toggle
    show text "Hello and welcome to the joke game" at truecenter
    with dissolve
    pause(1.0)
    hide text
    with dissolve

    show text "Would you like to hear music" at truecenter
    with dissolve
    pause(1.0)
    hide text
    with dissolve

    menu:
        "Yes to music":
            $music_preference = True
            
        "No to music":
           $music_preference = False 
   
    if music_preference:
        play music "01town1.wav" fadein 1.0
    else:
        show text "No music will be played" at truecenter
        with dissolve
        pause(1.0)
        hide text
        with dissolve

    #show sparkle_animation

    show markus with dissolve
    m "Hey my name is Markus!" 
   

    #show markus at scaled with easeinright
    #show markus at down_to_up 
    #show alice at down_to_up with dissolve
    

    

    m "Want to hear a joke?"

    menu:
        "Yes":
            m "Why is a math book always unhappy?"
            m "Because it aways has problems!"
            show markus happy
        "no":
            show markus shocked
            m "Boy! You do not have a sense of humor"
            jump donelabel 

    
    m "Want to hear another joke?"

    menu:
        "Yes":
            m "Why is 6 afraid of 7?"
            m "Because 7 8 9!"
            show alice at left with dissolve
            #show alice at down_to_up with dissolve
            #play sound "Spelll7.wav"
            
            #show alice at left with dissolve
            play sound "Gasp 2.wav"
            show markus angry
            pause(2.0)
            m "what?"
            a "I am the {i}witch {/i}of unfunny jokes!"
            a "...and that was {b}not{/b} a funny joke!"
            
            #show markus fluster at right
            show markus fluster 
            show markus fluster at slowly_right
            m "I am doing my best!"          
            pause(1.0)
            m "I will try better next time!"
            show alice happy
            a "That is all I can ask"
            a "thank you for working on your jokes"
            show markus 
            a "My work here is done. I will see you later!"
            hide alice with dissolve
            m "bye!"
            jump donelabel
            
        "no":
            jump donelabel
    
        #call random_joke
    

    label donelabel: 
        show markus
        m "Thanks for listening!"



    
return



  