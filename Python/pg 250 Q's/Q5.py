import csv

header = ["Event Name", "Location", "Date", "Ticket Price", "Genre"]

data = [["Summer Music Fest", "Berlin", "July 15", "€50", "Pop/Rock"],
        ["Rooftop Concert", "Frankfurt", "August 5", "€25", "Jazz"],
        ["Lakefront Serenade", "Hamburg", "August 20", "€35", "Classical"],
        ["Open Air Disco", "Munich", "September 2", "€30", "Electronic"],
        ["Folk Fest", "Cologne", "September 16", "€40", "Folk"],
        ["Jungle Rhythm", "Dresden", "October 7", "€20", "World Music"]]

with open("events.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

with open("events.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
