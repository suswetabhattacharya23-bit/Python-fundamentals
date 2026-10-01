name = "Selena"
count = 1


def another():
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Selena")


another()

 

# Daily Log: 13

# Timeline Sync ID: 13

# Unique Session ID: 13
