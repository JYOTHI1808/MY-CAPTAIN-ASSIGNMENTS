  #PROJECT ON DATA STRUCTURES

#PYTHON PROGRAM WHICH ACCEPTS THE RADIUS OF A CIRCLE FROM THE USER AND COMPUTES AREA

r = float(input("input the radius of the circle : "))
pi = 3.14159
print("the area of the circle with radius"+str(r) +"is :"+ str (pi*r**2))


#PYTHON PROGRAM TO ACCEPT A FILENAME FROM THE USER AND PRINT THE EXTENSION OF THAT


filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
