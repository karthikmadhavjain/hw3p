#Author: Karthik Madhav Jain kmj5614@psu.edu

def digit_sum(n):
  summation = 0
  summation = summation + (n%10)
  if (n//10)>0:
    summation = n%10 + digit_sum(n//10)
    return summation
  return summation

def run():
  integer = int(input('Enter an int: '))
  summedup = digit_sum(integer)
  print(f"sum of digits of {integer} is {summedup}.")
  return 0;

if __name__ == "__main__":
  run()

