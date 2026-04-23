def find_best_days(n):
    availability = [0 for _ in range(5)]

    for i in range(n):
        days = input().strip()
        for j in range(5):
            if days[j] == 'Y':
                availability[j] += 1

    max_attendance = max(availability)

    best_days = []
    for i in range(5):
        if availability[i] == max_attendance:
            best_days.append(i + 1)

    return ','.join(map(str, best_days))

n = int(input())
result = find_best_days(n)

print(result)