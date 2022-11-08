import random

if __name__ == '__main__':
    result = [False for i in range(100)] #false false false... * 100
    prisoners = list(range(1, 101)) #1..100 * 100
    randomlist = random.sample(range(1, 101), 100) #1..100 * 100
    for i in prisoners:
        seat = i
        loop = []
        loop.append(randomlist[seat - 1])  # add first seat
        for j in range(50):
            seat = randomlist[loop[-1]-1] # get the new seat
            loop.append(seat)
            if seat == i:
                result[i-1] = True
                break
    madeIt = 0
    for i in result:
          if i == True:
              madeIt = madeIt + 1

    print(randomlist)
    print(result)
    print(madeIt)

