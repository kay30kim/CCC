P = int(input())
N = int(input())
R = int(input())

total_infected = N
current_day_infected = N 
day = 0

while total_infected <= P:
    day += 1
    current_day_infected *= R 
    total_infected += current_day_infected 

print(day)