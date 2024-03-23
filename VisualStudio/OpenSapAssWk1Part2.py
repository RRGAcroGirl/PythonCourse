angle_1 = int(input("Please enter the degreee of angle 1 of your triangle:"))
angle_2 = int(input("Please enter the degreee of angle 2 of your triangle:"))
angle_3 = int(input("Please enter the degreee of angle 3 of your triangle:"))

angle_sum = angle_1 + angle_2 + angle_3
if angle_sum != 180:
    print("The entered values are not valid.")

elif (angle_1 > 0) and (angle_2 > 0) and (angle_3 > 0):
    if (angle_1 == 90) or (angle_2 == 90) or (angle_3 == 90):
        print("The triangle is a right triangle.")
    if (angle_1 > 90) or (angle_2 > 90) or (angle_3 > 90):
        print("The triangle is an obtuse triangle.")
    if (angle_1 < 90) and (angle_2 < 90) and (angle_3 < 90):
        print("The triangle is an acute triangle.")
else:
    print("Angles smaller than 0 are not valid.")