

label random_joke:
    $ joke_string_1 = ["Why did the chicken cross the road?", 
     "Why is the obtuse triangle so frustrated?", 
     "Why was the equal sign so humble?",
      "Two pickles fell out of a jar onto the floor. What did one say to the other?",
      "How does a cucumber become a pickle?",
      "What do you think of that new diner on the moon?",
      "Why did the dinosaur cross the road?"]


    $ joke_string_2 = ["To get to the other side!", 
    "Because it is never right!", 
    "Because he wasn't greater or less than anyone",
    "Dill with it.",
    "It goes through a jarring experience.",
    "Food was good, but there really wasn’t much atmosphere.",
    "Because the chicken wasn’t born yet."]


    #$ rjoke = renpy.random.choice(["joke1","joke2","joke3"])
    $ joke_length = len(joke_string_1)
    #"[joke_length]"
    $ rjoke = renpy.random.randint(0,(joke_length-1))
    #"[rjoke]"
     

    $joke_question = joke_string_1[rjoke]
    $joke_response = joke_string_2[rjoke]

    m "[joke_question]"
    m "[joke_response]"

return
