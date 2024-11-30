'''Author=Ben Mathew Ninan
   Date=30\11\2024
   Program=Right Angle Triangle'''

def is_right_angle_triangle(side1,side2,side3):
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]**2==sides[0]**2 + sides[1]**2:
        return True
    return False


side1=int(input("Enter the side 1 of the triangle:"))
side2=int(input("Enter the side 2 of the trianhle:"))
side3=int(input("Enter the side 3 of the triangle:"))
if is_right_angle_triangle(side1,side2,side3):
    print(f"The given sides are part of the right angle triangle")
else:
    print(f"The given sides are not part of the right angle triangle")