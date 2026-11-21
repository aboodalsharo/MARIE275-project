with open("test1.mas") as f:
    for num, line in enumerate(f, 1):
        text = line.rstrip()
        print(f"{num}: {text}")

        

        

        