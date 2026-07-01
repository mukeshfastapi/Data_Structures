# This is time Bomb problem
def timebomb(n):
    if n <= 0:
        print("Blast Off!")
    else:
        print(n)
        timebomb(n - 1)

timebomb(2)