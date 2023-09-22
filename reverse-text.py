reverse_input = input("Enter text to be reversed! ")
letter_list = []

for i in reversed(reverse_input):
    letter_list.append(i)

print(*letter_list, sep="")