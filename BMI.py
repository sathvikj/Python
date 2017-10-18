x = input("Please enter your name: ")
y = float(input("Please enter your Height in Mtrs: "))
z = float(input("Please enter your Weight in Kg's: "))
B = round(z/(y*y), 2)
if B <= 18.5:
  print("Hello", x," your BMI is", B, "and you are underweight, you must consider putting on some weight")
elif B > 18.5 and B < 30:
  print("Hello", x," your BMI is", B, "and you are normal, say cheeze!!")
elif B > 30:
  print("Hello", x," your BMI is", B, "and you are Obese. Let's see what we can do")

  

  


