run_again = ""
while run_again == "":
    num1=float(input("Enter the number1:"))
    num2=float(input("Enter the number2:"))
    operator=input("enter the operator(+,-,*,/):")
    if operator =="+":
      print("result:",num1+num2)
    elif operator =="-":
      print("result:",num1-num2)
    elif operator =="*":
      print("result:",num1*num2)
    elif operator =="/":
      if num2 == 0:
        print("Divided by zero is not allowed")
      else:    
        print("result:",num1/num2)
    else:
      print("please enter the valid operator.")

    run_again = input("Press Enter to continue,or type 'Q' to quit: ")