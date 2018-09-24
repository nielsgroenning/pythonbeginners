end = 6
var = 0
total = 0
while True:
    if end > 0:
        end = end - 1
        var = var + 1
        total = var + total
    else:
        print(total)
        break

