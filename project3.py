      #FUNCTIONS
       #PROGRAM TO CREATE A FUNCTION
 def most_frequent(string):
    j = dict()
    for key  in string:
        if key not in j:
          j[key] = 1
        else:
                j[key] +=1
    return j
print ( most_frequent('mississippi'))
        

