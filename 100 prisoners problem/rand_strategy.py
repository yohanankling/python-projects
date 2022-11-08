import random

if __name__ == '__main__':
    result = [False for i in range(100)]
    prisoners = list(range(1, 101)) #1..100 * 100
    randomlist = random.sample(range(1, 101), 100) #1..100 * 100
    for i in prisoners:
        randomchoose = random.sample(range(0, 100), 50) #1..100 * 50
        choosenseats = []
        for seat in randomchoose:
            choosenseats.append(randomlist[seat])
            if seat == i:
                result[i] = True
                break
    madeIt = 0
    for i in result:
          if i == True:
              madeIt = madeIt + 1

    print(randomlist)
    print(result)
    print(madeIt)

