#!/bin/python3

def birthdayCakeCandles(candles):
    max_value = max(candles)
    data = []
    for i in range(len(candles)):
        if candles[i] == max_value:
            data.append(candles[i])
    return (len(data))        
  
if __name__ == '__main__':
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    birthdayCakeCandles(candles)

