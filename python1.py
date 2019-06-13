
def Task1Function():
    numberList = list(range(2000, 3200))
    rightValues = []
    for i in numberList:
        if i%7 ==  0 and i%5 != 0:
            rightValues.append(i)
    return rightValues

if __name__== "__main__":
  print(Task1Function())
