def playTenis(outlook, humidity, wind):
    if outlook == "Overcast":
        return "Yes"
    elif outlook == "Sunny":
        if humidity == "High":
            return "No"
        else:
            return "Yes"
    else:
        if wind =="Strong":
            return "No"
        else:
            return "Yes"
tenisdict = {
    "R": ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No'],
    "O": ["Sunny", "Sunny", "Overcast", "Rain", "Rain", "Rain", "Overcast", "Sunny", "Sunny", "Rain", "Sunny", "Overcast", "Overcast", "Rain"],
    "H": ["High", "High", "High", "High", "Normal", "Normal", "Normal", "High", "Normal", "Normal", "Normal", "High", "Normal", "High"],
    "W": ["Weak", "Strong", "Weak", "Weak", "Weak", "Strong", "Strong", "Weak", "Weak", "Weak", "Strong", "Strong", "Weak", "Strong"]
    }

results = []
counter = 0
while counter != 14:
    x = playTenis(tenisdict["O"][counter], tenisdict["H"][counter], tenisdict["W"][counter])
    results.append(x)
    counter += 1
print(results)
if results == tenisdict["R"]:
    print("Accuracy = 100%")
else:
    print("not accurate L")
