import csv

header = ["Name", "Surname", "DOB", "Age"]

data = [["Summer Music Fest", "Berlin", "July 15", "€50", "Pop/Rock"],
        ["Rooftop Concert", "Frankfurt", "August 5", "€25", "Jazz"],
        ["Lakefront Serenade", "Hamburg", "August 20", "€35", "Classical"],
        ["Open Air Disco", "Munich", "September 2", "€30", "Electronic"],
        ["Folk Fest", "Cologne", "September 16", "€40", "Folk"],
        ["Jungle Rhythm", "Dresden", "October 7", "€20", "World Music"]]
while True:
    menu = input("""What do you want to do?
    1. Add new member
    2. Show list
    3. Exit""")
    if menu == "1":
        
    elif menu == "2":
      with open("events.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    elif menu == "3":
        quit()
    else:
        print("input not accepted")
    with open("events.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)



