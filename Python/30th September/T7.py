import random
fish = int(input("How many portions of fish? > "))
chips = int(input("How many portions of chips? > "))
tfish = fish*4.5
tchips = chips*2.8
print(f"""
        Order num{random.randint(1, 100)}
        Fish x{fish}     {tfish}
        Chips x{chips}   {tchips}
        Total {tfish+tchips}
""")
