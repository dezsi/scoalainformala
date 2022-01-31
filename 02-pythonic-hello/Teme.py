#Exercitii
#1.)

#months = ['January', 'February', 'March']
#months.append('April')
#print(months)

#month=['January', 'February', 'March']
#month.insert(3, 'April')
#print('list ', month)

#2.)

#sentence = 'Mary had a little lamb'
#count = 0
#for i in sentence:
#    if i == "t":
 #       count = count + 1
#print(count)

#3.)

#import re

#regex = '^[a-zA-Z+0-9]+[\._]?[a-z0-9]+[@]\w+[.][a-zA-Z]'


#def check(email):
 #   if (re.search(regex, email)):
 #       print("Valid Email")
 #   else:
 #       print("Invalid Email")




#if __name__ == '__main__':
  #  email = "rohit.gupta@mcnsolutions.nem"
  #  check(email)

  #  email = "praveen@c-sharpcorner.com"
  #  check(email)

  #  email = "inform2Atul@gmail.com"
  #  check(email)

  #4.)

#import re


#def isValid(s):
    # 1) Begins with 0 or 91
    # 2) Then contains 7 or 8 or 9.
    # 3) Then contains 9 digits
  #  Pattern = re.compile("(400|74)?[1-9][0-9]{10}")
  #  return Pattern.match(s)


# Driver Code
#s = "400752151319"
#if (isValid(s)):
    #print("Valid Number")
#else:
   # print("Invalid Number")

#5.)

