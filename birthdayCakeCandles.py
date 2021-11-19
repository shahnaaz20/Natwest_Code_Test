def birthdayCakeCandles(candels):
    max = 0
    count = 0
    for candel in candels:
        if candel > max:
            max = candel
            count = 1
        elif candel == max:
            count+=1
    return count

n = int(input("number of candels"))
candels = list(map(int, input().split()[:n]))
print(birthdayCakeCandles(candels))

