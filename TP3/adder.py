import sys
import re

def adder(text):
    sum = 0
    summing = True
    data_list = re.findall(r"(on|off|=|\d+)",text,re.IGNORECASE)
    for elem in data_list:
        if elem.isnumeric() and summing:
            sum += int(elem)
        elif elem.lower() == "on":
            summing = True
        elif elem.lower() == "off":
            summing = False
        elif elem == "=":
            print(sum)

if __name__ == "__main__":
    adder(sys.stdin.read())