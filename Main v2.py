answers = ("Hudson", "9th",
           "Success would be for me to complete the class with a newfound understanding for programs and the computers and engines that run them.",
           "I would like to take the knowledge I have about programs and code and expand that to be able to apply it.",
           "Be understanding and accept feedback. "
           "Sometimes things don’t work and it’s important that we can work it out.",
           "I like to show things to friends and family.",
           "I love to learn things, whether it’s a new mechanic in a game or a theory about how the world works.",
           "Probably an animation assignment. "
           "We were tasked with creating a short animation with google slide explaining the growth of an ecosystem.",
           "Probably access to technology. It is an incredibly powerful tool that many people don’t have access to.",
           "Definitely access to information. People are able to find out about things almost as they happen, "
           "even if it’s on the other side of the world. It’s kind of a double-edged sword. On one hand, "
           "you have the entirety of human knowledge in a device that fits in your pocket, "
           "but it also allows for misinformation to be spread easily as well.")

questions = ("1. What is your name?", "2. What grade are you in?", "3. What does success look like to you in this class",
             "4. What are your goals in relation to this class?",
             "5. What can your teacher do to make you feel welcome in class?",
             "6. How would you like your accomplishments to be celebrated?",
             "7. What is something new about yourself?",
             "8. What's the coolest assignment you've ever done?",
             "9. What problem do you want to solve?",
             "10. What is the biggest impact computers have made on society? Is that impact positive or negative?")
qnumber = 0

# Catches invalid inputs and clarifies valid inputs to user
def invalid():
    validq = str.upper(input("Invalid input. Must be a number between 1 and 10. OK?"))
    # print(validq)
    if validq == "YES":
        pass
    else:
        while validq != "YES":
            print("Answer must be yes.")
            validq = str.upper(input("Invalid input. Must be a number between 1 and 10. OK?"))


while True:
    # resets q to repeat the loop
    qnumber = 0
    
    # prints questions
    for q in questions:
        print(questions[qnumber])
        qnumber = qnumber + 1

    # determines what question user wants to ask
    qask = input("Which question would you like to ask?")
    if qask.isnumeric():
        qask = int(qask) - 1
    else:
            invalid()
            qask = "invalid"
    
    if str(qask).isnumeric():  # Checks if input is an integer
        if qask+1 <= 10:  # Verifies input is withing range
            print()
            print(questions[qask])
            print(answers[qask])
            nextq = str.upper(input("Do you want to ask another question?"))
            if nextq == "YES":
                pass
            else:
                break
        else:
            invalid()
    elif qask == "invalid":
        pass
    else:
        invalid()
