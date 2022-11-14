def fixMachine[working, should]:
    if working = "No":
        if should = "No":
            return "No problem"
        else:
            return "Apply lubricant"
    else:
        if should = "No":
            return "Apply tape"
        else:
            return "No problem"


machine = {
    "W": ["No", "No", "Yes", "Yes"],
    "L": ["No", "Yes", "No", "Yes"]
    }


