import time

def b_to_d():

    #Binary to Denary conversion  
    binary = input("Input a number in binary:")  
    denary = 0  
    for digit in binary:  
      
      denary = denary*2 + int(digit)  
    print("Your denary number is: " + str(denary))  
    return

def d_to_b():
    #Denary to Binary conversion  
    denary = int(input("Input a denary number:"))  
    binary=""  
    while denary>0:  
    
      binary = str(denary%2) + binary  
      denary = denary//2  
    print("Your binary number is: " + binary) 
    return

print("Choose from denary to binary or from binary to denary. For the former type '0' and for the latter type '1'.")
decider = input()
decider = int(decider)
if decider == 0:
  d_to_b();
elif decider == 1:
  b_to_d();

time.sleep(10); 
quit();