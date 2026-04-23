a = input()
ans = ""
# AFB+999999HC-4	
i = 0
while i < len(a):
    #print(a[i])
    if a[i] == "+":
        ans += " tighten "
        i += 1
    elif a[i] == "-":
        ans += " loosen "
        i += 1
    elif a[i] >= "0" and a[i] <= "9":
        while i < len(a) and a[i] >= "0" and a[i] <= "9": #숫자면 계속 ans뒤에 붙여라
            #if not a[i + 1] >= "0" and a[i + 1] <= "9":
            #	print(ans)
            #	ans = ""
            #	break
            ans += a[i]
            i += 1
        print(ans)
        ans = ""
    else:
        ans += a[i]
        i += 1

# def parse_tuning_instructions(instructions):
#     output = []
#     i = 0
#     while i < len(instructions):
#         start = i
#         while i < len(instructions) and instructions[i].isalpha():
#             i += 1
#         strings = instructions[start:i]

#         sign = instructions[i]
#         i += 1

#         start = i
#         while i < len(instructions) and instructions[i].isdigit():
#             i += 1
#         turns = instructions[start:i]

#         action = 'tighten' if sign == '+' else 'loosen'
#         output.append(strings + " " + action + " " + turns)

#     return output

# # Read input
# instructions = input().strip()

# # Parse the tuning instructions
# result = parse_tuning_instructions(instructions)

# # Print the results
# for line in result:
#     print(line)
