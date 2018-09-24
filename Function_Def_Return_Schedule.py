# [ ] add a 3rd period parameter to make_schedule
def make_schedule(period1, period2, period3):
    schedule = ("[1st] " + period1.upper() + ", [2nd] " + period2.lower() + ", [3rd] " + period3.title())
    return schedule

student_schedule = make_schedule("math", "science", "dansk")
print("Schedule", student_schedule)

# [ ] Optional - print a schedule for 6 classes (Tip: perhaps let the function make this easy)

