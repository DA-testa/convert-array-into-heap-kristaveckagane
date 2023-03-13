# python3

def build_heap(data):
    swaps = []
    for i in range(n // 2, -1, -1):
        while True:
          leftchild = 2*i+1
          rightchild = 2*i+2
          if leftchild < n and data[leftchild] < data[i]:
           mazaks = leftchild
          else:
            mazaks = i
          if rightchild < n and data[rightchild] < data[i]:
           mazaks = rightchild
          if mazaks == i:
            break
          swaps.append((i,mazaks))
          data[i], data[mazaks] == data[mazaks], data[i]
          i = mazaks

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    ievade = input("").strip()
    if "f" == ievade.lower():
        file = input("").strip()
        read = file.readlines()
        n = int(read[0])
        numbers = read[1].split()
        data = [int(x) for x in numbers]
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
          print(i, j)
    if "i" == ievade.lower():
    # input from keyboard
     n = int(input())
     data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
     assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
     swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
     print(len(swaps))
     for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
