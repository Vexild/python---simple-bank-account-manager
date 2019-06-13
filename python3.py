
def Task3Function():
    dictionary ={}
    result = ""
    for i in range(1,20):
        dictionary[i] = i**2
        result += str(i)+'**2='+str(dictionary[i])+", "
    return result

if __name__== "__main__":
  print(Task3Function())
