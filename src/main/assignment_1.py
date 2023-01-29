# Daina Diedrick
# COT 4500
# Assignment #1
import numpy as np

# Question #1: Use double precision, calculate the resulting values (format to 5 decimal places
  # 010000000111111010111001
def double_pre(s, c, f):
    d: double = ((-1)^s)*(2^(c-1027))*(1+f)
    return d
s=0
c=2^10+2^2+2^1+2^0
f=2^(-1)+2^(-2)+2^(-3)+2^(-5)+2^(-7)+2^(-8)+2^(-9)+2^(-12)
print(double_pre(s,c,f))
print("\n")

# Question #2: Chop
def chop(num,places):
  ch: double = num*(10**(-(places)))
  return ch
ch = str(chop(double_pre(s,c,f),4))
print(str(ch[0:5]))
print("\n")


#Question #3: Round
def ro_und(num,places):
  ro: double = num*(10**(-(places)))+(5*10**(-(places-1)))
  return ro
ro = str(ro_und(double_pre(s,c,f),4))
print(str(ro[0:5]))
print("\n")


#Question #4: Absolute and Relative Error
