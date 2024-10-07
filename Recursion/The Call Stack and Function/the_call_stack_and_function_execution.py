
def green():
    color = "Jade"
    print("Green")

def red():
    color = "crimson"
    print("Red")
    green()

def blue():
    red()
    print("Blue")

blue()