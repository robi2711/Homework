print("Height in metres, Weight in kilos")
def bmi(weight, height):
  result = weight/(height**2)
  return(result)
w = [50, 70, 90, 90]
h = [165, 170, 180, 170]
while len(w) != 0:
  i = (bmi(w[0], h[0]))*10000
  if i < 18.5:
    print("You are underweight")
  elif i < 24.9 and i > 18.5:
    print("You are normal weight")
  elif i < 29.9 and i > 25:
    print("You are overweight")
  else:
    print("You are obese")
  del w[0]
  del h[0]



