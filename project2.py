  #PROJECT ON LOOPS
  #PYTHON PROGRAM FOR FIBONACCI NUMBERS
  def fibonacci(n):
    a=0
    b=1
    for i in range(0,n):
      temp = a
      a = b
      b =temp +b
    return a

 for c in range(0, 13):
    print(fibonacci(c))
