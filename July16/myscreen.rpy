

screen joke_screen:
    frame:
        xpadding 10
        ypadding 10
        xalign 1.0
        yalign 0.0
        background Solid("#0000007F")
        hbox:
            imagebutton:
                idle "laugh_button" 
                hover "laugh_button"
                action SetVariable("score", score + 1 ) 
            text "Good jokes Responses: [score]"
            #textbutton "add to jokes" action SetVariable("score", score + 1 ) 

#screen music_screen:
#    frame:
#        xpadding 10
#        ypadding 10
#        xalign 1.0
#        yalign 0.0
#        textbutton "toggle music" 