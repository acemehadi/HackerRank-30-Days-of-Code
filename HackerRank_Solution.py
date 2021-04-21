import sys

s = input(":").strip()

try:
    s = int(s)
    print(s)
except:
    print("Bad String")