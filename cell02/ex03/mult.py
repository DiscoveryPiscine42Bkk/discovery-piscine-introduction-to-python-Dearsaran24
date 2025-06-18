num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = num1*num2
print(f"{num1} x {num2} = {num3}")
if num3 > 0 :
  print("The result is positive.")
elif num3 < 0 :
  print("The result is negative.")
elif num3 == 0 :
  print("The result is positive and negative.")
