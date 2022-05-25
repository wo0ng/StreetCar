def solution(cars):
    total = 0
    v = 0
    for car in cars:
        if car == 0:
            v += 1
        else:
            total += v
        return total
      
      
