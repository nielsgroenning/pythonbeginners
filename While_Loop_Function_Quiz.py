def quiz_item(question, solution):
    while True:
        answer = input('Here is the question:''\"'+question+'\"''\n')
        if answer == solution:
            print("Correct")
            break
        else:
            print("Try again")

quiz_item("Hvad er klokken", "9")
quiz_item("Hvilken Lufthavn", "Copenhagen")
quiz_item("Danmarks hovedstad", "Copenhagen")