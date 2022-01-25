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

import datetime




def compact(number):
    """Convert the number to the minimal representation. This strips the
    number of any valid separators and removes surrounding whitespace."""
    return clean(number, ' -').strip()


def calc_check_digit(number):
    """Calculate the check digit for personal codes."""
    # note that this algorithm has not been confirmed by an independent source
    weights = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
    check = sum(w * int(n) for w, n in zip(weights, number)) % 11
    return '1' if check == 10 else str(check)


def get_birth_date(number):
    """Split the date parts from the number and return the birth date."""
    number = compact(number)
    centuries = {
        '1': 1900, '2': 1900, '3': 1800, '4': 1800, '5': 2000, '6': 2000,
    }  # we assume 1900 for the others in order to try to construct a date
    year = int(number[1:3]) + centuries.get(number[0], 1900)
    month = int(number[3:5])
    day = int(number[5:7])
    try:
        return datetime.date(year, month, day)
    except ValueError:
        raise InvalidComponent()


def validate(number):
    """Check if the number is a valid VAT number. This checks the length,
    formatting and check digit."""
    number = compact(number)
    if not isdigits(number):
        raise InvalidFormat()
    # first digit should be a known one
    # (7,8=foreign resident, 9=other foreigner but apparently only as NIF)
    if number[0] not in '123456789':
        raise InvalidComponent()
    if len(number) != 13:
        raise InvalidLength()
    # check if birth date is valid
    get_birth_date(number)
    # TODO: check that the birth date is not in the future
    # number[7:9] is the county, we ignore it for now, just check last digit
    if calc_check_digit(number[:-1]) != number[-1]:
        raise InvalidChecksum()
    return number


def is_valid(number):
    """Check if the number is a valid VAT number."""
    try:
        return bool(validate(number))
    except ValidationError:
        return False