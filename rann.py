def ran():
    import random
    while True:
        i = random.randint(0, 100)
        yield i
        if i > 90 :
            break


if __name__ == "__main__":
    for i in ran():
        print(i)
    print([s for s in ran()])