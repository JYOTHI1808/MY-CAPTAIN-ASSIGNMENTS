#PYTHON PROGRAM TO ACCEPT A FILENAME FROM THE USER AND PRINT THE EXTENSION OF THAT
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

