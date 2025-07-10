x = input("hello brother")

def playback(x):
    x = x.split()
    return print(*x, sep="...")

playback(x)